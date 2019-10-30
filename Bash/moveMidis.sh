#!/bin/bash
FilesFromMuseScore=~/Documents/MuseScore2/Scores/*
FolderForScript=~/Documents/Practice/Python/MusicWork/

for file in $FilesFromMuseScore
do
	echo "Processing file $file ..."
	cp $file $FolderForScript
done