<?php
	function debug($var = false) {
		if (YII_DEBUG) {
			print "\n<pre  style=\"text-align:left\">\n";
			$calledFrom = debug_backtrace();
			print "\n\r";
            echo '<strong>' . substr(str_replace(YII_ROOT, '', $calledFrom[0]['file']), 0) . '</strong>';
            echo ' (line <strong>' . $calledFrom[0]['line'] . '</strong>)';
            print "\n";
			ob_start();
			print_r($var);
			$var = ob_get_clean();
			print "{$var}\n</pre>\n";
		}
	}


	function encodeID($id) {
		$ge = $id%10;
		if($ge == 0) $ge = 1;
		$encode_int = ($id*7 + 20130518)*$ge ;
		$encode_str = $encode_int.$ge;
		return $encode_str;
	}

	function decodeId($encode_str) {
		$encode_str = (int)$encode_str;
		$ge = $encode_str%10;
		if($ge == 0) {
			 throw new CHttpException(400,'请求无效');
		}
		$encode_int = substr($encode_str, 0, -1 );
		$id = ($encode_int/$ge - 20130518)/7;
		if( is_int($id) && $id > 0) {
			return $id;
		} else {
			 throw new CHttpException(400,'请求无效');
		}	
	}

?>