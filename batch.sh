#!/bin/bash


cd /project/atlas/users/vcroft/tauRes/PantauPi0

#first get number of inputs
wc inputs.txt > nlines
read lines words characters filename < nlines
echo "in file: $filename, there are $lines lines"

batchnr=1
#((nbatches=$((lines/10))+1))
nbatches=2
echo "there will be $nbatches batches"

while [ $batchnr -le $nbatches ] ; do
    export batchnr
    echo "submitting batch nr $batchnr"
    qsub -V -q stbcq runTauRes.sh
    ((batchnr++))
done

