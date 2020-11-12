#!/bin/bash
#SBATCH --job-name=port8086
#SBATCH --output=output.log
#SBATCH --error=error.log
#SBATCH -n1

python -m cProfile -o importChemkin.profile $RMGpy/importChemkin.py  \
	--species nc7_ver3.1_mech.txt \
	--reactions nc7_ver3.1_mech.txt \
	--thermo n_heptane_v3.1_therm.dat \
	--known SMILES.txt \
	--port 8086
gprof2dot -f pstats  importChemkin.profile | dot -Tpdf -o importChemkin.profile.pdf

