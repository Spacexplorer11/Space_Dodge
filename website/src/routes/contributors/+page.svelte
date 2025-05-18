<script>
  import { contributorsWithPct } from '$lib/stores/repo_data.js';
</script>
<div id="container">
<div id="header">
	  <h1>Contributors</h1>
	  <h2>Space Dodge is a collaborative project.</h2>
	  <h2>This page is to thank our contributors!</h2>
	  <h3>Contributors:</h3>
  </div>
  <div id="stats">
    {#if $contributorsWithPct.length === 0}
      <div id="loading-message">Loading contributors...</div>
    {/if}
	<div id="contributors">
    {#each $contributorsWithPct as c (c.login)}
      {#if c.login && (c.contributions ?? c.total) != null}
        <div class="contributor">
          <img src="{c.avatar_url || c.author?.avatar_url}" alt="{c.login}" width="32" height="32" style="border-radius:50%;margin-right:8px" />
          <a href="{c.html_url || c.author?.html_url}" target="_blank" style="margin-right:6px">
            {c.login}
          </a>
          <span>{c.percent}% ({c.contributions ?? c.total} commit{(c.contributions ?? c.total) !== 1 ? 's' : ''})</span>
        </div>
      {/if}
    {/each}
    <p id="disclaimer" style="margin-top: 1em; font-size: 0.9em; opacity: 0.75;">
      Just a heads up: the commits listed above may not add up to the
      <a href="https://github.com/spacexplorer11/Space_Dodge">total commits</a>
      due to how GitHub tracks contributors — but it's still
      <a href="https://github.com/Spacexplorer11/Space_Dodge/graphs/contributors">super accurate!</a>
    </p>
  </div>
  </div>
</div>