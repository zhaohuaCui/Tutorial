#execute SchNarc
python $SCHNARC/schnarc_md.py pred ../../../DBs/Fulvene.db ../../../Models/Model1 --modelpaths ../../../Models/Model2 --adaptive --thresholds 0.1 100 100 100 1 >> NN.log 2>> NN.err

