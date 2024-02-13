for FILE in ./initialConcentrationFiles/*
do
rm ./model/configuration/initialConcentrations.config

cp $FILE ./model/configuration/initialConcentrations.config
./build/build_atchem2.sh ./model/mechanism.fac
./atchem2
cp ./model/output/speciesConcentrations.output ./outputFiles/$(date +%Y_%m_%d_%I_%M_%p_.%3N).csv

done
