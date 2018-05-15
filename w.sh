#!/bin/bash

#files=$(rsync repo.monroe-system.eu:/experiments/backups/2018-04/|awk '/processed/ {print $5}')
#files=$(echo processed-2018-04-{23,24,25,26,27,28,29}.txz)
files=$(echo processed-2018-05-{01,02,03,04,05,06,07,08}.txz)

export HERE=$(pwd)

for f in $files
    do
        cd $HERE
        export DIR=workdir
        mkdir $DIR
        (cd $DIR
         echo "Using $(pwd) as workdir"
         rsync repo.monroe-system.eu:/experiments/backups/2018-05/$f .
         date; echo "Doing $f..."
         tar Jxf $f --wildcards --no-anchored '*HEADLESS*'
         cd 2018*
         python ../../a.py > ../../result-${f}.txt
         echo -n "done with $f at "; date
        )
        rm -fr $DIR
    done

echo "DONE"
