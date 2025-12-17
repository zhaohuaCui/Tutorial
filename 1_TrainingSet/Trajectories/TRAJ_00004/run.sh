#!/bin/bash

#$-N fulv_00004
. $SHARC/sharcvars.sh



PRIMARY_DIR=/global/moritz/molecular_tully/fulvene/traj/Singlet_1/TRAJ_00004/

cd $PRIMARY_DIR

$SHARC/sharc.x input
