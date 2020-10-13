#!/bin/bash
# 在Centos 7及Ubuntu 20.04测试，可以正确处理包含空格的文件
for folder in */;
do
        echo "$folder"
        cd "$folder"
        for i in {01..10};
        do
                # 遍历子目录查找类似s01e02的文件，将来设置为不处理文件夹
                if [[ $(ls *[sS]${i}[eE]*  2>/dev/null) ]];
                then
                        if [ ! -d "Season $i" ];
                        then
                                mkdir "Season $i"
                        fi
                        #将来让此命令在后台执行或许可以加快速度
                        mv *[sS]${i}[eE]* "Season $i/"
                fi
        done

        for other in *;
        do
                if [ -f "$other" ];
                then
                        if [ ! -d Specials ];
                        then
                                mkdir Specials
                        fi
                        mv "$other" Specials/
                        #将其它文件放到Specials目录中
                fi
        done
        cd ..
done
