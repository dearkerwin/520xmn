<?php
/* @var $this SiteController */
/* @var $error array */

$this->pageTitle=Yii::app()->name . ' - Error';
?>

<style type="text/css">

.error-link img{
	width:100px;
	height: 150px;
	overflow: hidden;
}
.error-container p{
	color: #bbb;
	font-weight: bold;
}

</style>
	<!--start: motion-about -->
	<div id="motion-about" class='error-container'>
		<div class="about-pattern">	
				<!--start: Container -->
		    	<div class="container">
					<a id="about">&nbsp;</a><!--anchorLink: about -->
		    		<!-- start: Row -->
					<div class="row">
						<div class="span6">
							<div class="about-us img-polaroid"> 
								<div class="title">
									<h2><a href='#'>页面找不到 Error <?php echo $code; ?></a></h2>
								</div>
								<div class="clearfix">
									<p>浑蛋，你看哪去了？</p>
									<p> 好脸、好胸、好身材你不看，偏偏来看我的鞋底？？</p>
									<p> 骚年，要不试试这些？？</p>
									<div class="error-link profile">
										<a href="<?php echo Yii::app()->createUrl("Pic/tagpic",array("tag"=>"hot"));?>">
											<img class="img-polaroid" alt="520小美女--热门图片"  title="520小美女--热门图片"  src="<?php echo WEB_ROOT;?>images/hot.jpg">
											<h4>热门图片</h4>
										</a>
									</div>
									<div class="error-link profile">
										<a href="<?php echo Yii::app()->createUrl("Pic/tagpic",array("tag"=>"new"));?>">
											<img class="img-polaroid" alt="520小美女--最新图片"  title="520小美女--最新图片" src="<?php echo WEB_ROOT;?>images/new.jpg">
											<h4>最新图片</h4>
										</a>
									</div>
									<div class="error-link profile">
										<a href="<?php echo Yii::app()->createUrl("Pic/index");?>">
											<img class="img-polaroid" alt="520小美女--返回首页"   title="520小美女--返回首页" src="<?php echo WEB_ROOT;?>images/home.jpg">
											<h4>返回首页</h4>
										</a>
									</div>									
								</div>
							</div>
						</div>	
					</div><!-- end: Row -->
				</div><!-- end: Container -->

		</div><!-- end: team-pattern -->
	</div><!-- end: team -->
