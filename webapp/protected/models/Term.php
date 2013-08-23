<?php

/**
 * This is the model class for table "term".
 *
 * The followings are the available columns in table 'term':
 * @property integer $id
 * @property string $name
 * @property string $type
 * @property string $created
 */
class Term extends CActiveRecord
{
	/**
	 * Returns the static model of the specified AR class.
	 * @param string $className active record class name.
	 * @return Term the static model class
	 */
	public static function model($className=__CLASS__)
	{
		return parent::model($className);
	}

	/**
	 * @return string the associated database table name
	 */
	public function tableName()
	{
		return 'term';
	}

	/**
	 * @return array validation rules for model attributes.
	 */
	public function rules()
	{
		// NOTE: you should only define rules for those attributes that
		// will receive user inputs.
		return array(
			array('name, created', 'required'),
			array('name', 'length', 'max'=>31),
			array('type', 'length', 'max'=>3),
			// The following rule is used by search().
			// Please remove those attributes that should not be searched.
			array('id, name, type, created', 'safe', 'on'=>'search'),
		);
	}

	/**
	 * @return array relational rules.
	 */
	public function relations()
	{
		// NOTE: you may need to adjust the relation name and the related
		// class name for the relations automatically generated below.
		return array(
			'picture'=>array(self::MANY_MANY, 'Pic','pic_term_relation(term_id,pic_id)',
							'order' => 'picture.view_count desc'
				),
			'tag_count' =>array(self::STAT, 'PicTermRelation', 'term_id','select'=>'count(term_id)')
		);
	}

	/**
	 * @return array customized attribute labels (name=>label)
	 */
	public function attributeLabels()
	{
		return array(
			'id' => 'ID',
			'name' => 'Name',
			'type' => 'Type',
			'created' => 'Created',
		);
	}

	/**
	 * Retrieves a list of models based on the current search/filter conditions.
	 * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
	 */
	public function search()
	{
		// Warning: Please modify the following code to remove attributes that
		// should not be searched.

		$criteria=new CDbCriteria;

		$criteria->compare('id',$this->id);
		$criteria->compare('name',$this->name,true);
		$criteria->compare('type',$this->type,true);
		$criteria->compare('created',$this->created,true);

		return new CActiveDataProvider($this, array(
			'criteria'=>$criteria,
		));
	}


	/** 
	 *根据tag名称获取图片
	 */
	public function getTagPic( $tag, $page= 1, $per = 30 ) {
		$pics = array();
		$config = array(
			'condition' => 'name=:tagName',
			'params' => array(':tagName'=> $tag),
		);
		$tagModel  = $this->find($config);
		if( !empty($tagModel) ) {
			$picsModel = $tagModel->picture(array('limit' => $per,'offset' => ($page - 1) * $per));
			if( !empty($picsModel)) {
				foreach ($picsModel as  $value) {
					$pics[] = $value->getAttributes();
				}
			}	
		}	
		return $this->__encodePicId($pics);
	}

	/**
	 * 获取所有标签 的图片数
	 */
	public function getTagCount() {
		$config = array(
			'select' => 'id, name',
			'with' => array('tag_count')
		);
		$tags = $this->f($config);
		$tagsCount = array();
		foreach ($tags as $key => $value) {
			$tagsCount[$value['name']] =  $value['Relations']['tag_count'];
		}
		return $tagsCount;
	}

	/**
	 * 获取一个标签中图片的总数量
	 */
	public function getSingleTagCount($tag) {
		$config = array(
			'select' => 'id, name',
			'condition' => 't.name=:tagName',
			'params' => array(':tagName'=> $tag),
			'with' => array('tag_count')
		);
		$tags = $this->f($config);
		$tagsCount = array();
		foreach ($tags as $key => $value) {
			$tagsCount[$value['name']] =  $value['Relations']['tag_count'];
		}
		return $tagsCount;
	}

	/**
	 * 获取一个seed作为查询起点, 随机获取一个标签的几张图片
	 */
	public function getPicBySeed($tag, $page=1, $per=30){
		$count = $this->getSingleTagCount($tag);
		$count = isset( $count[$tag]) ?  $count[$tag] : 0 ;
		if($count == 0) return array();
		if( ($page-1)*$per > $count ) return array();	//当前查询页大于图片的数量

		$seed = $this->get_rand_seed($count);		//获取一个查询起点
		$begin = $seed + ($page-1)*$per;
		$end = $seed + $page*$per;
		if( $end <= $count  ){
			$pic = $this->getTagPicWithLimt($tag, $begin, $per);	
		}else if ( $begin > $count ){
			$begin = $begin - $count;
			$count1 = ($begin + $per > $seed) ? ($seed - $begin) : $per;
			$pic = $this->getTagPicWithLimt($tag, $begin, $count1);
		}else if( $begin <=$count && $end > $count ){
			$count2 = $end - $count ;
			$pic1 = $this->getTagPicWithLimt($tag, $begin, $per);
			$pic2 = $this->getTagPicWithLimt($tag, 0, $count2);	
			$pic = array_merge($pic1,$pic2);
		}
		return $pic;
	}

	

	/**
	 * 获取指定tag 的图片，从begin开始，获取count个图片
	 */
	function getTagPicWithLimt( $tag, $begin, $count){
		$pics = array();
		$config = array(
				'condition' => 'name=:tagName',
				'params' => array(':tagName'=> $tag),
			);
		$tagModel  = $this->find($config);
		if( !empty($tagModel) ) {
			$picsModel = $tagModel->picture(array('limit' => $count,'offset' =>$begin));
			if( !empty($picsModel)) {
				foreach ($picsModel as  $value) {
					$pics[] = $value->getAttributes();
				}
			}	
		}
		return $this->__encodePicId($pics);	
	}
}