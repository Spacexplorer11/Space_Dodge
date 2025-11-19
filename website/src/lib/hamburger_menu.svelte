<script>
	import {menuOpen} from "$lib/stores/menu.js";

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

<button id="hamburger-toggle" on:click={toggleMenu}>☰</button>

<!-- 🍔 Slide-in Menu -->
<div id="hamburger-menu">
	<nav>
		<a href="/">Home</a>
		<a href="/instructions">Instructions</a>
		<a href="/contributors">Contributors</a>
		<a href="/about">About</a>
		<!--  <a href="/stats">Stats</a> -->
		<a href="/privacy_policy">Privacy Policy</a>
	</nav>
</div>