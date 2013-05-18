<?php

class PicController extends Controller
{
	public $layout = 'index';
	private $allow_page = 10; //允许加载的页面数量
	public function actionIndex()
	{
		$this->render('index',array(
				'new_pics' => Pic::model()->getNewPic(1,12, "height > width"),
				// 'new_pics' => Term::model()->getTagPic("小清新",1,12),
				'hot_pics' => Pic::model()->getHotPic(1,8, "height > width"),
				'rand_pics' => Pic::model()->getRandPic(),

			));
	}

	public function actionTag() {
		$tag_count = Term::model()->getTagCount();
		foreach ($tag_count as $key => $value) {
			$link = Yii::app()->createUrl("Pic/tagpic",array("tag"=>$key));
			$tag = array('text'=> $key, 'weight'=> $value, 'link' =>$link  );
			$tags[] = $tag;
		}
		$this->render('tag',array(
			'tags' => json_encode($tags)
		));
	}


	// Uncomment the following methods and override them if needed
	/*
	public function filters()
	{
		// return the filter configuration for this controller, e.g.:
		return array(
			'inlineFilterName',
			array(
				'class'=>'path.to.FilterClass',
				'propertyName'=>'propertyValue',
			),
		);
	}

	public function actions()
	{
		// return external action classes, e.g.:
		return array(
			'action1'=>'path.to.ActionClass',
			'action2'=>array(
				'class'=>'path.to.AnotherActionClass',
				'propertyName'=>'propertyValue',
			),
		);
	}
	*/

	/**
	 * 获取一张图片
	 */
	public function actionOne( $id ) {
		$id = decodeId($id);
		$this->layout = "ajax";
		$pic = Pic::model()->getOnePic($id);
		if( !empty($pic) ) {
			Pic::model()->increasePicView($id);
		} else {
			exit(" this picture is not exist !");
		}
		$this->render('one',array(
			'pic' => $pic[0]
		));
	}

	/** 
	 * 随机翻页
	 */
	public function actionRandpage($page) {
		if( $page > $this->allow_page ) return ;
		$this->layout = "ajax";
		$this->render('page',array(
			'pics' => Pic::model()->getRandPic()
		));
	}

	/**
	 * 标签\最新\热门 页面
	 */
	public function actionTagpic($tag) {
		$tag = urldecode($tag);
		$pics = array();
		$tag_name = $tag;
		if( $tag == "new") {
			$pics = Pic::model()->getNewPic();
			$tag_name ="最新";
		} else if ( $tag == "hot") {
			$pics = Pic::model()->getHotPic();
			$tag_name = "热门";
		} else {
			$pics = Term::model()->getTagPic($tag);
		}
		$this->render('tagpic',array(
			'pics' =>$pics,
			'tag' => $tag,
			'tag_name' => $tag_name
		));
	}

	/**
	 * 标签\最新\热门 页面 的翻页
	 */
	public function actionTagpage($tag, $page=2) {
		$tag = urldecode($tag);
		if( $page > $this->allow_page ) return ;
		$this->layout = "ajax";
		if( $tag == "new") {
			$pics = Pic::model()->getNewPic($page);
		} else if ( $tag == "hot") {
			$pics = Pic::model()->getHotPic($page);
		} else {
			$pics = Term::model()->getTagPic($tag, $page);
		}
		$this->render('page',array(
			'pics' => $pics
		));
	}


	/**
	 * 错误信息展示
	 */
	public function actionError()
	{
		if($error=Yii::app()->errorHandler->error)
		{
			if(Yii::app()->request->isAjaxRequest)
				echo $error['message'];
			else
				$this->render('error', $error);
		}
	}

}