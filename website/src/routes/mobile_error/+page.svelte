<script>
	import {base} from "$app/paths";
</script>
<div id="warning_header">
	<div id="header">
		<h1> Unavailable on your device</h1>
	</div>
	<h2>Space Dodge is <b>not available</b> on mobile devices.</h2>
	<h3>Please open this page on a computer<br><br><br></h3>
	<img alt="Warning Symbol - red circle with line through it" id="warning_symbol"
	     src="{base}/red_circle_with_cross.webp">
</div>
<style>
	/* Warning header styles */
	#warning_header {
		color: red;
		text-align: center;
		font-size: xx-large;
		padding-left: 2px;
	}

	/* Warning symbol styles */
	#warning_symbol {
		width: 80vw;
		height: 50vh;
	}
</style>