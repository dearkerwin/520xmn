<!--  begin of tagcloud widget -->
<style>
	#tag-cloud{
		height: 280px;
	}
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