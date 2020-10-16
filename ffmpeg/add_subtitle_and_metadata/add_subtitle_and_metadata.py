#!/usr/bin/python3
import os
import re

album = "Our Planet"
year = 2019
all_files = os.listdir('.')  # List current directory items

episode_list = [f[:-4] for f in all_files if f[-3:].lower() == "mkv"]
subtitle_list = [f[:-4] for f in all_files if f[-3:].lower() == "ass"]

matched = [f for f in episode_list if f in subtitle_list]

for title in matched:
	subtitle = title + ".ass"
	video = title + ".mkv"
	title = album + ": " + title
	script="""ffmpeg\t\t-i "{0}"  -i "{1}" \\\n \
	        -c copy -c:s subrip -map 0 -map -0:s -map 1 \\\n \
	        -metadata title="{2}"  \\\n \
	        -metadata:s:0 title="" -metadata:s:1 title="" \\\n \
	        -metadata:s:s:0 language=eng -metadata:s:2 title="" \\\n \
	        "tmp/{0}"
		""".format(video, subtitle, title)
	print(script)
#	os.system(script)
