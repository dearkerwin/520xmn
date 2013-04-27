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
				)
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
		return $pics;
	}
}