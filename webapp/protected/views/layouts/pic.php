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
	    <link media="screen" rel="stylesheet" href="<?php echo Yii::app()->request->baseUrl; ?>/css/colorbox.css" />
		<!-- end: CSS -->

	    <!--[if IE 9]>
			<style>.social {display:none;}.navbar .nav > li > .connect {display:none;}</style>
		<![endif]-->    
	    <!--[if IE 8]>
			<style>.ch-grid {float: left;}.ch-grid li {float: left;margin-left:100px;}.about-pattern {background-position: center;background-repeat: repeat-x;border:none;}</style>
		<![endif]-->
		<style type="text/css">
			.item {
			  width: 220px;
			  margin: 10px;
			  float: left;
			}
			#masonny-div{
				width: 95%;
			}
		</style>
    </head>
    <body>
    	<?php echo $content;?>  
    </body>
</html>