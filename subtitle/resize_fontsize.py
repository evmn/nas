#!/usr/bin/python3
import ass
import os
all_files = os.listdir('.') 

subtitles=[s for s in all_files if s[-3:].lower() == "ass"]
for sub in subtitles:
	with open(sub, encoding='utf_8_sig') as f:
		doc = ass.parse(f)
		for style in doc.styles:
#			print(style.fontname,style.fontsize)
			# 把字幕字体设置为之前的2倍
			style.fontsize = style.fontsize * 2
		with open("out/"+sub, "w", encoding='utf_8_sig') as g:
#			# 保存字幕到out文件夹内
			doc.dump_file(g)
