#!/bin/bash
FilesFromMuseScore=~/Documents/MuseScore2/Scores/*
FolderForScript=~/Documents/Practice/Python/MusicWork/


# Move files from MuseScore to processing
for file in $FilesFromMuseScore
do
	echo "Moving file $file to processing..."
	cp $file $FolderForScript
done

cd $FolderForScript

# Process midis
for file in *.mid
do
	echo "Processing $file..."
	python3 midi.py $file
done