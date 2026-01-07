
// this file is generated — do not edit it


declare module "svelte/elements" {
	export interface HTMLAttributes<T> {
		'data-sveltekit-keepfocus'?: true | '' | 'off' | undefined | null;
		'data-sveltekit-noscroll'?: true | '' | 'off' | undefined | null;
		'data-sveltekit-preload-code'?:
			| true
			| ''
			| 'eager'
			| 'viewport'
			| 'hover'
			| 'tap'
			| 'off'
			| undefined
			| null;
		'data-sveltekit-preload-data'?: true | '' | 'hover' | 'tap' | 'off' | undefined | null;
		'data-sveltekit-reload'?: true | '' | 'off' | undefined | null;
		'data-sveltekit-replacestate'?: true | '' | 'off' | undefined | null;
	}
}

export {};


declare module "$app/types" {
	export interface AppTypes {
		RouteId(): "/" | "/about" | "/contributors" | "/instructions" | "/mobile_error" | "/privacy_policy";
		RouteParams(): {
			
		};
		LayoutParams(): {
			"/": Record<string, never>;
			"/about": Record<string, never>;
			"/contributors": Record<string, never>;
			"/instructions": Record<string, never>;
			"/mobile_error": Record<string, never>;
			"/privacy_policy": Record<string, never>
		};
		Pathname(): "/" | "/about" | "/about/" | "/contributors" | "/contributors/" | "/instructions" | "/instructions/" | "/mobile_error" | "/mobile_error/" | "/privacy_policy" | "/privacy_policy/";
		ResolvedPathname(): `${"" | `/${string}`}${ReturnType<AppTypes['Pathname']>}`;
		Asset(): "/.DS_Store" | "/.nojekyll" | "/app.css" | "/apple-touch-icon.png" | "/favicon-96x96.png" | "/favicon.ico" | "/favicon.svg" | "/github_icon.webp" | "/red_circle_with_cross.webp" | "/site.webmanifest" | "/start_button.webp" | "/web-app-manifest-192x192.png" | "/web-app-manifest-512x512.png" | string & {};
	}
}