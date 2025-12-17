# Surface hopping dynamics
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
