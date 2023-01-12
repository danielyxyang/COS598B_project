# -*- coding: utf-8 -*-
"""daniel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j3KFMY1p_Wdxq4DLYXbizZtzisuElf8P

# Setup
"""

import itertools
import math
import time
import os
import json
from collections import defaultdict
from tqdm.auto import tqdm

import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from sklearn import svm, linear_model, neural_network, pipeline, preprocessing, base

# ignore convergence warnings from sklearn
import warnings
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning, module="sklearn")

DEV = False

# define environment constants
COLAB = 0
ADROIT = 1
EULER = 2
ENV = COLAB

# set environment settings
if ENV == COLAB:
  OUTPUT_DIR = "/content/results"
  EXPERIMENT_BATCH_ID = None
elif ENV == ADROIT:
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("-o", "--out", help="specify output directory")
  parser.add_argument("-b", "--batch", help="specify experiment batch number", type=int)
  
  args = parser.parse_args()
  OUTPUT_DIR = args.out
  EXPERIMENT_BATCH_ID = args.batch

def json_serialize(obj):
  """
  Convert some non-serializable types into serializable ones to be stored in JSON format
  """
  if isinstance(obj, np.integer):
    return int(obj)
  if isinstance(obj, np.floating):
    return float(obj)
  if isinstance(obj, np.ndarray):
    return obj.tolist()
  if isinstance(obj, base.BaseEstimator):
    return obj.__class__.__name__
  return json.JSONEncoder().default(obj)

"""# Code base

## Definition of Shapley values
$$
s_i := \mathbb{E}_{\pi} [U(\pi_{\leq i}) - U(\pi_{< i})]
$$

## Computing Shapley values

**Approach 1**: sum marginal utilities over all possible permutations
$$
s_i = \frac{1}{n!} \sum_{\pi \in S_n} (U(\pi_{\leq i}) - U(\pi_{< i})) \text{ for all } i \in [n]
$$
- number of iterations: $n \cdot n! \in \Theta(n^{n+1})$
- number of utility evaluations (without memoization): $n \cdot n! \in \Theta(n^{n+1})$
- number of utility evaluations (with memoization): $\Theta(2^n)$ with $\Theta(2^n)$ space complexity

**Approach 2**: sum marginal utilities over all possible subsets weighted by probability of $S$ (i.e. $n$ possibilities for choosing $i$ and $\binom{n-1}{|S|}$ possibilities for choosing $|S|$)
$$
s_i = \sum_{S \subseteq [n] \setminus \{i\}} \frac{1}{n\binom{n-1}{|S|}}(U(S \cup \{i\}) - U(S)) \text{ for all } i \in [n]
$$
- number of iterations: $\Theta(n \cdot 2^n)$
- number of utility evaluations (with memoization): $\Theta(2^n)$ with $\Theta(2^n)$ space complexity

## Approximating Shapley values
...

## Class: Dataset
"""

class Dataset():
  def __init__(self, dataset):
    """
    Initialize wrapper class for dataset

    Args:
      dataset: list of (x, label)
    """
    self.dataset = dataset
    self.size = len(self.dataset)
    self.indices = list(range(self.size))
  
  def __call__(self, indices):
    """
    Create a dataset with a subset of datapoints according to the specified indices

    Args:
      indices: list of indices
    Returns:
      sub_dataset: Dataset object with a sublist of datapoints
    """
    sub_dataset = Dataset([self.dataset[i] for i in indices])
    return sub_dataset
  
  def to_matrix_form(self):
    """
    Convert the dataset to a feature matrix and label vector

    Returns:
      X: matrix of features with dimensions (n_samples, n_features)
      y: vector of labels with dimensions (n_samples)
    """
    n_samples = len(self.dataset)
    n_features = len(self.dataset[0][0])
    X = np.zeros((n_samples, n_features))
    y = np.zeros(n_samples)
    for i, (x, label) in enumerate(self.dataset):
      X[i,:] = x
      y[i] = label
    return X, y
  
  def save(self, folder, filename="dataset"):
    """
    Save the dataset in JSON format

    Args:
      folder: path to folder 
      filename: name of file
    """
    filepath = os.path.join(folder, filename)
    with open("{}.json".format(filepath), "w") as file:
      json.dump(self.dataset, file, indent=2, default=json_serialize)
  
  def get_params(self):
    """
    Return all relevant parameters for this class required for reproducability

    Returns:
      dictionary with all relevant parameters
    """
    return {}

"""## Class: Utility"""

class Utility():
  def __call__(self, dataset):
    return self.compute_utility(dataset)
  
  def compute_utility(self, dataset):
    """
    Compute the utility of the given datapoints

    Args:
      dataset: list of datapoints
    Returns:
      utility: utility of the given datapoints
    """
    pass
  
  def get_params(self):
    """
    Return all relevant parameters for this class required for reproducability

    Returns:
      dictionary with all relevant parameters
    """
    return {}

"""## Class: DataShapleySolver"""

class DataShapleySolver():
  def __init__(self, dataset, utility, seed=0):
    """
    Initialize class for computing Shapley values

    Args:
      dataset: object of class Dataset
      utility: object of class Utility
      seed: integer seed used for reproduceability
    """
    self.dataset = dataset
    self.utility = utility
    self.seed = seed

  def _reset(self, n_evals=None):
    """
    Reset solver before computing Shapley values

    Args:
      n_evals: total number of utility evaluations for the next computation (only required for progress bar)
    """
    self.utilities_computed = {}
    self.utility_eval_time = 0
    self.utility_eval_counter = 0
    self.utility_eval_counter_total = 0
    self.utility_eval_counter_pbar = tqdm(total=n_evals, desc="Utility evaluations", mininterval=1)
    self.shapley_values = np.zeros(self.dataset.size)

    if self.seed is not None:
      self.rng = np.random.default_rng(self.seed)
    else:
      self.rng = np.random.default_rng()

  def _utility_wrapper(self, subset_indices, memo=True, statistics=True):
    """
    Wrapper function around the given utility object to apply memoization and to record statistics

    Args:
      subset_indices: list of indices for which utility should be computed
      memo: boolean flag whether to apply memoization
      statistics: boolean flag whether to update statistics
    Returns:
      utility: computed utility for given subset indices
    """
    if statistics:
      self.utility_eval_counter_total += 1
      self.utility_eval_counter_pbar.update(1)
    # return trivial utility
    if len(subset_indices) == 0:
      return 0
    # return memoized utility
    subset_key = tuple(sorted(subset_indices))
    if memo and subset_key in self.utilities_computed:
      return self.utilities_computed[subset_key]
    # compute utility
    start = time.time()
    utility = self.utility(self.dataset(subset_indices))
    end = time.time()
    if statistics:
      self.utility_eval_time += end - start
      self.utility_eval_counter += 1
    # apply memoization (reduce number of utility evaluations) or skip memoization (reduce memory footprint)
    if memo:
      self.utilities_computed[subset_key] = utility
    # return computed utility
    return utility
  
  def _compute_shapley_with_subsets(self, memo=True):
    """
    Compute Shapley values exactly by computing marginal utility for all possible subsets

    Args:
      memo: boolean flag whether to apply memoization
    """
    # construct iterator over all subsets of size 0 to n-1
    subsets = itertools.chain.from_iterable(
        [itertools.combinations(self.dataset.indices, r) for r in range(self.dataset.size)]
    )
    n_subsets = 2**self.dataset.size - 1
    
    # initialize computation
    self._reset(n_evals=self.dataset.size * 2**self.dataset.size)
    # compute marginal utilities over all subsets
    for S in tqdm(subsets, total=n_subsets, desc="Loop 1", mininterval=1):
      # scan through all data points not in S
      factor = self.dataset.size * scipy.special.binom(self.dataset.size - 1, len(S))
      not_S = [index for index in self.dataset.indices if index not in S]
      for i in tqdm(not_S, desc="Loop 2", mininterval=2, delay=2, disable=len(not_S) < 500, leave=False):
        self.shapley_values[i] += (self._utility_wrapper(list(S) + [i], memo=memo) - self._utility_wrapper(list(S), memo=memo)) / factor
    # finish computation
    self.utility_eval_counter_pbar.close()

  def _compute_shapley_with_permutations(self, permutations, n_permutations, memo=True):
    """
    Compute or approximate Shapley values by computing marginal utility only for the given permutations

    Args:
      permutations: list or iterable object with a list of all possible permutations
      n_permutations: number of provided permutations
      memo: boolean flag whether to apply memoization
    """
    # initialize computation
    self._reset(n_evals=n_permutations * self.dataset.size)
    # compute marginal utilities over given permutations
    for permutation in tqdm(permutations, total=n_permutations, desc="Loop 1", mininterval=1):
      # scan through given permutation and accumulate marginal utilities
      utility = 0
      for end in tqdm(range(len(permutation)), desc="Loop 2", mininterval=2, delay=2, disable=len(permutation) < 500, leave=False):
        S = permutation[0:end]
        i = permutation[end]
        last_utility = utility
        utility = self._utility_wrapper(list(S) + [i], memo=memo)
        self.shapley_values[i] += utility - last_utility
    self.shapley_values = self.shapley_values / n_permutations
    # finish computation
    self.utility_eval_counter_pbar.close()
  
  def _sanity_check(self):
    """
    Sanity check computed Shapley values
    """
    # check efficiency property of Shapley values
    utility_total = sum(self.shapley_values)
    utility_expected = self._utility_wrapper(self.dataset.indices, statistics=False)
    error = abs(utility_total - utility_expected)
    if error > 1e-9:
      print("WARNING: sum of Shapley values {} different from expected total utility {} by {}".format(utility_total, utility_expected, error))

  def compute_shapley(self):
    """
    Compute Shapley values exactly
    """
    # compute marginal utilities over all subsets
    self._compute_shapley_with_subsets()
    self._sanity_check()

    # compute marginal utilities over all permutations
    # return self._compute_shapley_with_permutations(
    #     itertools.permutations(self.dataset.indices),
    #     math.factorial(self.dataset.size),
    # )
    # self._sanity_check()
  
  def approximate_shapley(self, n_permutations):
    """
    Approximate Shapley values with randomly sampled permutations

    Args:
      n_permutations: number of permutations to be sampled
    """
    if n_permutations > math.factorial(self.dataset.size):
      print("WARNING: using more samples than total number of possible permutations")
    
    def permutation_generator():
      for _ in range(n_permutations):
        yield self.rng.permutation(self.dataset.indices)

    # compute marginal utilities over permutation samples
    self._compute_shapley_with_permutations(
        permutation_generator(),
        n_permutations,
        memo=False,
    )
    self._sanity_check()
  
  def print_results(self):
    """
    Print computed Shapley values and statistics
    """
    print("Shapley values")
    print(self.shapley_values) if len(self.shapley_values) <= 30 else None
    print("    average:    {}".format(sum(self.shapley_values) / len(self.shapley_values)))
    print("    total:      {:.4f}".format(sum(self.shapley_values)))
    print("Number of evaluations")
    print("    actual:     {}".format(self.utility_eval_counter))
    print("    total:      {}".format(self.utility_eval_counter_total))
    print("Time of evaluations")
    print("    per eval:   {:.2f}s".format(self.utility_eval_time / self.utility_eval_counter))
    print("    total:      {:.2f}s".format(self.utility_eval_time))
  
  def save_shapley_values(self, folder, filename="shapley_values"):
    """
    Save the Shapley values in JSON format

    Args:
      folder: path to folder 
      filename: name of file
    """
    filepath = os.path.join(folder, filename)
    with open("{}.json".format(filepath), "w") as file:
      json.dump(self.shapley_values.tolist(), file, indent=2)
    
  def get_params(self):
    """
    Return all relevant parameters for this class required for reproducability

    Returns:
      dictionary with all relevant parameters
    """
    return {
        "seed": self.seed,
    }

"""## Functions: plotting"""

def plot_shapley_values(labels, shapley_values, title=None, cmap=None):
  # compute average Shapley value
  avg_sv = sum(shapley_values) / len(shapley_values)

  # group Shapley values based on labels
  shapley_values_grouped = defaultdict(lambda: ([],[]))
  for index, (label, sv) in enumerate(zip(labels, shapley_values)):
    shapley_values_grouped[label][0].append(str(index))
    shapley_values_grouped[label][1].append(sv)
  
  # plot Shapley values for each label separately
  num_labels = len(shapley_values_grouped)
  fig, axes = plt.subplots(1, num_labels, figsize=(4 * num_labels, 4), sharey=True, constrained_layout=True)
  for i, (label, (axis_labels, sv)) in enumerate(shapley_values_grouped.items()):
    sv, axis_labels = zip(*sorted(zip(sv, axis_labels))) # sort by shapley values
    axes[i].bar(axis_labels, sv, color=cmap[label] if cmap is not None else None)
    axes[i].axhline(avg_sv, color="grey", linestyle="--")
    axes[i].tick_params(axis="x", bottom=False, labelbottom=False) if len(axis_labels) > 15 else None
    axes[i].tick_params(axis="y", labelleft=True)
    axes[i].set_title(title)
  
  return fig

"""# Experiments with Gaussians

## Class ModelUtility
"""

class ModelUtility(Utility):
  def __init__(self, model_constructor, test_dataset):
    self.model_constructor = model_constructor
    self.test_dataset = test_dataset
    
  def compute_utility(self, subset):
    X_train, y_train = subset.to_matrix_form()
    X_test, y_test = self.test_dataset.to_matrix_form()
    
    if len(np.unique(y_train)) == 1: # assuming model always predicts y_train for datasets with only one class
      return np.sum(y_test == y_train[0]) / len(y_test)
    
    model = self.model_constructor().fit(X_train, y_train)
    mean_acc = model.score(X_test, y_test)

    return mean_acc
  
  def get_params(self):
    model = self.model_constructor()
    return {
        "model_name": model.__class__.__name__,
        "model": model.get_params(),
        **super().get_params(),
    }

"""## Class: GaussianDataset"""

class GaussianDataset(Dataset):
  def __init__(self, gaussians, cmap, sizes=100, seed=0):
    self.gaussians = gaussians
    self.cmap = cmap
    self.sizes = [sizes] * len(gaussians) if isinstance(sizes, int) else sizes
    self.seed = seed

    if self.seed is not None:
      rng = np.random.default_rng(seed)
    else:
      rng = np.random.default_rng()

    # sample n[i] data points from i-th gaussian
    datapoints = []
    for i, (label, gaussian) in enumerate(gaussians.items()):
      data = rng.multivariate_normal(gaussian["mean"], gaussian["cov"], self.sizes[i])
      labels = np.full(self.sizes[i], label)
      datapoints += list(zip(data, labels))

    super().__init__(datapoints)

  def _plot_data(self, axis, point_sizes):
    # scale relative point sizes by avg
    if not isinstance(point_sizes, np.ndarray):
      point_sizes = np.array(point_sizes)
    min, scale, max = 1, 10, 100
    point_sizes = np.clip(point_sizes * scale, min, max)

    # group data points based on labels
    dataset_grouped = defaultdict(lambda: ([],[]))
    for (x, label), size in zip(self.dataset, point_sizes):
      dataset_grouped[label][0].append(x)
      dataset_grouped[label][1].append(size)
    
    # plot data points for each label separately
    for label, (datapoints, sizes) in dataset_grouped.items():
      datapoints = np.array(datapoints)
      axis.scatter(datapoints[:,0], datapoints[:,1], label="label: {}".format(label), c=self.cmap[label], s=sizes)
    
    # fix size of markers in legend
    for handle in axis.legend().legendHandles:
      handle.set_sizes([scale])
    
  def _plot_gaussians(self, axis):
    for label, g in self.gaussians.items():
      l, v = np.linalg.eig(g["cov"])
      # plot shape of Gaussian (corresponding to standard deviation 1)
      axis.add_patch(Ellipse(
          xy=g["mean"],
          width=2 * np.sqrt(l[0]),
          height=2 * np.sqrt(l[1]),
          # angle=np.rad2deg(np.arccos(v[0, 0])),
          angle=np.rad2deg(np.arctan(v[1, 0] / v[0, 0])), # TODO (assuming first eigenvalue is largest?)
          edgecolor=self.cmap[label], facecolor="none", linestyle="--",
      ))
      # plot center of Gaussian
      axis.scatter(g["mean"][0], g["mean"][1], s=100, color=self.cmap[label], marker="+")

  def _plot_decision_region(self, axis, model, region, h=0.1):
    xx, yy = np.meshgrid(np.arange(region[0][0]-0.5, region[0][1]+0.5, h), np.arange(region[1][0]-0.5, region[1][1]+0.5, h))
    y_pred = model.predict(np.c_[xx.ravel(), yy.ravel()])
    y_pred = y_pred.reshape(xx.shape)
    colors = [self.cmap[label] for label in sorted(self.gaussians.keys())] # order colors by label
    axis.contourf(xx, yy, y_pred, colors=colors, alpha=0.1)

  def plot(self, dataset=True, gaussians=True, model=None, shapley_values=None, title=None):
    fig, axis = plt.subplots(figsize=(4, 4), constrained_layout=True)
    # plot dataset
    if dataset:
      if shapley_values is not None:
        avg_shapley_value = sum(shapley_values) / len(shapley_values)
        point_sizes = shapley_values / avg_shapley_value
      else:
        point_sizes = 0.5 * np.ones(self.size)
      self._plot_data(axis, point_sizes)
    # plot Gaussian contours
    if gaussians:
      self._plot_gaussians(axis)
    # plot decision regions of model
    if model is not None:
      self._plot_decision_region(axis, model, ((-6, 6), (-6, 6)))
    # set layout
    if title is not None:
      axis.set_title(title)
    axis.axis("equal")
    axis.set_xlim(-6, 6)
    axis.set_ylim(-6, 6)
    return fig
    
  def get_params(self):
    return {
        "gaussians": self.gaussians,
        "sizes": self.sizes,
        "seed": self.seed,
        **super().get_params(),
    }

if ENV == COLAB:
  gaussians = {
      1: {"mean": [-1.25, -1.25], "cov": [[4,2], [2,4]]},
      -1: {"mean": [1.25, 1.25], "cov": [[4,-2], [-2,4]]},
  }
  cmap = {1: "blue", -1: "red"}
  dataset = GaussianDataset(gaussians, cmap, sizes=10, seed=0)
  dataset.plot()
  dataset.plot(shapley_values=np.array(list(range(19)) + [1000]))
  print()

"""## Class: GaussianExperiment"""

class GaussianExperiment():
  def __init__(self, model_constructor, train_dataset_params, test_dataset_params, cmap, num_permutations=None, seed=0,
               name_batch=None, name_experiment="temp"):
    if seed is not None:
      rng = np.random.default_rng(seed)
    else:
      rng = np.random.default_rng()
    seeds = rng.integers(1000, size=3)
    
    self.train_dataset = GaussianDataset(train_dataset_params[0], cmap, sizes=train_dataset_params[1], seed=seeds[0])
    self.test_dataset = GaussianDataset(test_dataset_params[0], cmap, sizes=test_dataset_params[1], seed=seeds[1])
    self.utility = ModelUtility(model_constructor, self.test_dataset)
    self.solver = DataShapleySolver(self.train_dataset, self.utility, seed=seeds[2])
    
    self.num_permutations = num_permutations
    self.seed = seed
    self.experiment_type = "{}{}".format(self.__class__.__name__, "" if name_batch is None else "-{}".format(name_batch))
    self.experiment_name = "{}{}".format(name_experiment, "_exact" if self.num_permutations is None else "_approx{}".format(self.num_permutations))
    self.experiment = "{}/{}".format(self.experiment_type, self.experiment_name)
  
  def run(self, save_results=True):
    print("EXPERIMENT: {}".format(self.experiment))

    # compute Shapley values
    if self.num_permutations is None:
      self.solver.compute_shapley()
    else:
      self.solver.approximate_shapley(self.num_permutations)

    # print results
    self.solver.print_results()
    fig_dataset = self.train_dataset.plot(
        shapley_values=self.solver.shapley_values,
        model=self.utility.model_constructor().fit(*self.train_dataset.to_matrix_form()),
        title=self.experiment_name,
    )
    fig_shapley_values = plot_shapley_values(
        self.train_dataset.to_matrix_form()[1],
        self.solver.shapley_values,
        title=self.experiment_name,
        cmap=self.train_dataset.cmap,
    )
    if ENV == COLAB:
      plt.show()

    # save results
    if save_results:
      # setup results folder
      folder = os.path.join(OUTPUT_DIR, self.experiment_type, self.experiment_name)
      os.makedirs(folder, exist_ok=True)
      # save experiment parameters
      with open(os.path.join(folder, "parameters.json"), "w") as file:
        json.dump(self.get_params(), file, indent=2, default=json_serialize)
      # save datasets
      self.train_dataset.save(folder, filename="dataset_train")
      self.test_dataset.save(folder, filename="dataset_test")
      # save results
      self.solver.save_shapley_values(folder)
      fig_dataset.savefig(os.path.join(folder, "plot_dataset.png"), dpi=150)
      fig_shapley_values.savefig(os.path.join(folder, "plot_shapley_values.png"), dpi=150)
      print("Results saved to \"{}\"".format(folder))
    
    print()
  
  def get_params(self):
    return {
        "experiment": self.experiment,
        "seed": self.seed,
        "num_permutations": self.num_permutations,
        "dataset_train": self.train_dataset.get_params(),
        "dataset_test": self.test_dataset.get_params(),
        "utility": self.utility.get_params(),
        "solver": self.solver.get_params(),
    }

"""## Functions: experiment management

- **experiment**: computing Shapley value for one game formulation
- **experiment batch**: computing Shapley values for multiple "similar" game formulations (*executed in a single job on the cluster*)
"""

def get_experiment_batch(config, test_run=False):
  return [
      GaussianExperiment(
          model_constructor,
          (dataset["gaussians"], params["train_dataset_size"] if not test_run else 5),
          (dataset["gaussians"], params["test_dataset_size"] if not test_run else 100),
          dataset["cmap"],
          num_permutations=params["num_permutations"] if not test_run or params["num_permutations"] is None else 10,
          seed=seed,
          name_batch="{}-{}{}".format(config["batch_id"], config["batch_name"], "" if not test_run else "_dev"),
          name_experiment="{}-{}".format(i, model_name),
      ) for i, (dataset, params, (model_name, model_constructor), seed) in enumerate(itertools.product(
          config["datasets"],
          config["params"],
          config["model_constructors"].items(),
          config["seeds"],
      ))
  ]

def run_experiment_batch(experiment_batch, batch_id="unspecified"): 
  print("EXPERIMENT BATCH: {}".format(batch_id))
  print("Number of experiments: {}".format(len(experiment_batch)))
  print()
  for experiment in experiment_batch:
    experiment.run()
  print()

def run_experiment_batches(experiment_batches, batch_ids=None):
  if EXPERIMENT_BATCH_ID is not None:
    # run only specified experiment batch (from command line)
    run_experiment_batch(experiment_batches[EXPERIMENT_BATCH_ID], batch_id=EXPERIMENT_BATCH_ID)
  elif batch_ids is not None:
    # run only specified experiment batches (from parameters)
    for batch_id in batch_ids:
      run_experiment_batch(experiment_batches[batch_id], batch_id=batch_id)
  else:
    # run all experiment batches
    for i, batch in enumerate(experiment_batches):
      run_experiment_batch(batch, batch_id=i)

"""## Experiment 3"""

datasets = [
    {
        "gaussians": {
            1: {"mean": [-1.25, -1.25], "cov": [[4,2], [2,4]]},
            -1: {"mean": [1.25, 1.25], "cov": [[4,-2], [-2,4]]},
        },
        "cmap": {1: "blue", -1: "red"},
    },
]
model_constructors = {
    "LogisticRegression": lambda: pipeline.make_pipeline(preprocessing.StandardScaler(), linear_model.LogisticRegression()),
    "LinearSVC": lambda: pipeline.make_pipeline(preprocessing.StandardScaler(), svm.LinearSVC()),
    "SVC_rbf": lambda: svm.SVC(kernel='rbf', gamma=0.7),
    "MLPClassifier": lambda: pipeline.make_pipeline(preprocessing.StandardScaler(), neural_network.MLPClassifier(hidden_layer_sizes=(10, 10), solver='lbfgs', random_state=1)),
}

experiment_batch1 = { # 12 experiments, exact, different seeds
    "batch_id": 1,
    "batch_name": "size10_exact",
    "model_constructors": model_constructors,
    "datasets": datasets,
    "params": [
        {"train_dataset_size": 10, "test_dataset_size": 100, "num_permutations": None},
    ],
    "seeds": [
        0,
        1,
        2,
    ],
}

experiment_batch2 = { # 12 computations, approx, different num_permutations
    "batch_id": 2,
    "batch_name": "size100_approx",
    "model_constructors": model_constructors,
    "datasets": datasets,
    "params": [
        {"train_dataset_size": 100, "test_dataset_size": 1000, "num_permutations": 200},
        {"train_dataset_size": 100, "test_dataset_size": 1000, "num_permutations": 400},
        {"train_dataset_size": 100, "test_dataset_size": 1000, "num_permutations": 600},
    ],
    "seeds": [
        0,
    ],
}

experiment_batch3 = {
    "batch_id": 3,
    "batch_name": "size6_exact",
    "model_constructors": model_constructors,
    "datasets": datasets,
    "params": [
        {"train_dataset_size": 6, "test_dataset_size": 100, "num_permutations": None},
    ],
    "seeds": [
        0,
        1,
        2,
    ],
}

experiment_batch4 = {
    "batch_id": 4,
    "batch_name": "size8_exact",
    "model_constructors": model_constructors,
    "datasets": datasets,
    "params": [
        {"train_dataset_size": 8, "test_dataset_size": 100, "num_permutations": None},
    ],
    "seeds": [
        0,
        1,
        2,
    ],
}

experiment_batch5 = {
    "batch_id": 5,
    "batch_name": "size100_200_approx",
    "model_constructors": model_constructors,
    "datasets": datasets,
    "params": [
        {"train_dataset_size": 100, "test_dataset_size": 1000, "num_permutations": 460},
        {"train_dataset_size": 200, "test_dataset_size": 1000, "num_permutations": 1060},
    ],
    "seeds": [
        0,
    ],
}

experiment_batch6 = {
    "batch_id": 6,
    "batch_name": "size400_approx",
    "model_constructors": model_constructors,
    "datasets": datasets,
    "params": [
        {"train_dataset_size": 400, "test_dataset_size": 1000, "num_permutations": 2400},
    ],
    "seeds": [
        0,
    ],
}

experiment_batch_dev = {
    "batch_id": 0,
    "batch_name": "dev",
    "model_constructors": {
        "LinearSVC": lambda: pipeline.make_pipeline(preprocessing.StandardScaler(), svm.LinearSVC()),
    },
    "datasets": datasets,
    "params": [
        {"train_dataset_size": 5, "test_dataset_size": 100, "num_permutations": None},
    ],
    "seeds": [
        0,
    ],
}

experiment_batches = [
    get_experiment_batch(experiment_batch_dev), # index 0 = dev experiments
    get_experiment_batch(experiment_batch1, test_run=DEV),
    get_experiment_batch(experiment_batch2, test_run=DEV),
    get_experiment_batch(experiment_batch3, test_run=DEV),
    get_experiment_batch(experiment_batch4, test_run=DEV),
    get_experiment_batch(experiment_batch5, test_run=DEV),
    get_experiment_batch(experiment_batch6, test_run=DEV),
]
run_experiment_batches(experiment_batches)

"""## Experiment 2"""

# datasets = [
#     {
#         "gaussians": {
#             1: {"mean": [-2, 2], "cov": [[4, 2], [2, 4]]},
#             -1: {"mean": [2, -2], "cov": [[4, 2], [2, 4]]},
#         },
#         "cmap": {1: "blue", -1: "red"},
#     },
# ]
# model_constructors = {
#     "LogisticRegression": lambda: pipeline.make_pipeline(preprocessing.StandardScaler(), linear_model.LogisticRegression()),
#     "LinearSVC": lambda: pipeline.make_pipeline(preprocessing.StandardScaler(), svm.LinearSVC()),
#     "SVC_rbf": lambda: svm.SVC(kernel='rbf', gamma=0.7),
#     "MLPClassifier": lambda: pipeline.make_pipeline(preprocessing.StandardScaler(), neural_network.MLPClassifier(hidden_layer_sizes=(10, 10), solver='lbfgs', random_state=1)),
# }

# experiment_batch1 = { # 12 experiments, exact, different seeds
#     "tag": "1_size10_exact",
#     "model_constructors": model_constructors,
#     "datasets": datasets,
#     "params": [
#         {"train_dataset_size": 10, "test_dataset_size": 100, "num_permutations": None},
#     ],
#     "seeds": [
#         0,
#         1,
#         2,
#     ],
# }

# experiment_batch2 = { # 12 computations, approx, different num_permutations
#     "tag": "2_size100_approx",
#     "model_constructors": model_constructors,
#     "datasets": datasets,
#     "params": [
#         {"train_dataset_size": 100, "test_dataset_size": 1000, "num_permutations": 200},
#         {"train_dataset_size": 100, "test_dataset_size": 1000, "num_permutations": 400},
#         {"train_dataset_size": 100, "test_dataset_size": 1000, "num_permutations": 600},
#     ],
#     "seeds": [
#         0,
#     ],
# }

# experiment_batch3 = {
#     "tag": "3_size6_exact",
#     "model_constructors": model_constructors,
#     "datasets": datasets,
#     "params": [
#         {"train_dataset_size": 6, "test_dataset_size": 100, "num_permutations": None},
#     ],
#     "seeds": [
#         0,
#         1,
#         2,
#     ],
# }

# experiment_batch4 = {
#     "tag": "4_size8_exact",
#     "model_constructors": model_constructors,
#     "datasets": datasets,
#     "params": [
#         {"train_dataset_size": 8, "test_dataset_size": 100, "num_permutations": None},
#     ],
#     "seeds": [
#         0,
#         1,
#         2,
#     ],
# }

# experiment_batch5 = {
#     "tag": "5_size100_200_approx",
#     "model_constructors": model_constructors,
#     "datasets": datasets,
#     "params": [
#         {"train_dataset_size": 100, "test_dataset_size": 1000, "num_permutations": 460},
#         {"train_dataset_size": 200, "test_dataset_size": 1000, "num_permutations": 1060},
#     ],
#     "seeds": [
#         0,
#     ],
# }

# experiment_batch6 = {
#     "tag": "6_size400_approx",
#     "model_constructors": model_constructors,
#     "datasets": datasets,
#     "params": [
#         {"train_dataset_size": 400, "test_dataset_size": 1000, "num_permutations": 2400},
#     ],
#     "seeds": [
#         0,
#     ],
# }

# experiment_batches = [
#     [], # index 0 = dev experiments
#     get_experiment_batch(experiment_batch1, test_run=DEV),
#     get_experiment_batch(experiment_batch2, test_run=DEV),
#     get_experiment_batch(experiment_batch3, test_run=DEV),
#     get_experiment_batch(experiment_batch4, test_run=DEV),
#     get_experiment_batch(experiment_batch5, test_run=DEV),
#     get_experiment_batch(experiment_batch6, test_run=DEV),
# ]
# run_experiment_batches(experiment_batches)

"""## Experiment 1"""

# datasets = [
#     {
#         "gaussians": {
#             1: {"mean": [-1, 1], "cov": [[4, 2], [2, 4]]},
#             -1: {"mean": [1, -1], "cov": [[4, 2], [2, 4]]},
#         },
#         "cmap": {1: "blue", -1: "red"},
#     },
# ]
# model_constructors = {
#     "LogisticRegression": lambda: pipeline.make_pipeline(preprocessing.StandardScaler(), linear_model.LogisticRegression()),
#     "LinearSVC": lambda: pipeline.make_pipeline(preprocessing.StandardScaler(), svm.LinearSVC()),
#     "SVC_rbf": lambda: svm.SVC(kernel='rbf', gamma=0.7),
#     "MLPClassifier": lambda: pipeline.make_pipeline(preprocessing.StandardScaler(), neural_network.MLPClassifier(hidden_layer_sizes=(10, 10), solver='lbfgs', random_state=1)),
# }

# experiment_batch1 = { # 12 experiments, exact, different seeds
#     "tag": "1_size10_exact",
#     "model_constructors": model_constructors,
#     "datasets": datasets,
#     "params": [
#         {"train_dataset_size": 10, "test_dataset_size": 100, "num_permutations": None},
#     ],
#     "seeds": [
#         0,
#         1,
#         2,
#     ],
# }

# experiment_batch2 = { # 12 computations, approx, different num_permutations
#     "tag": "2_size100_approx",
#     "model_constructors": model_constructors,
#     "datasets": datasets,
#     "params": [
#         {"train_dataset_size": 100, "test_dataset_size": 1000, "num_permutations": 200},
#         {"train_dataset_size": 100, "test_dataset_size": 1000, "num_permutations": 400},
#         {"train_dataset_size": 100, "test_dataset_size": 1000, "num_permutations": 600},
#     ],
#     "seeds": [
#         0,
#     ],
# }

# experiment_batch3 = {
#     "tag": "3_size6_exact",
#     "model_constructors": model_constructors,
#     "datasets": datasets,
#     "params": [
#         {"train_dataset_size": 6, "test_dataset_size": 100, "num_permutations": None},
#     ],
#     "seeds": [
#         0,
#         1,
#         2,
#     ],
# }

# experiment_batch4 = {
#     "tag": "4_size8_exact",
#     "model_constructors": model_constructors,
#     "datasets": datasets,
#     "params": [
#         {"train_dataset_size": 8, "test_dataset_size": 100, "num_permutations": None},
#     ],
#     "seeds": [
#         0,
#         1,
#         2,
#     ],
# }

# experiment_batch5 = {
#     "tag": "5_size100_200_approx",
#     "model_constructors": model_constructors,
#     "datasets": datasets,
#     "params": [
#         {"train_dataset_size": 100, "test_dataset_size": 1000, "num_permutations": 460},
#         {"train_dataset_size": 200, "test_dataset_size": 1000, "num_permutations": 1060},
#     ],
#     "seeds": [
#         0,
#     ],
# }

# experiment_batch6 = {
#     "tag": "6_size400_approx",
#     "model_constructors": model_constructors,
#     "datasets": datasets,
#     "params": [
#         {"train_dataset_size": 400, "test_dataset_size": 1000, "num_permutations": 2400},
#     ],
#     "seeds": [
#         0,
#     ],
# }

# experiment_batches = [
#     [], # index 0 = dev experiments
#     get_experiment_batch(experiment_batch1, test_run=DEV),
#     get_experiment_batch(experiment_batch2, test_run=DEV),
#     get_experiment_batch(experiment_batch3, test_run=DEV),
#     get_experiment_batch(experiment_batch4, test_run=DEV),
#     get_experiment_batch(experiment_batch5, test_run=DEV),
#     get_experiment_batch(experiment_batch6, test_run=DEV),
# ]
# run_experiment_batches(experiment_batches)

"""# Toy example"""

# # example taken from https://www.analyticsvidhya.com/blog/2019/11/shapley-value-machine-learning-interpretability-game-theory/
# class ToyUtility(Utility):
#   def __init__(self):
#     self.utilities = {
#         ("Abhiraj",): 560,
#         ("Pranav",): 700,
#         ("Ram",): 800,
#         ("Abhiraj", "Pranav",): 720,
#         ("Abhiraj", "Ram",): 800,
#         ("Pranav", "Ram",): 850,
#         ("Abhiraj", "Pranav", "Ram",): 900,
#     }
    
#   def compute_utility(self, subset):
#     return self.utilities[tuple(sorted(subset.dataset))]

# dataset = Dataset(["Ram", "Abhiraj", "Pranav"], None)
# utility = ToyUtility()
# solver = DataShapleySolver(dataset, utility)

# solver.compute_shapley()
# solver.print_results()

# solver.approximate_shapley(n_permutations=1000)
# solver.print_results()