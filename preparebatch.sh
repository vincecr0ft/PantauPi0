#!/bin/bash

cd /project/atlas/users/vcroft/tauRes/PantauPi0

DIR=/glusterfs/atlas1/users/vcroft/tauSamples/user.bwinter.TauPi0Rec_ESD2D3PD_doubleCB.147818.Pythia8_AU2CTEQ6L1_Ztautau.recon.ESD.e1176_s1479_s1470_r3553_tid00999076_00.v01-02.140709184748
ls $DIR/*.root > inputs.txt


#first get number of inputs
wc inputs.txt > nlines
read lines words characters filename < nlines
echo "in file: $filename, there are $lines lines"

job=1
batchnr=1
((nbatches=$((lines/5))+1))
#nbatches=2
echo "there will be $nbatches batches"
comma="2" 



while [ $batchnr -lt $nbatches ] ;do
#    comma=$batchnr
    awk "NR==$job,NR==$job+4" inputs.txt | awk '{ print $0 >> "thisbatch"}'
    while read -r line
    do
	echo $line >> "input"$batchnr".txt"
    done<thisbatch
    rm thisbatch
    ((job+=5))
    ((batchnr+=1))
done

#dont forget the last few files in the last batch
#comma=$batchnr
awk "NR>$job" inputs.txt | awk '{ print $0 >> "thisbatch"}'
while read -r line
do
    echo $line >> "input"$batchnr".txt"
done<thisbatch
rm thisbatch



