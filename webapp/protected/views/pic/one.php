<style type="text/css">
.one {
	text-align: center;
	margin: 20px 40px;
}
.tag p{
  display: inline-block;
  margin: 10px 5px;
}
</style>

<div class="one" >
	<img src="<?php echo  PIC_ROOT.$pic['path'].$pic['file_name'];?>"  style="height:<?php echo $pic['height'];?>px; width:<?php echo $pic['width'];?>px" />
	<div class="tag"> 
		<p> 标签: </p>
	<?php
		foreach ($pic['Relations']['tag'] as $value) :
			$tag = $value['name'];
	?>
		<p> <a href="<?php echo Yii::app()->createUrl("Pic/tagpic",array("tag"=>$tag));?>"><?php echo $tag;?></a></p>
	<?php 
		endforeach;
	?>
	</div>
</div>
