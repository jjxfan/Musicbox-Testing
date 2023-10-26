for FILE in ../ConfigData/*
do
../../music_box $FILE
cp ../output.csv ./outputFiles/${FILE%.*}.csv

done
