<?php 
	foreach ($pics as  $pic):
		$height = (int)(($pic['height'] /$pic['width']) * 220); 
?>
	<a  class='item' href="<?php echo Yii::app()->createUrl("Pic/one",array("id"=>$pic['id']));?>" style=" height:<?php echo $height;?>px">
		<img src="<?php echo  PIC_THUMB_ROOT.$pic['path'].$pic['file_name'];?>" style=" height:<?php echo $height;?>px"  />
	</a>
<?php endforeach; ?>