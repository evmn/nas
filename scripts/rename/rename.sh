#!/bin/bash
# 
# First parameter is title, second one is episode info, third one is other info
# rename.sh 1 6 2-5,7
# Episode-Name.2015.WEB.Hindi-Eng.site-info.S01E01.mkv -> Episode-Name.S01E01.2015.WEB.Hindi-Eng.site-info.mkv
# Are you sure (Y/N)? 

asksure() {
echo -n "Are you sure (Y/N)? "
while read -r -n 1 -s answer; do
	if [[ $answer = [YyNn] ]]; then
		[[ $answer = [Yy] ]] && retval=0
		[[ $answer = [Nn] ]] && retval=1
		break
	fi
done
echo # just a final linefeed, optics...
return $retval
}

for file in *.mkv
do
	title=$(echo $file | cut -d . -f $1)
	episode=$(echo $file | cut -d . -f $2)
	other=$(echo $file | cut -d . -f $3)
	newname=$title.$episode.$other
	echo "$file -> $newname"
	if asksure; then
		mv "$file" "$newname" &
	fi
done
