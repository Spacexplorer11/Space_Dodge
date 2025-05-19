<script>
	import { goto } from "$app/navigation";
		import { base } from "$app/paths";
	import { onMount } from "svelte";

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
	function checkMobile() {
    const device = getDeviceInfo();
	if (Mobile.includes(device)) {
        goto(`${base}/mobile_error`);
    } else if (!Desktop.includes(device)) {
        alert("Your OS is not supported.");
        goto(`${base}/mobile_error`);
    }
}

onMount (() => {
checkMobile()
	});
</script>
<div id="container">
<div id="header">
	<h1>Instructions to install</h1>
	<h2>Have fun in just seven steps!</h2>
</div>
	<div id="content">
		<ol>
			<li>Download Python 3.13 or later from the official website: <a href="https://www.python.org/downloads/">Python
				Downloads</a>.<br>
				(If you are on windows, click to open <a href="https://www.microsoft.com/en-us/p/python-3/9p3sx8s0c0r4">Python
					3 on Microsoft Store</a> as well as downloading from the website)
			</li>
			<li>Install Python by running the downloaded installer. Make sure to check the box that says "Add Python to
				PATH" during installation.
			</li>
			<li><a href="https://github.com/spacexplorer11/Space_Dodge/releases/latest/download/Space_Dodge.zip" download>
  Download the latest version of the game
</a>
			</li>
			<li>Extract/Unzip the file you downloaded.</li>
			<li>Open the extracted folder and find the file named <code>main.py</code>. <em>The path is <code>space_dodge/main.py</code></em></li>
			<li>Right click and run the file with Python Launcher (MacOS) or Python 3.13 (Windows/Linux).</li>
			<li>Have fun!</li>
		</ol>
	</div>
</div>