# tmdb查询视频记录

## 系统要求

 - Python 3
 - [tmdbsimple](https://github.com/celiao/tmdbsimple)
 - 替换程序中tmdb的API KEY


数据库文件tv.csv，格式为**视频名@首映年份**，年份未知则为空：

```
 1 亮剑@2005
 2 士兵突击@2006
 3 康熙微服私访记1@
 4 康熙微服私访记2@
 5 康熙微服私访记3@
 6 康熙微服私访记4@
 7 新京华烟云@2014
 8 爱情悠悠药草香@2013
```

运行tv.py，在tmdb查询tv.csv，运行结果如下:


```
1.	亮剑 (2005)
2.	士兵突击 (2006)
3.	康熙微服私访记1 (1997)
4.	康熙微服私访记2 (1999)
5.	康熙微服私访记3 (2000)
6.	康熙微服私访记4 (2002)
7.	新京华烟云 (2014)
8.	爱情悠悠药草香 (2013)
9.	狙击部队 (2013)
10.	秘密森林 (2017)
11.	血色浪漫 (2004)
12.	=== 我的军官女友 无tmdb记录 ===
13.	=== 2589的距离 无tmdb记录 ===
14.	--- 回家 在tmdb有3条记录 ---
		1. 回家狂想曲 (2017-01-23)
		2. 回家的路有多远 (2017-12-06)
		3. 爱·回家之开心速递 (2017-06-01)
15.	Life Less Ordinary 小人物向前冲 (2017)
16.	=== 欢喜就好3 无tmdb记录 ===
17.	=== 爱不迟疑 无tmdb记录 ===
18.	=== 高校学朝 无tmdb记录 ===
19.	=== 星期二特写 一生 护事 无tmdb记录 ===
20.	=== 118大结局 无tmdb记录 ===
21.	=== Code of Law S4 无tmdb记录 ===
22.	=== Ghosts AR 无tmdb记录 ===
23.	=== 入侵者前传 无tmdb记录 ===
24.	=== 加文纳桥的约定 无tmdb记录 ===
25.	=== 千年来说对不起之前传 无tmdb记录 ===
26.	=== 对面的女孩 无tmdb记录 ===
27.	=== 料理人生 无tmdb记录 ===
28.	=== 新生 无tmdb记录 ===
29.	=== 梦行者 无tmdb记录 ===
30.	=== 给我一百万 无tmdb记录 ===
31.	=== 维多利亚的模力 无tmdb记录 ===
32.	=== 闭上眼就看不见 无tmdb记录 ===
33.	=== I'm Madam 无tmdb记录 ===
34.	=== 北京到莫斯科 无tmdb记录 ===
35.	谁是凶手？ (2020)
```

