<?php

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
}