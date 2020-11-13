#%%
import sys, os
import logging, multiprocessing
from pyteck.eval_model import evaluate_model
import numpy as np

## Setting appropirate paths
current_dir = os.getcwd()
scratch = "/scratch/harms.n/comparison-scratch"


#%%
## Getting the Job Number
if os.getenv('SLURM_ARRAY_TASK_ID'):
    i = int(os.getenv('SLURM_ARRAY_TASK_ID'))
else:
    logging.warning("Number not specified as script argument or via environment variable, so using default")
    i = 23
logging.info("RUNNING WITH JOB NUMBER i = {}".format(i))
logging.info("Running on a node with {} processors".format(multiprocessing.cpu_count()))

#%%
fuels = ['butanol', 'heptane', 'methylheptane']
for fuel in fuels:

    model_path = os.path.join(current_dir, '..', 'alternatives', fuel)
    models = np.array([f for f in os.listdir(model_path) if f not in ['.ipynb_checkpoints', 'master.cti']])
    if i == 833:
        model_to_run = os.path.join(model_path, 'master.cti')
    else:
        try:
            model_to_run = models[list(map(lambda x: int(x.split('.')[1]) == i-1, models ))][0]
        except IndexError:
            print(f'For {fuel}, there was no model created... skipping...')
            continue

    data_path = os.path.join(current_dir,"data", fuel)
    data_list = os.path.join(current_dir, f"{fuel}-dataset.txt")
    species_key = os.path.join(current_dir, f"{fuel}-species.txt")

    os.makedirs(os.path.join(scratch, model_to_run.strip(".cti")), exist_ok=True)
    os.chdir(os.path.join(scratch, model_to_run.strip(".cti")))

    if not os.path.exists(os.path.join(scratch, model_to_run.strip('.cti'), model_to_run.replace('.cti', '-results.yaml'))):
        print(f'We are in the current directory: {os.getcwd()}')

        output = evaluate_model(
            model_to_run, 
            spec_keys_file=species_key,
            dataset_file=data_list, 
            data_path=data_path,
            model_path=model_path,
            skip_validation=True
        )
    else:
        print(f'We already have results for {model_to_run} model')

    print('#'*50)
    print(f'## Done with {os.path.join(scratch, model_to_run.strip(".cti"))}')