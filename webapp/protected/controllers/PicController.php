<?php

class PicController extends Controller
{
	public $layout = 'pic';
	public function actionIndex()
	{

		debug(Term::model()->getTagPic('吊带'));
		$new_pics = Pic::model()->getNewPic(1);
		$this->render('index',array(
			'new_pics' => $new_pics,
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
}