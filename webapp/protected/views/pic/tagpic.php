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
			<div class='item' style=" height:<?php echo $height;?>px" >
				<a  href="<?php echo Yii::app()->createUrl("Pic/one",array("id"=>$pic['id']));?>" style="position:absolute;width:100%">
					<img src="<?php echo  PIC_THUMB_ROOT.$pic['path'].$pic['file_name'];?>" style=" height:<?php echo $height;?>px" />
					<span><i class="icon-info-sign"></i></span>
				</a>
			</div>
			<?php endforeach; ?>
		</div>
		<!-- end: image grid -->
		<div class="span12"  id="next" >
			<a href="<?php echo Yii::app()->createUrl("Pic/randpage",array("page"=>2));?>"></a>
			<p>↓点击加载更多美女↓</p>
		</div>
	</div>
</div>