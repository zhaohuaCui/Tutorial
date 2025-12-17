import ase
import ase.io

# read in the data set
dbname = "Fulvene.db"

geoms = ase.io.read(dbname,":")

# write reduced database with 500 data points
# note that this is only for the prediction mode as only geometries will be saved in this way
n=500
ase.io.write("Fulvene_%s.db"%n,geoms[:n])

