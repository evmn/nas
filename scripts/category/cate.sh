#!/bin/bash
# 在Centos 7及Ubuntu 20.04测试，可以正确处理包含空格的文件
move_file(){
        for i in {01..10};
        do
                # 遍历子目录查找类似s01e02的文件，将来设置为不处理文件夹
                if [[ $(ls *[sS]${i}[eE]*  2>/dev/null) ]];
                then
                        if [ ! -d "Season $i" ];
                        then
                                mkdir "Season $i"
                        fi
                        # 不能在后台运行过多的命令，网络缓存会让下面的Specials先执行
			# 除非先用正则表达式匹配并处理不包含[sS]${i}[eE]的文件
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
                        mv "$other" Specials/ &
                        #将其它文件放到Specials目录中
                fi
        done
}


for folder in */;
do
        echo "$folder"
        cd "$folder"
	move_file 
	sleep 10
        cd ..
done
