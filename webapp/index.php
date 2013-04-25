<?php

// change the following paths if necessary
$yii=dirname(__FILE__).'/framework/yii.php';
$config=dirname(__FILE__).'/protected/config/main.php';
$constant = dirname(__FILE__).'/protected/config/520xmn_constant.php';

// remove the following lines when in production mode
defined('YII_DEBUG') or define('YII_DEBUG',true);
// specify how many levels of call stack should be shown in each log message
defined('YII_TRACE_LEVEL') or define('YII_TRACE_LEVEL',3);

defined('YII_ROOT') or define('YII_ROOT',dirname(__FILE__));

require_once($yii);
require_once($constant);
require_once(dirname(__FILE__).'/basic.php');
Yii::createWebApplication($config)->run();
