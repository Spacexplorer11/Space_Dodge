<script>
	import {menuOpen} from "$lib/stores/menu.js";
	import {base} from '$app/paths';

	function toggleMenu() {
		const menu = document.getElementById("hamburger-menu");
		const container = document.getElementById("container");


		switch (menu, container) {
			case (menu.classList.contains("active") && !container.classList.contains("active_menu")):
				container.classList.toggle("active_menu");
				break;
			case (!menu.classList.contains("active") && container.classList.contains("active_menu")):
				menu.classList.toggle("active");
				break;
			default:
			case ((menu.classList.contains("active") && container.classList.contains("active_menu")) || (!menu.classList.contains("active") && !container.classList.contains("active_menu"))) :
				menu.classList.toggle("active");
				container.classList.toggle("active_menu");
		}
		if (menu.classList.contains("active")) {
			menuOpen.set(true);
		} else if (!menu.classList.contains("active")) {
			menuOpen.set(false);
			if (container.classList.contains("active_menu")) {
				container.classList.toggle("active_menu");
			}
		}
	}
</script>

<button id="hamburger-toggle" on:click={toggleMenu}>☰</button>

<!-- 🍔 Slide-in Menu -->
<div id="hamburger-menu">
	<nav>
		<a href="{base}/">Home</a>
		<a href="{base}/instructions">Instructions</a>
		<a href="{base}/contributors">Contributors</a>
		<!--  <a href="/stats">Stats</a> -->
		<!--  <a href="/about">About</a> -->
		<a href="{base}/privacy_policy">Privacy Policy</a>
	</nav>
</div>