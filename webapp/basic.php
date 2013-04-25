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

?>