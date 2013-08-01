<!--  begin of tagcloud widget -->
<style>
@media (min-width: 768px) and (max-width: 979px) {#tag-cloud{height: 280px;}}
@media (max-width: 767px) 						{#tag-cloud{height: 450px;}}
@media (min-width: 1200px) 						{#tag-cloud{height: 280px;}}
</style>
<div id="tag-cloud"></div>
<script>
	var weight = '<?php echo $tags;?>';
	var obj = eval ("(" + weight + ")");
	$(function(){
		$("#tag-cloud").jQCloud(obj); 
	});
</script>
<!--  end of tagcloud widget -->