--
-- 表的结构 `pic`
--
CREATE  TABLE  IF NOT EXISTS `pic` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `src` VARCHAR(255) NOT NULL COMMENT '图片来源' ,
  `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT  '存放时间' ,
  `view_count` SMALLINT NOT NULL DEFAULT 0 COMMENT '查看次数' ,
  `path` VARCHAR(255) BINARY NOT NULL COMMENT '存放位置' ,
  `file_name` VARCHAR(255) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NOT NULL COMMENT '图片名' ,
  `title` VARCHAR(255) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL COMMENT 'title' ,
  `postfix` VARCHAR(15) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL COMMENT '后缀' ,
  `remark` VARCHAR(255) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL COMMENT '备注' ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `src_UNIQUE` (`src` ASC) )
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci
COMMENT = '存放图片记录';

--
-- 表的结构 `host`
--
CREATE TABLE IF NOT EXISTS `host` (
  `id` int(11) NOT NULL auto_increment,
  `host` varchar(63) NOT NULL COMMENT 'host',
  `status` enum('enable','disable') NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `host_index` (`host`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;



--
-- 表的结构 `term`
--

CREATE TABLE IF NOT EXISTS `term` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(31) NOT NULL,
  `type` enum('tag') NOT NULL default 'tag',
  `created` timestamp NOT NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`id`),
  KEY `name_index` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- 表的结构 `pic_term_relation`
--

CREATE TABLE IF NOT EXISTS `pic_term_relation` (
  `id` int(11) NOT NULL auto_increment,
  `pic_id` int(11) NOT NULL,
  `term_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `pic_id` (`pic_id`),
  KEY `term_id` (`term_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
