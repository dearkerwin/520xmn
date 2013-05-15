<?php
/**
 *  标签云
 */
class TagCloudWidget extends CWidget{
	public function run() {
		$tag_count = Term::model()->getTagCount();
		foreach ($tag_count as $key => $value) {
			$link = Yii::app()->createUrl("Pic/tagpic",array("tag"=>$key));
			$tag = array('text'=> $key, 'weight'=> $value, 'link' =>$link  );
			$tags[] = $tag;
		}
		$this->render('tagcloud',array(
			'tags' => json_encode($tags)
		));
   }
}