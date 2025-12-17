# first we generate many initial conditions

python2 $SHARC/wigner.py -n 1000 -x ../Inputfiles/freq.molden 

# then we transform the initconds.xyz file to an ase-db format
# Note that we need to transform the structures from Angstrom to Bohr

python convert_atoms.py

