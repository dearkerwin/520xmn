$(function(){
	initItem();
	initPictureNew();
	// initScroll();
	initInfiniteScroll();
	var $container = $('#masonny-div');
	$container.masonry({
		// options
		itemSelector : '.item',
		columnWidth : 240,
		isAnimated : true,
		animationOptions: {
			duration: 400
		}
	});
	$container.imagesLoaded( function(){
		$container.masonry({
			itemSelector : '.item'
		});
	});

	function initInfiniteScroll() {
		$('#masonny-div').infinitescroll({
		   //#masonny-div 是包括所有文章的div元素id
			navSelector  : "#next",
			             // 页面分页元素(成功后隐藏)
			nextSelector : "#next a",
			             // 需要点击的下一页链接
			itemSelector : ".item"   ,
			             // 返回后文章对应的插入位置
			loadingImg    : "images/loading-new.gif",
			             //加载图片路径（绝对路径）
			loadingText	  : "加载中...",
			           //显示的提示文字
			// animate      : true,
			           //加载完毕是否采用动态效果
			extraScrollPx: 150,
			          //向下滚动的像素，必须开启动态效果
			// donetext       : "后面没有了" ,
			        //返回404，即到头了显示的文字
		    // debug        : true,  
		    loading: {
				finishedMsg: 'No more pages to load.',
				img: "images/loading-new.gif"
				}
      
	    	}, 
		    function( newElements ) {
		        // hide new items while they are loading
		        var $newElems = $( newElements ).css({ opacity: 0 });
		        // ensure that images load before adding to masonry layout
		        $newElems.imagesLoaded(function(){
					// show elems now they're ready
					$newElems.animate({ opacity: 1 });
					$container.masonry( 'appended', $newElems, true ); 
					initItem();
		    	});

	    	}
	    );
	}

	function initScroll() {
		var ajaxUrl = "pic.html";
		$(window).scroll(function(){
			var clientHeight = window.screen.height  ;
			var $masonrySign = $("#masonny-Sign");
			var signHeight = $masonrySign.offset().top;

			if(clientHeight + $(window).scrollTop() >= signHeight + 100	){
				if( $masonrySign.attr("sign") == 0 ) {
					//开始加载
					console.log("load");
					$masonrySign.attr("sign",1);
					$.ajax({
						url:ajaxUrl,
						type: "GET",
						success:function(data){
							$masonrySign.attr("sign",0);
							console.log("success");
						},
						error: function(){
							alert("error");
							$masonrySign.attr("sign",0);
						}
					});
				} else {
					//已经再加载，忽略
					console.log("busy");
				}
				// alert(clientHeight + $(window).scrollTop());
				// $newElems = $(getItem());
		  //       $container.append($newElems).masonry( 'appended', $newElems, true ); 
		  //       initItem();
			}
		});
	}

	// function 

	

	function getItem() {
		var items = $("#display-none").html();
		return items;
	}

	function initItem() {
		$(".item").colorbox({ rel: 'group1' ,transition:"fade"});
	}

	function initPictureNew() {
		$(".picture-new").colorbox({ rel: 'group2' ,transition:"fade" });
	}

	function initPictureHot() {
		$(".picture-hot").colorbox({ rel: 'group3',transition:"fade" });
	}

	function thumbHover() {
		$(".thumbs").mouseover(function(){

		});
	}

});










