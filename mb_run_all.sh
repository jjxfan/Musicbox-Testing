for FILE in ../testScript/configFiles/*
do
../music_box $FILE
cp ../output.csv ./outputFiles/${FILE%.*}.csv

done
