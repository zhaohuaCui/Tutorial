#!/bin/bash
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#create tmpdir
export TMPDIR=/public/`hostname -s`/scratch/tmp/$LOGNAME.$$
mkdir $TMPDIR
echo $TMPDIR
module use /usr/license/modulefiles
#information
CWD=$(pwd)
echo $HOSTNAME
#cd $TMPDIR
#cp $CWD/* .
cd $CWD
#execute SchNarc
python2 $SHARC/SHARC_MOLPRO.py QM.in >> QM.log 2>> QM.err

