<script>
  import { contributorsWithPct } from '$lib/stores/repo_data.js';
</script>
<div id="container">
<div id="header">
	  <h1>Contributors</h1>
	  <h2>Space Dodge is a collaborative project.</h2>
	  <h2>This page is to thank our contributors!</h2>
	  <h3>Contributors:</h3>
  </div>
  <div id="stats">
    {#if $contributorsWithPct.length === 0}
      <div id="loading-message">Loading contributors...</div>
    {/if}
	<div id="contributors">
    {#each $contributorsWithPct as c (c.login)}
      {#if c.login && (c.contributions ?? c.total) != null}
        <div class="contributor">
          <img src="{c.avatar_url || c.author?.avatar_url}" alt="{c.login}" width="32" height="32" style="border-radius:50%;margin-right:8px" />
          <a href="{c.html_url || c.author?.html_url}" target="_blank" style="margin-right:6px">
            {c.login}
          </a>
          <span>{c.percent}% ({c.contributions ?? c.total} commit{(c.contributions ?? c.total) !== 1 ? 's' : ''})</span>
        </div>
      {/if}
    {/each}
    <p id="disclaimer" style="margin-top: 1em; font-size: 0.9em; opacity: 0.75;">
      Just a heads up: the commits listed above may not add up to the
      <a href="https://github.com/spacexplorer11/Space_Dodge">total commits</a>
      due to how GitHub tracks contributors — but it's still
      <a href="https://github.com/Spacexplorer11/Space_Dodge/graphs/contributors">super accurate!</a>
    </p>
  </div>
  </div>
</div>
<style>
	/* Contributor styles */
#contributors {
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-top: 1em;
}

#contributors {
    font-size: 5vmin;
    display: flex;
    flex-direction: column;
    justify-content: left;
    margin: 5vmin;
}

.contributor {
    display: flex;
    vertical-align: center;
    align-items: center;
    gap: 2vmin;
    padding: 2vh;
}

.contributor img {
    width: 10vmin;
    height: 10vmin;
}

.contributor a {
    color: white;
    text-decoration-line: underline;
    text-decoration-style: dashed;
    margin-top: 16px;
    margin-bottom: 16px;
}

.contributor span {
    color: white;
    text-decoration-line: underline;
    text-decoration-style: dashed;
    margin-top: 16px;
    margin-bottom: 16px;
}

/* Loading message styles */
#loading-message {
    text-align: center;
    font-size: 1.2em;
    margin-top: 2em;
    color: #888;
    animation: pulse 2s infinite;
}

/* Pulse animation */

@keyframes pulse {
    0% { opacity: 0.5; }
    50% { opacity: 1; }
    100% { opacity: 0.5; }
}
</style>