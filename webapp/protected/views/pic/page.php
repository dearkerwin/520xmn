<?php 
	foreach ($pics as  $pic):
		$height = (int)(($pic['height'] /$pic['width']) * 220); 
?>
	<div class='item' style=" height:<?php echo $height;?>px">
		<a  href="<?php echo Yii::app()->createUrl("Pic/one",array("id"=>$pic['id']));?>" >
			<img src="<?php echo  PIC_THUMB_ROOT.$pic['path'].$pic['file_name'];?>" style=" height:<?php echo $height;?>px"  />
			<span><i class="icon-info-sign"></i></span>
		</a>
	</div>
<?php endforeach; ?>