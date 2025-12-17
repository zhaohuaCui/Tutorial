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
for i in {0..29}
do
 cd Calc_${i}
 python2 $SHARC/SHARC_MOLPRO.py QM.in >> QM.log 2>> QM.err
 let j=$i+1
 echo $j
 cp -r SAVEDIR ../Calc_$j
 cd .. 
done

