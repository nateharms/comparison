#!/bin/bash
#SBATCH --job-name=port8173
#SBATCH --output=output.log
#SBATCH --error=error.log
#SBATCH -n1

python -m cProfile -o importChemkin.profile $RMGpy/importChemkin.py  \
	--species model.txt \
	--reactions model.txt \
	--thermo thermo.txt \
	--known SMILES.txt \
	--port 8173
gprof2dot -f pstats  importChemkin.profile | dot -Tpdf -o importChemkin.profile.pdf
