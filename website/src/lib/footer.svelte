<script>
	import {base} from '$app/paths';
</script>
<div id="footer">
	<p id="footer_text">© 2025 <a href="https://github.com/spacexplorer11">Akaalroop Singh (Spacexplorer11)</a>. <br>
		Space Dodge is licensed under the <a href="https://www.gnu.org/licenses/agpl-3.0.html">GNU AGPL v3.0</a>.
		You can read our privacy policy <a href="{base}/privacy_policy">here</a></p>
</div>
<style>
	/* Footer styles */
	#footer {
		background: teal;
		padding: 5px;
		text-align: center;
		margin-top: auto;
		z-index: 1000;
		position: relative;
	}

	#footer_text {
		color: black;
	}

	#footer a {
		color: white;
	}
</style>