	<header> 	
		<div class="menu-fixed">

			<!--start: Container -->
			<div class="container">

				<!--start: Row -->
				<div class="row">
				
					<a href="<?php echo Yii::app()->createUrl("Pic/index");?>"class="logo"><span>520小美女</span></a>

					<!--start: Navigation -->	
					<div class="navbar navbar-inverse">
			    		<div class="navbar-inner">
			          		<a data-target=".nav-collapse" data-toggle="collapse" class="btn btn-navbar collapsed">
								<span class="icon-reorder"></span>
			          		</a>						
							<div class="nav-collapse collapse">
								<ul class="nav pull-right">
									<li class=""><a href="<?php echo Yii::app()->createUrl("Pic/index");?>" data-target=".nav-collapse" class="anchorLink">Home</a></li>
									<li><a href="<?php echo Yii::app()->createUrl("Pic/tagpic",array("tag"=>"new"));?>" class="anchorLink">最新</a></li>
									<li><a href="<?php echo Yii::app()->createUrl("Pic/tagpic",array("tag"=>"hot"));?>" class="anchorLink">热门</a></li>
								</ul>
							</div>		
						</div>		
					</div><!--end: Navigation -->

				</div><!--end: Row -->
			</div><!--end: Container -->

		</div>

	</header><!--end: Header -->