<?php

class localRecord extends CActiveRecord {

	/**
	 * 获取数据，并且格式化数据
	 *
	 */
	private function _find( $config = array()) {
		$default_config = array(
			'limit' => 30,
			'order' => 'id DESC',
		);

		$find_config = array_merge( $default_config, $config);
		$items = $this->findAll($find_config);
		$return_items = array();
		if(empty($items)) return array();

		$relations = array();
		if( isset($find_config['with'])) {
			$relations = $find_config['with'];
		} 

		foreach ($items as  $item) {
			$atts = $item->getAttributes();
			$atts = $this->_filter_item_value($atts);
			
			$rel = $this->_get_item_rel($relations, $item);
			!empty($rel) && $atts['Relations'] = $rel;  //获取rel数据
			$return_items[] = $atts;
		}
		return $return_items;
	}

	/**
	 * 获取一个Model的relation 数据
	 *
	 */
	private function _get_item_rel( $relations, $item) {
		$rel_return = array();
		foreach ($relations as $rel) {
			$rel_obj = $item->$rel;
			$rel_values = array();
			if(!empty($rel_obj)) {
				foreach ($rel_obj as  $rel_obj_single) {
					$rel_values[] = $rel_obj_single->getAttributes();
				}
			}
			$rel_return[$rel] = $rel_values;
		}
		return $rel_return;
	}

	private function _filter_item_value($item) {
		foreach ($item as $key => $value) {
			if( $item[$key] === null) { unset($item[$key]);}
		}
		return $item;
	}

}



?>