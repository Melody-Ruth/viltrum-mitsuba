#!/usr/bin/env bash
cd ../../../mitsuba
source setpath.sh 
cd ../scenes/dragon/

cd ../../graphing
printf "" > results.txt
cd ../scenes/dragon/

for i in {1..16}
do
    mitsuba -p 1 ./automated/scene_paper_non$i.xml > /dev/null 2>&1
    mitsuba -p 1 ./automated/scene_paper$i.xml > /dev/null 2>&1
    cd ../../graphing
    printf "$i," >> results.txt
    python3 compareImg.py >> results.txt
    cd ../scenes/dragon
    printf "i=$i done"
done

printf "Done"