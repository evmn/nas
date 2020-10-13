#!/bin/bash

for num in {01..03}
do
	mkdir test$num
	cd test$num
	
	for i in {01..12}
	do
	        touch a.s01e$i.mp4
	        touch b.S02e$i.tc
	        touch c.s03E$i.mkv
	        touch d.S04E$i.avi
	        touch e.S05E$i.wmv
	        touch "f .S10E$i.wmv"
	done
	
	touch "a song of ice and fire"
	cd ..
done
