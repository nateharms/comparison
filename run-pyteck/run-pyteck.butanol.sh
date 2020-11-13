#!/bin/sh
##set a job name
#SBATCH --job-name=run-pyteck.butanol

##a file for job output, you can check job progress
#SBATCH --output=log-files/butanol/pyteck.%a.slurm.log

## a file for errors from the job
#SBATCH --error=log-files/butanol/pyteck.%a.slurm.log

#SBATCH -N 1
#SBATCH -n 20
#SBATCH --partition=west,short
#SBATCH --mem=100GB
## 701 because we run the master model as well
#SBATCH --array=1-832
##SBATCH --array=1-6
## we missed 6 models
#SBATCH --exclude=c5003
#SBATCH --time 8:00:00
source $HOME/.bashrc
export PATH='/home/harms.n/anaconda2/envs/rmg3/bin':$PATH
echo $PATH
export HDF5_USE_FILE_LOCKING=FALSE
python run-pyteck.butanol.py
