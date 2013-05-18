<div class="container">
	<?php 
		$this->widget('application.widgets.TagCloudWidget'); 
	?>
</div>

<div class="container">
	<div class="row">
		<div class="span12">	
			<div class="title">
				<h3>
					<a href="#"><?php echo $tag_name;?></a> 
					<?php if($pic_count != 0) :?>

						<span style="font-size:16px">(<?php echo $pic_count;?>张图片)</span>

					<?php endif;?>
				</h3>
			</div>
		</div>
		<!-- <div class="span12"> -->
			<!--start: image grid -->
			
		<!-- </div> -->
	</div>
</div>

<div class="container">
	<div class="row">
		<div id="masonny-div" >
			<?php 
				foreach ($pics as  $pic): 
					$height = (int)(($pic['height'] /$pic['width']) * 220);
			?>
				<a  class='item' href="<?php echo Yii::app()->createUrl("Pic/one",array("id"=>$pic['id']));?>">
					<img src="<?php echo  PIC_THUMB_ROOT.$pic['path'].$pic['file_name'];?>" style=" height:<?php echo $height;?>px" />
				</a>
			<?php endforeach; ?>
		</div>
		<!-- end: image grid -->
		<div id="next" ><a href="<?php echo Yii::app()->createUrl("Pic/tagpage",array("tag"=>$tag,"page"=>2));?>">下一页</a></div>
	</div>
</div>