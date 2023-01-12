
if [ "$#" -lt 1 ]; then
    echo "Usage: submit_job.sh [submission file] {experiment_dir} {experiments} {runtime} {num_cores} {mem} {prev_job_id}"
    exit
fi

source /etc/profile.d/modules.sh # get user environment (propagated by sbatch to start_job.sh)

experiment_name=${2:-"TEMP"}
experiments=${3:-0}
prev_job_id=${7:-"-"}

timestamp=$(date "+%Y%m%d-%H%M%S")
out="/scratch/network/dy8451/$experiment_name/$timestamp"
submission_file="$out/$(basename $1)"

runtime=${4:-"04:00:00"}
num_cores=${5:-1}
mem=${6:-4096}

mkdir -p $out # create output directory
cp $1 $out # copy submission file to output directory (to avoid subsequent changes)
chmod ugo-w $submission_file # make submission file read-only

echo
echo "Experiment name:  $experiment_name"
echo "Experiments:      $experiments"
echo "Waiting for:      $prev_job_id"
echo
echo "Submission:       \"$submission_file\""
echo "Output directory: \"$out\""
echo "Resources:        runtime=$runtime, num_cores=$num_cores, total_mem=$((num_cores*mem))"
echo

if [ "$prev_job_id" = "-" ]; then
    sbatch --array=$experiments --time=$runtime --nodes=1 --ntasks=1 --cpus-per-task=$num_cores --mem-per-cpu=$mem --job-name="${experiment_name}_${experiments}" --output="$out/slurm-%A-%a.out.txt" --mail-type="end,fail" --mail-user="dy8451@princeton.edu" start_job.sh $submission_file $out 
else
    sbatch --array=$experiments --time=$runtime --nodes=1 --ntasks=1 --cpus-per-task=$num_cores --mem-per-cpu=$mem --job-name="${experiment_name}_${experiments}" --output="$out/slurm-%A-%a.out.txt" --mail-type="end,fail" --mail-user="dy8451@princeton.edu" --dependency="aftercorr:${prev_job_id}" start_job.sh $submission_file $out 
fi
