This example is based on fulvene. If you want to train another molecule, change the name of the dataset in the following run-scripts.

# Training (on the example of a very small initial training set): 

Although we recommend to use the trained models for the following sections in this tutorial, you can train your own SchNarc model by executing the following run-script if you have a CPU:
``sh train_cpu.sh``
or if you have a GPU:
``sh train_gpu.sh``

We strongly recommend to train a model on a GPU, as the training is expected to take several days on a GPU.

Take a look at the tradeoffs-file. It defines which properties you train. The first number after each property indicates the weight of each property during training, i.e., how much the error of this property is weighted in the loss function. The second - fifth numbers indicate the number of singlets, doublets, triplets, and quartetts used for training.

Note that for training we use the initially generated training set "Fulvene.db" which only contains 100 data points. you need to copy this training set to the "DBs" folder. 

# Validation

Execute 
``sh eval_cpu.sh``
or 
``sh eval_gpu.sh`` 
to predict the error on the validation set. The error is saved in the "Train" folder.

# Prediction

First, we will generate more initial conditions with SHARC and transform these into an ase-db. 
Execute
``sh get_initial_conditions.sh``
Then we can predict the new db file "initcond.db".
Execute
``sh pred_cpu.sh``
or 
``sh pred_gpu.sh``
to predict the properties of the molecules written in the file "initcond.db"
Check the jupyter notebook "Check\_prediction.npz" to see how to load these properties into an numpy array and to plot them.


If you wish to use the pretrained model, simply change the path to the trained model is the pred\_cpu.sh, ... files from "Train" to "../Models/Model1".
