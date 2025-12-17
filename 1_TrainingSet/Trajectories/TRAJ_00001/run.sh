#!/bin/bash

#$-N fulv_00001
. $SHARC/sharcvars.sh



PRIMARY_DIR=/global/moritz/molecular_tully/fulvene/traj/Singlet_1/TRAJ_00001

cd $PRIMARY_DIR

$SHARC/sharc.x input
