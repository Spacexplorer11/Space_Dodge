<script>
	import { Footer, Github_icon, Menu } from "$lib";
	let { children } = $props();
	import { afterNavigate } from '$app/navigation';
	import { onMount } from 'svelte';
	import { menuOpen } from '$lib/stores/menu.js';
	export const prerender = true;

	// Set active marker based on current page
function highlightActiveMenu() {
  const links = document.querySelectorAll("#hamburger-menu a");
  const currentPage = window.location.pathname;

  links.forEach(link => {
    const page = link.getAttribute("href");
    if (page === currentPage) {
      link.classList.add("active-link");
    } else {
      link.classList.remove("active-link");
    }
  });
}

	function updateLayout() {
		const container = document.getElementById('container');
		if (container) {
			container.classList.toggle('active_menu', $menuOpen);
		}
		highlightActiveMenu()
	}

	onMount(() => {
		// Run once on initial load
		updateLayout();

		// Then on every route change
		afterNavigate(() => {
			updateLayout();
		});
	});
</script>

<Menu/>
<Github_icon></Github_icon>
{@render children()}
<Footer></Footer>
