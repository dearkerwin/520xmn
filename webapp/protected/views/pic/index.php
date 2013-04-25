	<!--start: motion-work -->
	<div id="motion-work">
		<div class="work-pattern">		
			<!--start: Container -->
	    	<div class="container">

				<a id="work">&nbsp;</a><!--anchorLink: work -->

				<div class="row"><!-- start: Row 最新 -->

					<div class="span12">	
						<div class="title">
							<h3>最新</h3>
						</div>
					</div>

					<?php 
						foreach ($new_pics as  $pic):
					?>

					<div class="span2 span2-height">	
						<div class="thumbs">
							<a href="<?php echo PIC_ROOT.$pic['file_name'];?>"  class="picture picture-new">
								<img class="img-polaroid" alt="content" src="<?php echo PIC_ROOT.$pic['file_name'];?>">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					</div>

					<?php
						endforeach;
					?>
<!-- 
					<div class="span2 span2-height">	
						<div class="thumbs">
							<a href="1 (2).jpg" class="picture picture-new">
								<img class="img-polaroid" alt="content" src="./img/medium/1_2.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					</div>


					<div class="span2 span2-height">	

						<div class="thumbs">
							<a href="1 (17).jpg" class="picture  picture-new">
								<img class="img-polaroid" alt="content" src="./img/medium/1_17.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					</div>

					<div class="span2 span2-height">	

						<div class="thumbs">
							<a href="1 (4).jpg" class="picture  picture-new">
								<img class="img-polaroid" alt="content" src="./img/medium/1_4.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					</div>

					<div class="span2 span2-height">	
						<div class="thumbs">
							<a href="1 (5).jpg" class="picture  picture-new">
								<img class="img-polaroid" alt="content" src="./img/medium/1_5.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					</div>

					<div class="span2 span2-height">	
						<div class="thumbs">
							<a href="1 (6).jpg" class="picture  picture-new">
								<img class="img-polaroid" alt="content" src="./img/medium/1_6.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					</div>


					<div class="span2 span2-height">	

						<div class="thumbs">
							<a href="1 (7).jpg" class="picture  picture-new">
								<img class="img-polaroid" alt="content" src="./img/medium/1_7.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					

						
					</div>

					<div class="span2 span2-height">	

						<div class="thumbs">
							<a href="1 (8).jpg" class="picture  picture-new">
								<img class="img-polaroid" alt="content" src="./img/medium/1_8.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					

						
						
					</div>

					<div class="span2 span2-height">	

						<div class="thumbs">
							<a href="1 (18).jpg" class="picture  picture-new">
								<img class="img-polaroid" alt="content" src="./img/medium/1_18.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					

						
						
					</div>


					<div class="span2 span2-height">	

						<div class="thumbs">
							<a href="1 (9).jpg" class="picture  picture-new">
								<img class="img-polaroid" alt="content" src="./img/medium/1_9.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					

						

					</div>

					<div class="span2 span2-height">	

						<div class="thumbs">
							<a href="1 (10).jpg" class="picture  picture-new">
								<img class="img-polaroid" alt="content" src="./img/medium/1_10.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>				
					</div>


					<div class="span2 span2-height">	

						<div class="thumbs">
							<a href="1 (11).jpg" class="picture  picture-new">
								<img class="img-polaroid" alt="content" src="./img/medium/1_11.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					</div> -->

				</div><!-- end: Row -->

				
				<div class="row"><!-- start: Row 热门 -->

					<div class="span12">	
						<div class="title">
							<h3>热门</h3>
						</div>
					</div>

					<div class="span3 span3-height">	
						<div class="thumbs">
							<a href="./pic.html"  class="picture picture-hot">
								<img class="img-polaroid" alt="content" src="./img/medium/1_9.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					</div>

					<div class="span3 span3-height">	
						<div class="thumbs">
							<a href="1 (2).jpg" class="picture picture-hot">
								<img class="img-polaroid" alt="content" src="./img/medium/1_2.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					</div>


					<div class="span3 span3-height">	

						<div class="thumbs">
							<a href="1 (17).jpg" class="picture  picture-hot">
								<img class="img-polaroid" alt="content" src="./img/medium/1_17.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					</div>

					<div class="span3 span3-height">	

						<div class="thumbs">
							<a href="1 (4).jpg" class="picture  picture-hot">
								<img class="img-polaroid" alt="content" src="./img/medium/1_4.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					</div>

					<div class="span3 span3-height">	
						<div class="thumbs">
							<a href="1 (5).jpg" class="picture  picture-hot">
								<img class="img-polaroid" alt="content" src="./img/medium/1_5.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					</div>

					<div class="span3 span3-height">	
						<div class="thumbs">
							<a href="1 (6).jpg" class="picture  picture-hot">
								<img class="img-polaroid" alt="content" src="./img/medium/1_6.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					</div>


					<div class="span3 span3-height">	

						<div class="thumbs">
							<a href="1 (7).jpg" class="picture  picture-hot">
								<img class="img-polaroid" alt="content" src="./img/medium/1_7.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					

						
					</div>

					<div class="span3 span3-height">	

						<div class="thumbs">
							<a href="1 (8).jpg" class="picture  picture-hot">
								<img class="img-polaroid" alt="content" src="./img/medium/1_8.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					

						
						
					</div>

					<div class="span3 span3-height" >	

						<div class="thumbs">
							<a href="1 (18).jpg" class="picture  picture-hot">
								<img class="img-polaroid" alt="content" src="./img/medium/1_18.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					

						
						
					</div>


					<div class="span3 span3-height">	

						<div class="thumbs">
							<a href="1 (9).jpg" class="picture  picture-hot">
								<img class="img-polaroid" alt="content" src="./img/medium/1_9.jpg">
								<span><i class="icon-info-sign"></i></span>
							</a>
						</div>
					

						

					</div>

					<div class="span12">

						<div class="arrow-down">
			   				 	<a class="anchorLink" href="http://wbpreview.com/previews/WB001304D/#contact"><i class="icon-circle-arrow-down"></i></a>
						</div>

					</div>

				</div><!-- end: Row -->

			</div><!-- end: Container -->
		</div><!-- end: work-pattern -->
	</div><!--end: work -->




    	
	<!--start: image grid -->
	<div id="masonny-div" >
			 
			<a  class='item' href="./img/medium/1_2.jpg"><img src="./img/medium/1_2.jpg"/></a>
			<a  class='item' href="./img/medium/1_3.jpg"><img src="./img/medium/1_3.jpg"/></a>
			<a  class='item' href="./img/medium/1_4.jpg"><img src="./img/medium/1_4.jpg"/></a>
			<a  class='item' href="./img/medium/1_5.jpg"><img src="./img/medium/1_5.jpg"/></a>
			<a  class='item' href="./img/medium/1_6.jpg"><img src="./img/medium/1_6.jpg"/></a>
			<a  class='item' href="./img/medium/1_7.jpg"><img src="./img/medium/1_7.jpg"/></a>
			<a  class='item' href="./img/medium/1_8.jpg"><img src="./img/medium/1_8.jpg"/></a> 
			<a  class='item' href="./img/medium/1_9.jpg"><img src="./img/medium/1_9.jpg"/></a>
			<a  class='item' href="./img/medium/1_10.jpg"><img src="./img/medium/1_10.jpg"/></a>
			<a  class='item' href="./img/medium/1_11.jpg"><img src="./img/medium/1_11.jpg"/></a>
			<a  class='item' href="./img/medium/1_12.jpg"><img src="./img/medium/1_12.jpg"/></a>
			<a  class='item' href="./img/medium/1_13.jpg"><img src="./img/medium/1_13.jpg"/></a>
			<a  class='item' href="./img/medium/1_14.jpg"><img src="./img/medium/1_14.jpg"/></a>
			<a  class='item' href="./img/medium/1_15.jpg"><img src="./img/medium/1_15.jpg"/></a>
			<a  class='item' href="./img/medium/1_16.jpg"><img src="./img/medium/1_16.jpg"/></a>
			<a  class='item' href="./img/medium/1_17.jpg"><img src="./img/medium/1_17.jpg"/></a>
			<a  class='item' href="./img/medium/1_18.jpg"><img src="./img/medium/1_18.jpg"/></a>
			<a  class='item' href="./img/medium/1_19.jpg"><img src="./img/medium/1_19.jpg"/></a>
			<a  class='item' href="./img/medium/1_20.jpg"><img src="./img/medium/1_20.jpg"/></a>
			<a  class='item' href="./img/medium/1_21.jpg"><img src="./img/medium/1_21.jpg"/></a>
			<a  class='item' href="./img/medium/1_22.jpg"><img src="./img/medium/1_22.jpg"/></a>
			<a  class='item' href="./img/medium/1_23.jpg"><img src="./img/medium/1_23.jpg"/></a>
			<a  class='item' href="./img/medium/1_24.jpg"><img src="./img/medium/1_24.jpg"/></a>
			<a  class='item' href="./img/medium/1_25.jpg"><img src="./img/medium/1_25.jpg"/></a>
			<a  class='item' href="./img/medium/1_26.jpg"><img src="./img/medium/1_26.jpg"/></a>
	</div>
	<!-- end: image grid -->
	<div id="next" ><a href="./2.html">下一页</a></div>

