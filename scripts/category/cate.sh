#!/bin/bash
# 在Centos 7及Ubuntu 20.04测试，可以正确处理包含空格的文件


# 先处理不包含S01E或者S1E的其它文件
special_file(){
	find . -maxdepth 1 -type f ! -iname  "*S[0-9]?E*" -and ! -iname "*S[0-9]E*" -print0 | while read -d $'\0' other
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
#        for other in *;
#        do
#                if [ -f "$other" ];
#                then
#                        if [ ! -d Specials ];
#                        then
#                                mkdir Specials
#                        fi
#                        mv "$other" Specials/ &
#                        #将其它文件放到Specials目录中
#                fi
#        done
}

# 处理完其它文件，再在后台处理电视剧文件，加快处理速度
tv_file(){
        for i in {01..50};
        do
                # 遍历子目录查找类似s01e02的文件，将来设置为不处理文件夹
                if [[ $(ls *[sS]${i}[eE]*  2>/dev/null) ]];
                then
                        if [ ! -d "Season $i" ];
                        then
                                mkdir "Season $i"
                        fi
                        mv *[sS]${i}[eE]* "Season $i/" &
			sleep 2
                fi
        done

}


for folder in */;
do
        echo "$folder"
        cd "$folder"
	special_file
	tv_file
        cd ..
done
