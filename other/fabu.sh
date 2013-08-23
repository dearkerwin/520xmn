#!/bin/sh

# 实现功能  把目录A 的所有文件更新到 目录B， 可以增加不需要更新的 文件后缀 array
# 更新规则：
#                       1、新增目录： 如果A下有，但是B下没有，则在B下创建相应的文件夹（权限相同）
#                       2、更新目录： 如果目录权限更改，则会相应地更改
#                       3、新增文件： 如果A下有，但是B下没有，则从A复制到B，
#                       4、更新文件：判断A下文件和B下文件 的权限、大小、最后修改时间，如果不同则从A复制到B
#           5、删除文件：B下的文件，在A下找不到，则认为已经被删除，则删除B下相应的文件
#                       6、ln连接：如果A下有软连接，则复制到B，一旦更新，会相应更新


array=("log","pyc") # ignore 的后缀


function compareDir() {

        local sourDir=$1
        local descDir=$2
        local subPath=''
        local sour_nowPath=$sourDir
        local desc_nowPath=$descDir
        if [ $# -eq 3 ]; then
                subPath=$3"/"
                sour_nowPath=$sourDir"/"$subPath
                desc_nowPath=$descDir"/"$subPath
        fi

        #--begin--当前文件夹
        if [ ! -d "$desc_nowPath" ]; then
                #获取文件夹权限
                local mod=`stat -c %a $sour_nowPath`
                `mkdir -m $mod $desc_nowPath`
                echo "++d  $subPath"
        else
                #判断权限是否一致
                local sour_mod=`stat -c %a $sour_nowPath`
                local desc_mod=`stat -c %a $desc_nowPath`
                if [ "$sour_mod" != "$desc_mod" ];then
                        echo "=mod $sour_mod "$subPath
                        `chmod $sour_mod $desc_nowPath`
                fi
        fi
        #--end--当前文件夹

        #--begin-- 增加或者修改的 文件
        for file in `ls $sour_nowPath`
                do
                        #后缀判断，如果属于ignore，则忽略
                        extension=${file##*.}
                        [[ "${array[@]/$extension/}" != "${array[@]}" ]] && continue

                        local name=$subPath""$file
                        local sour_filename=$sourDir"/"$name
                        local desc_filename=$descDir"/"$name

                        #如果是ln连接
                        if [ -L $sour_filename ]; then
                                if [ -L $desc_filename ]; then
                                        local sour_link=`ls -l $sour_filename|awk '{print $11}'`
                                        local desc_link=`ls -l $desc_filename|awk '{print $11}'`
                                        if [ "$sour_link" != "$desc_link" ]; then
                                                echo "+M   "$name
                                                `cp -a $sour_filename $desc_filename`
                                        fi
                                else
                                        echo "+L   "$name
                                        `cp -a $sour_filename $desc_filename`
                                fi

                        #如果是文件夹 递归
                        elif [ -d $sour_filename ]; then
                                compareDir $sourDir $descDir $name

                        #如果是普通文件
                        else
                                if [ -f $desc_filename ]; then
                                        local sour_size=`ls -l  $sour_filename|awk '{print $5}'`
                                        local sour_modified=`ls -l $sour_filename|awk '{print $6}'`
                                        sour_modified=$sour_modified" "`ls -l $sour_filename|awk '{print $7}'`
                                        sour_modified=$sour_modified" "`ls -l $sour_filename|awk '{print $8}'`

                                        local desc_size=`ls -l  $desc_filename|awk '{print $5}'`
                                        local desc_modified=`ls -l $desc_filename|awk '{print $6}'`
                                        desc_modified=$desc_modified" "`ls -l $desc_filename|awk '{print $7}'`
                                        desc_modified=$desc_modified" "`ls -l $desc_filename|awk '{print $8}'`

                                        if [ $sour_size=$desc_size ] && [ "$sour_modified"x = "$desc_modified"x ]; then
                                                local tmp=1
                                        else
                                                echo "+M   "$name
                                                `cp -p $sour_filename $desc_filename`
                                        fi

                                        #判断权限
                                        local sour_mod=`stat -c %a $sour_filename`
                                        local desc_mod=`stat -c %a $desc_filename`
                                        if [ "$sour_mod" != "$desc_mod" ];then
                                                echo "=mod $sour_mod "$name
                                                `cp -p $sour_filename $desc_filename`
                                        fi
                                else
                                        echo "++   "$name
                                        `cp -p $sour_filename $desc_filename`
                                fi
                        fi
                done
        #--end--增加或者修改的 文件

        #--begin--需要删除的文件
        for file in `ls $desc_nowPath`
                do
                        extension=${file##*.}
                        [[ "${array[@]/$extension/}" != "${array[@]}" ]] && continue

                        if [ ! -d $desc_nowPath"/"$file ]
                        then
                                local name=$subPath""$file
                                local sour_filename=$sourDir"/"$name
                                local desc_filename=$descDir"/"$name
                                if [ ! -f $sour_filename ]
                                then
                                        echo "--   $name"
                                        `rm -f $desc_filename`
                                fi
                        fi
                done
        #--end--需要删除的文件
}



IFS=$'\n'                      #这个必须要，否则会在文件名中有空格时出错
SOUR_DIR="/var/www/520xmn"
DESC_DIR="/var/www/online_520xmn"

compareDir $SOUR_DIR $DESC_DIR
