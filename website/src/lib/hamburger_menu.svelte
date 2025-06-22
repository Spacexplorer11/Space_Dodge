<script>
	import {menuOpen} from "$lib/stores/menu.js";
	import {base} from '$app/paths';

	function toggleMenu() {
		const menu = document.getElementById("hamburger-menu");
		const container = document.getElementById("container");


		const menuIsActive = menu.classList.contains("active");
		const containerIsActive = container.classList.contains("active_menu");

		if (menuIsActive && !containerIsActive) {
			container.classList.toggle("active_menu");
		} else if (!menuIsActive && containerIsActive) {
			menu.classList.toggle("active");
		} else {
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

<button id="hamburger-toggle" class="default_hover" onclick={toggleMenu}>☰</button>

<!-- 🍔 Slide-in Menu -->
<div id="hamburger-menu">
	<nav>
		<a href="{base}/">Home</a>
		<a href="{base}/instructions">Instructions</a>
		<a href="{base}/contributors">Contributors</a>
		<a href="{base}/about">About</a>
		<!--  <a href="/stats">Stats</a> -->
		<a href="{base}/privacy_policy">Privacy Policy</a>
	</nav>
</div>