#training on a CPU using 80 data points for training, 10 for validation, a batch size of 10 and the Trainingset CH2NH2.db
python $SCHNARC/run_schnarc.py train schnet --split 80 10 --tradeoffs tradeoffs.yaml --batch_size 10 --min_loss --cuda ../DBs/Fulvene.db Train

