<?php
require_once("localRecord.php");
/**
 * This is the model class for table "pic".
 *
 * The followings are the available columns in table 'pic':
 * @property integer $id
 * @property string $src
 * @property string $created
 * @property integer $view_count
 * @property string $path
 * @property string $file_name
 * @property string $title
 * @property string $remark
 */
class Pic extends CActiveRecord
{
	/**
	 * Returns the static model of the specified AR class.
	 * @param string $className active record class name.
	 * @return Pic the static model class
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
		return 'pic';
	}

	/**
	 * @return array validation rules for model attributes.
	 */
	public function rules()
	{
		// NOTE: you should only define rules for those attributes that
		// will receive user inputs.
		return array(
			array('src, created, path', 'required'),
			array('view_count', 'numerical', 'integerOnly'=>true),
			array('src, path, file_name, title, remark', 'length', 'max'=>255),
			// The following rule is used by search().
			// Please remove those attributes that should not be searched.
			array('id, src, created, view_count, path, file_name, title, remark', 'safe', 'on'=>'search'),
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
			'tag'=>array(self::MANY_MANY, 'Term','pic_term_relation(pic_id, term_id)')
		);
	}

	/**
	 * @return array customized attribute labels (name=>label)
	 */
	public function attributeLabels()
	{
		return array(
			'id' => 'ID',
			'src' => 'Src',
			'created' => 'Created',
			'view_count' => 'View Count',
			'path' => 'Path',
			'file_name' => 'File Name',
			'title' => 'Title',
			'remark' => 'Remark',
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
		$criteria->compare('src',$this->src,true);
		$criteria->compare('created',$this->created,true);
		$criteria->compare('view_count',$this->view_count);
		$criteria->compare('path',$this->path,true);
		$criteria->compare('file_name',$this->file_name,true);
		$criteria->compare('title',$this->title,true);
		$criteria->compare('remark',$this->remark,true);

		return new CActiveDataProvider($this, array(
			'criteria'=>$criteria,
		));
	}

	public function getNewPic($page = 1, $per = 30, $condition = null) {
		if (empty($condition)) $condition = "1=1";
		$pics = array();
		$config = array(
			'select' => 'id,path,file_name,title,width,height',
			'limit' => $per,
			'condition' => $condition ,
			'order' => 'created DESC',
			'offset' => ($page - 1) * $per,
			'with' =>array('tag') 
			
		);
		$pics = $this->f($config);
		return $this->__encodePicId($pics);

	}

	public function getOnePic($id = 1) {
		$config = array(
			'select' => 'id,path,file_name,title,view_count,width,height',
			'condition' => "t.id=$id",
			'params' => array(':picID'=> $id),
			'with' =>array('tag')	
		);
		$pics = $this->f($config);
		return $this->__encodePicId($pics);
	}

	public function increasePicView($id ) {
		$pic = $this->findByPk($id);
		$pic->view_count ++;
		$pic->save();
	}

	public function getHotPic( $page = 1, $per = 30, $condition = null) {
		if (empty($condition)) $condition = "1=1";
		$config = array(
			'select' => 'id,path,file_name,view_count,title,width,height',
			'limit' => $per,
			'condition' => $condition ,
			'order' => 'view_count DESC',
			'offset' => ($page - 1) * $per,
		);
		$pics = $this->f($config);
		return $this->__encodePicId($pics);
	}


	public function getRandPic( $per = 30 ) {
		$count = $this->count();
		$numbers = range(1, $count); 
		$result = array_rand($numbers, $per); 
		$in_string = "(".join(",",$result).")";
		$config = array(
			'select' => 'id,path,file_name,title,view_count,width,height',
			'condition' => 'id in '.$in_string,	
		);
		$pics = $this->f($config);
		return $this->__encodePicId($pics);
	}


	/**
	 * 获取一个seed作为查询起点，获取几张图片
	 */
	public function getPicBySeed( $page=1, $per=30, $condition="1=1"){
		$count = $this->count($condition);
		if($count == 0) return array();
		if( ($page-1)*$per > $count ) return array();	//当前查询页大于图片的数量

		$seed = $this->get_rand_seed($count);		//获取一个查询起点
		$begin = $seed + ($page-1)*$per;
		$end = $seed + $page*$per;
		if( $end <= $count || $begin > $count){
			if ( $begin > $count){
				$begin = $begin - $count;
			} 
			$pic = $this->getPicWithBegin( $begin, $per,  $condition);	
		}else if( $begin <=$count && $end > $count ){
			$count2 = $end - $count ;
			$pic1 = $this->getPicWithBegin( $begin, $per,  $condition);
			$pic2 = $this->getPicWithBegin( 0, $count2,  $condition);	
			$pic = array_merge($pic1,$pic2);
		}
		return $pic;
	}

	/**
	 * 从begin开始，获取count个图片，指定begin 和 count
	 */
	function getPicWithBegin(  $begin, $count, $condition="1=1"){
		if (empty($condition)) $condition = "1=1";
		$config = array(
			'select' => 'id,path,file_name,title,width,height',
			'limit' => $count,
			'condition' => $condition ,
			'order' => 'view_count DESC',
			'offset' => $begin,
		);
		$pics = $this->f($config);
		return $this->__encodePicId($pics);
	}


	

	
}