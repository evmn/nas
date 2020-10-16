# tmdb查询视频记录

## 系统要求

 - Python 3
 - [tmdbsimple](https://github.com/celiao/tmdbsimple)
 - 替换程序中tmdb的API KEY


数据库文件media.list为程序用到的csv数据库，格式为**视频名@首映年份**，年份未知则为空：

```
群鸟@1963
小人物向前冲@2017
美人计@1946
北极@2018
玉面飞狐@
伯尼小海豚2@2019
大内高手@
年轻气盛@2015
恶虎村@
K: Seven Stories Movie 3 - Side:Green - The Overwritten World@2018
特别的她 Alternative@2018
```

运行`multi_query.py`，在[tmdb](https://www.themoviedb.org/)查询`media.list`，运行结果如下:


```
01.电影🎥	群鸟 (1963)
02.剧集  	小人物向前冲 (2017)
03.电影🎥	美人计 (1946)
04.	北极 在tmdb有2条记录
		1.电影🎥  北极 (2018)
		2.电影🎥  北极熊诺姆：王国之匙 (2018)
05.	玉面飞狐 在tmdb有2条记录
		1.剧集    玉面飞狐 (1989)
		2.电影🎥  玉面飞狐 (1968)
06.	 === 伯尼小海豚2 无tmdb记录 ===
07.电影🎥	大内高手 (1972)
08.电影🎥	年轻气盛 (2015)
09.电影🎥	恶虎村 (1974)
10.电影🎥	K Seven Stories SIDE:GREEN ~上書き世界~ (2018)
11.电影🎥	特别的她 Alternative (2018)
```

