This example is based on fulvene. If you want to train another molecule, change the name of the dataset in the following run-scripts.

# 1) Get the initial training set

Go into the folder "1\_TrainingSet/Initial" and open the jupyter notebook to see an example on how to generate an initial training set.
Copy the generated training set into the folder "DBs". 

# 2) Training (on the example of a very small initial training set): 

Go to the directory "2\_Training".
Although we recommend to use the trained models for the following sections in this tutorial, you can train your own SchNarc model by executing the following run-script if you have a CPU:
``sh train_cpu.sh``
or if you have a GPU:
``sh train_gpu.sh``

We strongly recommend to train a model on a GPU, as the training is expected to take several days on a GPU.
The full training set for Fulvene.db will be available with the corresponding publication. 

# 3) Validation (optional):

Go to the directory "2\_Training" if you are not already inside of it.
After training the model, you can validate it by predicting the error on the properties on a validation or test split (in the example, you predict the error on the validation set).
Therefore, carry out:
``sh eval_cpu.sh`` or ``sh eval_gpu.sh`` dependent on whether you have a GPU available or not.

As a result, you will receive two files that are saved in the "Train" folder. They are named "evaluation\_qmvalues.npz" and "evaluation\_values.npz". The former contains the reference energies, forces, and other properties on the predicted data points, whereas the latter contains the respective predicted values. You can load these files using "np.load()". You can use the jupyter notebook "Validation.ipynb" to see how this works.

# 4) Prediction:

Go to the directory "2\_Training" if you are not already inside this folder.
After training and validation of your model, you can predict the energies and dipole moments of any data set that only require molecular structures. For instance, you can generate many initial conditions with SHARC and save it to an ase-db format. You can generate many initial conditions with the script and the provided frequency file:
``sh get_initial_conditions.sh``
You can then transform the initconds.xyz to an ase db format via:
``sh convert_geometry.py`` 

For the prediction of these geometries with SchNarc, carry out:
``sh pred_cpu.sh``, ``sh pred_cpu_minimal.sh`` or ``sh pred_gpu.sh``
Note that the first and last scripts use the full initial-conditions data set, which can take up to 30 min on a CPU. Thus, you can use the "pred\_cpu\_minimal" script, which uses only 500 data points for prediction.
You can check the "adapt\_dataset.py" script, which it is called to adapt the training set.
This script writes a file called "predictions.npz" into the training-folder.

If you want to create more initial conditions than 20k, you can change the number of molecules to generate in the get\_initial\_conditions.sh script. Check the Sharc tutorial to sample more conformations. See https://sharc-md.org/wp-content/uploads/2019/10/SHARC_Tutorial.pdf
The frequency-file can be found in the "Inputfolder" folder. The files end with ".molden".

# 5) Adaptive sampling

Go to the directory "3\_AdaptiveSampling".


For adaptive sampling you need 4 files:
* geom
* veloc
* input
* run.sh


The geom, veloc and input files for the dynamics with SchNarc can be generated with SHARC. Please have a look at the SHARC tutorial on how to set up trajectories. You will have 10 folders already provided for the purpose of this tutorial that contain these files.
The run.sh file contains the commands for adaptive sampling.
You need at least two models to do adaptive sampling.

Go into each of the folders and execute the run.sh file. It will terminate when the error of the models is larger than 1 eV.

After the dynamics are done, please have a look at the jupyter notebook and find out how to get the geometries and sample data.

# Surface hopping dynamics

Go to the directory "4\_Dynamics".
For surface hopping dynamics you will need the same files as for adaptive sampling:
* geom
* veloc
* input
* run.sh


The geom, veloc and input files for the dynamics with SchNarc can be generated with SHARC. Please have a look at the SHARC tutorial on how to set up trajectories. You will have 10 folders already provided for the purpose of this tutorial that contain these files.
The run.sh file contains the commands for running dynamics with one ML model. Check the adaptive-sampling folder or Table 3 in the doi: to find out how to set more ML models. 

You can use the learned NACs, therefore go into the folder "LearnedNacs".
If you want to use approximated NACs based on Hessians, go in the folder "withHessian". 
Go into each of the folders and execute the run.sh file to run surface hopping dynamics of fulvene.

After the dynamics are done, please have a look at the SHARC tutorial to analyze them, e.g., to plot populations. Note that the used ML models are not final models and most probably will not report fully reliable dynamics yet.
