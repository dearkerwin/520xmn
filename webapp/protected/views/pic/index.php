
	<!--start: motion-work -->
	<div id="motion-work">
		<div class="work-pattern">		
			<!--start: Container -->
	    	<div class="container">


	    		<div class="row new"><!-- start: Row 最新 -->
					<div class="span12">	
						<div class="title">
							<!-- <h3>最新</h3> -->
							<h3><a href="<?php echo Yii::app()->createUrl("Pic/tagpic",array("tag"=>"new"));?>"> 最新  <span class="more"> 更多>></span> </a></h3>
						</div>
					</div>

					<?php foreach ($new_pics as  $pic): ?>
					<div class="span2 span2-height">	
						<div class="thumbs">
							<a href="<?php echo Yii::app()->createUrl("Pic/one",array("id"=>$pic['id']));?>"  class="picture picture-new">
								<img class="img-polaroid" alt="美女 图片 520xmn"  src="<?php echo  PIC_THUMB_ROOT.$pic['path'].$pic['file_name'];?>">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					</div>
					<?php endforeach; ?>
				</div><!-- end: Row 最新 -->


				<div class="row hot"><!-- start: Row 热门 -->
					<div class="span12">	
						<div class="title">
							<h3><a href="<?php echo Yii::app()->createUrl("Pic/tagpic",array("tag"=>"hot"));?>"> 热门 <span class="more"> 更多>></span> </a></h3>
						</div>
					</div>

					<?php foreach ($hot_pics as  $pic): ?>
					<div class="span3 span3-height">	
						<div class="thumbs">
							<a href="<?php echo Yii::app()->createUrl("Pic/one",array("id"=>$pic['id']));?>"  class="picture picture-hot">
								<img class="img-polaroid" alt="美女 图片 520xmn"   src="<?php echo WEB_ROOT;?>images/loazload.gif" data-original="<?php echo PIC_THUMB_ROOT.$pic['path'].$pic['file_name'];?>">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					</div>
					<?php endforeach; ?>
				</div><!-- end: Row  热门-->


				

				<div class="row" id='tag'><!-- start: 标签 -->
					<div class="span12">	
						<div class="title">
							<h3><a href="#"> 标签  </a></h3>
						</div>
					</div>
					<?php 
						$this->widget('application.widgets.TagCloudWidget'); 
					?>	
				</div><!-- end: Row 标签 -->
				
				
				<!-- <div class="span12">
					<div class="arrow-down">
		   				 <i class="icon-circle-arrow-down"></i>
					</div>
				</div> -->
				
			</div><!-- end: Container -->
		</div><!-- end: work-pattern -->
	</div><!--end: work -->
    	
    <div class="container">
    	<div class="row">
    		<div class="span12">	
				<div class="title">
					<h3><a href="<?php echo Yii::app()->createUrl("Pic/tagpic",array("tag"=>"rand"));?>"> 随机一下 <span class="more"> 更多>></span> </a></h3>
				</div>
			</div>
    	</div>
		<div class="row">
			<!--start: image grid -->
			<div id="masonny-div" class="rand">
				<?php 
					foreach ($rand_pics as  $pic): 
						$height = (int)(($pic['height'] /$pic['width']) * 220);
				?>
				<div class='item' style=" height:<?php echo $height;?>px">
					<a  href="<?php echo Yii::app()->createUrl("Pic/one",array("id"=>$pic['id']));?>"  style="position:absolute; width:100%">
						<img  data-original="<?php echo  PIC_THUMB_ROOT.$pic['path'].$pic['file_name'];?>" style=" height:<?php echo $height;?>px" alt=" 520小美女 图片 加载中.."  />
						<span><i class="icon-info-sign"></i></span>
					</a>
				</div>
				<?php endforeach; ?>
			</div>
			<!-- end: image grid -->
			<div class="span12"  id="next" >
				<a href="<?php echo Yii::app()->createUrl("Pic/randpage",array("page"=>2));?>"></a>
				<p>↓加载更多美女↓</p>
			</div>
		</div>
	</div>
