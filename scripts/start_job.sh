#!/bin/sh

echo
echo "Batch ID:                $SLURM_ARRAY_TASK_ID"
echo "Submission file:         $1"
echo "Output directory:        $2"
echo

module purge
module load anaconda3/2021.11

python $1 --out $2 --batch $SLURM_ARRAY_TASK_ID
