$(function(){
	initColorboxItem();
	initColorboxPictureNew();
	initColorboxPictureHot();
	initMasonry();
	initInfiniteScroll();
	initScrollup();
	initLazyLoad();


	
	function initMasonry() {
		var $container = $('#masonny-div');
		// $container.imagesLoaded( function(){
			$container.masonry({
				itemSelector : '.item',
				columnWidth : 240,
				isAnimated : true,
				animationOptions: {
					duration: 400
				}
			});
		// });
	}
	

	function initInfiniteScroll() {
		var $container = $('#masonny-div');
		var $sign = $("#masonny-Sign");
		var currentPage = 1;
		var ajaxPath = $("#next a").attr('href');
		ajaxPath = ajaxPath.substring( 0, (ajaxPath.length -1) );
		
		$('#masonny-div').infinitescroll({
		   //#masonny-div 是包括所有文章的div元素id
			navSelector  : "#next",   // 页面分页元素(成功后隐藏)
			nextSelector : "#next a", // 需要点击的下一页链接
			itemSelector : ".item"  , // 返回后文章对应的插入位置
			animate      : true,      //加载完毕是否采用动态效果
			extraScrollPx: 100,      //向下滚动的像素，必须开启动态效果
		    // debug        : true,
		    bufferPx     : 5,
		    loading: {
					finishedMsg: '浑蛋，人家都被你看完了啦. 明天再来吧',
					img:  BASE_PATH + "images/loading-new.gif",
					msgText : "网速不给力,美女马上就来,不要急嘛...",
				},
	    	}, 
		    function( newElements ) {
		        var $newElems = $( newElements );
				$container.masonry( 'appended', $newElems, true ); 
				initColorboxItem();
				currentPage ++;
				push_pv(ajaxPath+currentPage);
				
	    	}
	    );
	}

	

		

	function getItem() {
		var items = $("#display-none").html();
		return items;
	}

	function initColorboxItem() {
		$(".item a").colorbox({ rel: 'group1',transition:"fade" ,width: "80%"});
	}

	function initColorboxPictureNew() {
		$(".picture-new").colorbox({ rel: 'group2',transition:"fade" ,width: "80%"});
	}

	function initColorboxPictureHot() {
		$(".picture-hot").colorbox({ rel: 'group3',transition:"fade" ,width: "80%" });
	}

	function thumbHover() {
		$(".thumbs").mouseover(function(){

		});
	}

	function initScrollup() {
		$.scrollUp({
			scrollName: 'scrollUp',
			scrollImg: true,
			topDistance: '500',
			scrollText: '返回顶部'
		});
	}

	function initLazyLoad() {
		$(".new img").lazyload({
			event : "sporty"
		});
		$(window).bind("load", function() { 
		    var timeout = setTimeout(
		    	function() {
		    		$(".new img").trigger("sporty");
		    	}, 1000
		    );
		});

		$(".rand img").lazyload({
			event : "sporty1"
		});
		$(window).bind("load", function() { 
		    var timeout = setTimeout(
		    	function() {
		    		$(".rand img").trigger("sporty1");
		    	}, 3000
		    );
		});
	}

});

function push_pv(url) {
	if(typeof(_hmt) != 'undefined'){
		console.log(url);
		_hmt.push(['_trackPageview', url]); 
	}
}










