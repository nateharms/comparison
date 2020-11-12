#%%
import os, sys
import pickle 
import pandas as pd 
import numpy as np
# %%
f = open('kinetics.pkl', 'rb')
kinetics = pickle.load(f)
# %%
# Finding reactions that are present in all of these models
df = pd.DataFrame(kinetics).T[['CombFlame2012/2028-Sarathy', 'n-Heptane', 'PCI2013/335-Wang']]
df.dropna(how='all', inplace=True)
# %%

# Removing reactions that are not A+B <=> C+D at most
def is_less_than_bimolecular(reaction):
    return len(reaction.reactants) <= 2 and len(reaction.products) <= 2

df = df[df.index.map(is_less_than_bimolecular)]

# %%
# Finding all "AutoTST"-able reactions
from autotst.reaction import Reaction
def match_to_autotst(reaction):
    try:
        r = Reaction(rmg_reaction=reaction)
        r.get_labeled_reaction()
        return True
    except AssertionError:
        return False
match = np.vectorize(match_to_autotst)

df = df[match(df.index)]
# %%
# Sorting the reactions by weight
def get_weight(reaction):
    return sum([r.molecular_weight.value for r in reaction.reactants])

weight = np.vectorize(get_weight)
df['weight'] = weight(df.index)

df.sort_values('weight', inplace=True)
# %%
reactions_to_run = df.index.to_numpy()
np.save('autotst-reactions',reactions_to_run)

# %%
