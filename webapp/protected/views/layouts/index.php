<!DOCTYPE html>
<html lang="en" class="no-js">
    <head>
	    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<style type="text/css">
			@media print {   .gmnoprint {    display:none  }}
			@media screen {  .gmnoscreen {    display:none  }}
		</style>

		<!-- start: Meta -->
		<meta charset="utf-8">
		<title>Motion - Single Page Responsive portofolio at Bootstrap </title> 
		<meta content="Single Page Responsive portofolio at Bootstrap" name="description">
		<meta content="dark, responsive, portofolio, single page" name="keywords">
		<!-- end: Meta -->
		
		<!-- start: Mobile Specific -->
		<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
		<!-- end: Mobile Specific -->

	    <!-- start: CSS -->
	    <link rel="stylesheet" href="<?php echo Yii::app()->request->baseUrl; ?>/css/bootstrap.css">
	    <link rel="stylesheet" href="<?php echo Yii::app()->request->baseUrl; ?>/css/bootstrap-responsive.css">
	    <link rel="stylesheet" href="<?php echo Yii::app()->request->baseUrl; ?>/css/font-awesome.css">
	    <link rel="stylesheet" href="<?php echo Yii::app()->request->baseUrl; ?>/css/style.css">
<!-- 	    <link rel="stylesheet" href="<?php echo Yii::app()->request->baseUrl; ?>/css/jqcloud.css"> -->
	    <link media="screen" rel="stylesheet" href="<?php echo Yii::app()->request->baseUrl; ?>/css/colorbox.css" />
	    <script type="text/javascript" src="<?php echo Yii::app()->request->baseUrl; ?>/js/jquery-1.7.1.min.js"></script>
		<!-- end: CSS -->

	    <!--[if IE 9]>
			<style>.social {display:none;}.navbar .nav > li > .connect {display:none;}</style>
		<![endif]-->    
	    <!--[if IE 8]>
			<style>.ch-grid {float: left;}.ch-grid li {float: left;margin-left:100px;}.about-pattern {background-position: center;background-repeat: repeat-x;border:none;}</style>
		<![endif]-->
    </head>
    <body>
    	<a id="home"></a><!--anchorLink: home -->	
    	<?php echo $this->renderPartial('/layouts/header'); ?> 
    	

	
		<?php echo $content;?>  

		<?php echo $this->renderPartial('/layouts/footer'); ?>  

		
	  	<script type="text/javascript" src="<?php echo Yii::app()->request->baseUrl; ?>/js/bootstrap.min.js"></script>
		<script type="text/javascript" src="<?php echo Yii::app()->request->baseUrl; ?>/js/jquery.masonry.min.js"></script>
		<script type="text/javascript" src="<?php echo Yii::app()->request->baseUrl; ?>/js/jquery.colorbox.js"></script>
		<script type="text/javascript" src="<?php echo Yii::app()->request->baseUrl; ?>/js/jquery.infinitescroll.min.js"></script>
		<script type="text/javascript" src="<?php echo Yii::app()->request->baseUrl; ?>/js/masonry.js"></script>
		<script type="text/javascript" src="<?php echo Yii::app()->request->baseUrl; ?>/js/jqcloud-1.0.3.min.js"></script>
    </body>
</html>