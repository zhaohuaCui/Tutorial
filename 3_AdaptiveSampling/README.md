# Adaptive sampling
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
