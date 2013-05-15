<?php foreach ($pics as  $pic): ?>
<a  class='item' href="<?php echo Yii::app()->createUrl("Pic/one",array("id"=>$pic['id']));?>"><img src="<?php echo  PIC_THUMB_ROOT.$pic['path'].$pic['file_name'];?>"/></a>
<?php endforeach; ?>