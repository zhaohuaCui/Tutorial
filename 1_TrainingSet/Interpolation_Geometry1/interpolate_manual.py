from interpolation import interpolate
import os
import numpy as np
from glob import iglob
import shutil
import os
import readline
import pprint
import sys
from sys import argv
if __name__ == "__main__":
  try:
    name, start, end  = argv
  except ValueError:
    print( "Usage: script <QMpath (TRAJ of QM)> <NNpath (TRAJ broke from NN)> <icondpath (Path of ICOND_00000)> <NN path (where output_all.dat is located)> <stepsize> <Nr of performed scan>")
    exit()
  start = argv[1]
  end = argv[2]
  natoms=12
  n_singlets=2
  n_triplets = 0
  interpolate(start,end,natoms,n_singlets,n_triplets)
