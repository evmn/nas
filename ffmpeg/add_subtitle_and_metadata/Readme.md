# 对mkv视频批量添加ass英文字幕，并编辑metadata标题

在test目录运行`add_subtitle_and_metadata.py`，会输出下面的结果:

```sh
ffmpeg		-i "02.mkv"  -i "02.ass" \
 	        -c copy -c:s subrip -map 0 -map -0:s -map 1 \
 	        -metadata title="Our Planet: 02"  \
 	        -metadata:s:0 title="" -metadata:s:1 title="" \
 	        -metadata:s:s:0 language=eng -metadata:s:2 title="" \
 	        "tmp/02.mkv"

ffmpeg		-i "S01E01 One Planet.mkv"  -i "S01E01 One Planet.ass" \
 	        -c copy -c:s subrip -map 0 -map -0:s -map 1 \
 	        -metadata title="Our Planet: S01E01 One Planet"  \
 	        -metadata:s:0 title="" -metadata:s:1 title="" \
 	        -metadata:s:s:0 language=eng -metadata:s:2 title="" \
 	        "tmp/S01E01 One Planet.mkv"
```
