for FILE in ../ConfigData/*
do
../../music_box $FILE
filename=$(basename "$FILE")
cp ./output.csv ./outputFiles/${filename%.*}.csv

done
