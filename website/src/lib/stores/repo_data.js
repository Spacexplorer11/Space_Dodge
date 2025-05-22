import {derived, readable} from 'svelte/store';

export const repoData = readable({contributors: [], commit_count: 0, total: 0}, set => {
    if (typeof window === 'undefined') return;

    function generateUUID() {
        return ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, c =>
            (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
        );
    }

    let deviceId = localStorage.getItem("DEVICE_ID");
    if (!deviceId) {
        deviceId = generateUUID();
        localStorage.setItem("DEVICE_ID", deviceId);
    }

    const stored = localStorage.getItem("lastGithubPayload");
    if (stored) {
        try {
            const parsed = JSON.parse(stored);
            update(parsed);
        } catch {
        }
    }

    const url = new URL("https://github-backend.spacexplorer11.workers.dev/sse");
    url.searchParams.set("device_id", deviceId);

    const sse = new EventSource(url.toString());

    function update(data) {
        const contributors = (data.contributors || []).filter(c =>
            (c.contributions ?? c.total) != null &&
            (c.login || c.author?.login)
        );

        const total = contributors.reduce(
            (sum, c) => sum + (c.contributions ?? c.total), 0
        );

        set({
            contributors,
            commit_count: data.commit_count || 0,
            total
        });

        localStorage.setItem("lastGithubPayload", JSON.stringify(data));
    }

    sse.onmessage = e => {
        try {
            update(JSON.parse(e.data));
        } catch {
        }
    };

    return () => {
        sse.close();
    };
});

export const contributorsWithPct = derived(repoData, $data =>
    ($data.contributors ?? [])
        .map(c => ({
            ...c,
            percent: $data.total > 0
                ? Math.round(((c.contributions ?? c.total) / $data.total) * 1000) / 10
                : 0
        }))
        .sort((a, b) => b.percent - a.percent)
);