<?php

class PicController extends Controller
{
	public $layout = 'index';
	public function actionIndex()
	{
		$this->render('index',array(
				'new_pics' => Pic::model()->getNewPic(4,12),
				// 'new_pics' => Term::model()->getTagPic("清纯",1,12),
				'hot_pics' => Pic::model()->getHotPic(1,8),
				'rand_pics' => Pic::model()->getRandPic()
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
		$this->layout = "pic";
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
		$this->layout = "ajax";
		$this->render('page',array(
			'pics' => Pic::model()->getRandPic()
		));
	}

	/**
	 * 标签\最新\热门 页面
	 */
	public function actionTagpic($tag) {
		$pics = array();
		if( $tag == "new") {
			$pics = Pic::model()->getNewPic();
		} else if ( $tag == "hot") {
			$pics = Pic::model()->getHotPic();
		} else {
			$pics = Term::model()->getTagPic($tag);
		}
		$this->render('tagpic',array(
			'pics' =>$pics,
			'tag' => $tag
		));
	}

	/**
	 * 标签\最新\热门 页面 的翻页
	 */
	public function actionTagpage($tag, $page=2) {
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
	

}