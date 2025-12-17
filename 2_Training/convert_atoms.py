from ase.units import Bohr
import ase.io
from ase.atoms import Atoms 

geoms = ase.io.read("initconds.xyz",":")
geoms_bohr = []
for i in range(len(geoms)):
    geoms_bohr.append(Atoms(geoms[i].get_atomic_numbers(),geoms[i].get_positions()/Bohr))

# write db 
ase.io.write("initconds.db", geoms_bohr)
