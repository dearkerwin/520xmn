
<?php echo $content;?>
<script type="text/javascript">
	var currentUrl = '<?php echo Yii::app()->request->getUrl();?>';
	if(typeof(_hmt) != 'undefined'){
		_hmt.push(['_trackPageview', currentUrl]); 
	}
</script>
