#!/bin/bash
source /project/atlas/nikhef/cvmfs/setup.sh
source $ATLAS_LOCAL_ROOT_BASE/user/atlasLocalSetup.sh
source $ATLAS_LOCAL_ROOT_BASE/packageSetups/atlasLocalROOTSetup.sh --rootVersion 5.34.18-x86_64-slc6-gcc48-opt
cd /project/atlas/users/vcroft/tauRes/PantauPi0/

echo "submitting batch number "$batchnr
python /project/atlas/users/vcroft/tauRes/PantauPi0/tauRes.py $batchnr
