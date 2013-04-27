	<!--start: image grid -->
	<div id="masonny-div" >
			 <?php foreach ($pics as  $pic): ?>
			<a  class='item' href="<?php echo Yii::app()->createUrl("Pic/one",array("id"=>$pic['id']));?>"><img src="<?php echo PIC_ROOT.$pic['file_name'];?>"/></a>
			<?php endforeach; ?>
	</div>
	<!-- end: image grid -->
	<div id="next" ><a href="<?php echo Yii::app()->createUrl("Pic/tagpage",array("tag"=>$tag,"page"=>2));?>">下一页</a></div>