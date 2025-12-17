#!/bin/bash

#$-N init_00000



PRIMARY_DIR=/user/julia/Tutorial/1_TrainingSet/Initial/ICOND_00000//

cd $PRIMARY_DIR


$SHARC/SHARC_MOLPRO.py QM.in >> QM.log 2>> QM.err
