#!/bin/bash

#$-N init_00018



PRIMARY_DIR=/user/julia/Tutorial/1_TrainingSet/Initial/ICOND_00018//

cd $PRIMARY_DIR

if [ -d ../ICOND_00000/SAVE ];
then
  if [ -d ./SAVE ];
  then
    rm -r ./SAVE
  fi
  cp -r ../ICOND_00000/SAVE ./
else
  echo "Should do a reference overlap calculation, but the reference data in ../ICOND_00000/ seems not OK."
  exit 1
fi


$SHARC/SHARC_MOLPRO.py QM.in >> QM.log 2>> QM.err
