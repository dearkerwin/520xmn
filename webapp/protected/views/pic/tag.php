<style>
 #tag-cloud{
 	height: 500px;
 	width: 80%;
 }
</style>
<div class="container">
	<div class="row"><!-- 标签云 -->
		<div class="span12" >
			<div id="tag-cloud"></div>
		</div>
		<script>
			var weight = '<?php echo $tags;?>';
			var obj = eval ("(" + weight + ")");
			$(function(){
				$("#tag-cloud").jQCloud(obj); 
			});

		</script>
	</div> <!-- enf: 标签云 -->
</div>