#!/bin/bash
FilesFromMuseScore=~/Documents/MuseScore2/Scores/*
FolderForScript=~/Documents/Practice/Python/MusicWork/


# Move files from MuseScore to processing
for file in $FilesFromMuseScore
do
	echo "Moving file $file to processing..."
	cp $file $FolderForScript
done

# Process midis
for file in $FolderForScript.mid
do
	echo "Processing $file..."
	python3 
done