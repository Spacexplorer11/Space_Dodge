<script>
	import { base } from '$app/paths';
	import { goto } from "$app/navigation";
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
        goto(`${base}/instructions`);
    } else if (Mobile.includes(device)) {
        goto(`${base}/mobile_error`);
    } else {
        alert("Your OS is not supported.");
        goto(`${base}/mobile_error`);
    }
}
</script>
<div id="container">
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
			     src="https://github.com/Spacexplorer11/Space_Dodge/blob/main/space_dodge/assets/start_button.png?raw=true">
		</button>
	</div>
</div>