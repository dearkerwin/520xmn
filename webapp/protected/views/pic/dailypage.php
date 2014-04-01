<?php 
$p = array();
	foreach ($pics as  $pic){
		$p[] = $pic['path'].$pic['file_name'];
	}
	echo json_encode($p);

		
?>
