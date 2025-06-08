<script>
	import {base} from '$app/paths';
	import {goto} from "$app/navigation";

	let hovering = $state(false);
	let clicked = $state(false);

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
<div class="demo-button">
	<button class="demo-button" onmouseenter={() => hovering = true} onmouseleave={() => hovering = false}
	        onclick={() => clicked = true} ontransitionend={() => {
    if (clicked) goto(`${base}/about#demo`); // Navigate to demo page after click
  }}>
		<img src="{base}/demo_button_bg.png" alt="button background" class="bg"/>
		<svg class="label" class:clicked={clicked} viewBox="0 0 143 53" fill="none" xmlns="http://www.w3.org/2000/svg">
			<text
					fill="url(#paint1_linear_4_46)"
					xml:space="preserve"
					style="white-space: pre"
					font-family="Space Grotesk"
					font-size="16"
					font-weight="500"
					letter-spacing="0.15px"
			>
      <tspan x="30" y="27.9688">Demo</tspan>
    </text>
			<g id="arrow" class:hovered={hovering}>
				<path
						d="M120.707 23.7071C121.098 23.3166 121.098 22.6834 120.707 22.2929L114.343 15.9289C113.953 15.5384 113.319 15.5384 112.929 15.9289C112.538 16.3195 112.538 16.9526 112.929 17.3431L118.586 23L112.929 28.6569C112.538 29.0474 112.538 29.6805 112.929 30.0711C113.319 30.4616 113.953 30.4616 114.343 30.0711L120.707 23.7071ZM88 23V24H120V23V22H88V23Z"
						fill="#13A094"
				/>
			</g>
			<defs>
				<linearGradient id="paint1_linear_4_46" x1="30" y1="22.5" x2="74" y2="22.5"
				                gradientUnits="userSpaceOnUse">
					<stop stop-color="#13A094" offset="0"/>
					<stop offset="1" stop-color="#188279"/>
				</linearGradient>
			</defs>
		</svg>
	</button>
</div>
<div class="start_button">
	<button class="start_button default_hover" onclick={startGame}>
		<img alt="Space Dodge Start Button"
		     class="start_button"
		     src="{base}/start_button.png">
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

	button.demo-button {
		background: none;
		width: 143px;
		height: 53px;
		overflow: visible;
	}

	#arrow {
		transition: transform 0.3s ease;
	}

	.hovered {
		transform: translateX(8px);
	}

	.clicked {
		transform: translateX(min(52vw, 800px));
		transition: transform 1s ease;
	}

	div.demo-button {
		justify-content: center;
		align-items: center;
		position: relative;
		display: flex;
		flex-direction: column;
		margin-bottom: 2vmin;
		overflow: visible;
	}

	svg {
		overflow: visible;
	}

	.bg {
		display: block;
		width: 100%;
		height: 100%;
		position: relative;
		z-index: 1;
	}

	.label {
		position: absolute;
		top: 3.7px;
		left: 0;
		width: 100%; /* match parent */
		height: 100%;
		z-index: 2; /* higher than the background */
		pointer-events: none; /* optional: lets clicks pass through */
	}

</style>