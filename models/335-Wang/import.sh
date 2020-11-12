#!/bin/bash
#SBATCH --job-name=port8140
#BSUB -o output.log
#BSUB -e error.log
#SBATCH -n1
# Run under a profiler

python -m cProfile -o importChemkin.profile $RMGpy/importChemkin.py  \
	--species mechanism.txt \
	--reactions mechanism.txt \
	--thermo thermo.txt \
	--known SMILES.txt \
	--port 8140
gprof2dot -f pstats  importChemkin.profile | dot -Tpdf -o importChemkin.profile.pdf
