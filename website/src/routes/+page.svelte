<script>
	import {goto} from "$app/navigation";

	// Array of desktop and mobile OS types
	const Desktop = [
		"Windows",
		"macOS",
		"Linux"
	]
	const Mobile = [
		"Android",
		"iOS"
	]

	// Function to get the device information
	function getDeviceInfo() {
		const ua = navigator.userAgent;

		if (/android/i.test(ua)) return "Android";
		if (/iPad|iPhone|iPod/.test(ua) && !window.MSStream) return "iOS";
		if (/Macintosh/.test(ua)) return "macOS";
		if (/Windows/.test(ua)) return "Windows";
		if (/Linux/.test(ua)) return "Linux";

		return "Unknown OS";
	}

	// Navigates to game instructions or error page based on device
	function startGame() {
		const device = getDeviceInfo();
		if (Desktop.includes(device)) {
			goto(`/instructions`);
		} else if (Mobile.includes(device)) {
			goto(`/mobile_error`);
		} else {
			alert("Your OS is not supported.");
			goto(`/mobile_error`);
		}
	}
</script>
<div id="header">
	<h1>Space Dodge</h1>
	<h2>by <a href="https://github.com/spacexplorer11">Akaalroop Singh</a>. <br><br></h2>
</div>
<div id="content">
	<p>Welcome to Space Dodge!</p>
	<p>This is a simple game where you dodge bullets in space. </p>
	<p>It can only be played on a computer using a keyboard, <em>Windows, MacOS & Linux</em> are supported
	</p>
</div>
<div class="start_button">
	<button class="start_button" on:click={startGame}>
		<img alt="Space Dodge Start Button"
		     class="start_button"
		     src="/start_button.webp">
	</button>
</div>
<style>
	/* Start button styles */
	.start_button {
		display: flex;
		width: 50vmin;
		height: 40vmin;
		margin: 0 auto;
		justify-content: center;
		align-items: center;
		border: none;
		cursor: pointer;
		transition: transform 0.3s, box-shadow 0.3s;
		box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
	}

	.start_button:hover {
		transform: scale(1.02) translateY(-3px);
		box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
	}
</style>