<script>
	import { Footer, Github_icon, Menu } from "$lib";
	let { children } = $props();
	import { afterNavigate } from '$app/navigation';
	import { onMount } from 'svelte';
	import { menuOpen } from '$lib/stores/menu.js';
	import Particles, { particlesInit } from '@tsparticles/svelte';
    import { loadSlim } from '@tsparticles/slim';

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

    let particlesConfig = {
        particles: {
            color: {
                value: '#cccccc'
            },
            links: {
                enable: true,
                color: '#cccccc'
            },
            move: {
                enable: true
            },
            number: {
                value: 50
            }
        }
    };

    let onParticlesLoaded = (event) => {
        const particlesContainer = event.detail.particles;

        // you can use particlesContainer to call all the Container class
        // (from the core library) methods like play, pause, refresh, start, stop
    };

    void particlesInit(async (engine) => {
        // call this once per app
        // you can use main to customize the tsParticles instance adding presets or custom shapes
        // this loads the tsparticles package bundle, it's the easiest method for getting everything ready
        // starting from v2 you can add only the features you need reducing the bundle size
        //await loadFull(engine);
        await loadSlim(engine);
    });
</script>

<Menu/>
<Github_icon></Github_icon>
{@render children()}
<Particles
	id="tsparticles"
	class="container"
	style="z-index: -1; position: fixed; top: 0; left: 0; width: 100%; height: 100%"
	options="{particlesConfig}"
	on:particlesLoaded="{onParticlesLoaded}"
/>
<Footer></Footer>
