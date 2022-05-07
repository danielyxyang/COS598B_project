# COS598 - Final Project
## Results of `experimentA4`

### Setup
- Dataset
    - Gaussian 1: $\mu_1 = \begin{pmatrix}1 \\ -1\end{pmatrix}$ and $\Sigma_1 = V_1 \Lambda_1 V_1^T$ with $\Lambda_1 = \begin{pmatrix}3 & 0 \\ 0 & 1\end{pmatrix}$ and $V_1 = \begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}$
    - Gaussian 2: $\mu_2 = \begin{pmatrix}-1 \\ 1\end{pmatrix}$ and $\Sigma_2 = V_2 \Lambda_2 V_2^T$ with $\Lambda_2 = \begin{pmatrix}3 & 0 \\ 0 & 1\end{pmatrix}$ and $V_2 = \begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}$
- Models
    - MLPClassifier with (10, 10) layers, random_state 1 (MLP1)
    - MLPClassifier with (10, 10) layers, random_state 2 (MLP2)
    - MLPClassifier with (10, 10) layers, random_state 3 (MLP3)
    - MLPClassifier with (10, 10) layers, random_state 4 (MLP4)

### Hypothesis
TBD

### Approximate Shapley values

\#| \| |size train|size test|num perm|seed| \| |size total|num eval| \| |MLP1|MLP2|MLP3|MLP4
-| - |-|-|-|-| - |-|-| - |-|-|-|-
1-size100_approx| \| |**100**|1000|**460**|0| \| |200|92K| \| |0.7744 / 2:24:28|0.7802 / 2:24:53|0.7300 / 2:23:50|0.7338 / 2:22:15
2-size200_approx| \| |**200**|1000|**1060**|0| \| |400|424K| \| |0.7935 / 10:16:59|0.8096 / 10:25:40|0.7973 / 10:10:22|0.7900 / 10:10:43

#### GaussianExperimentA-1-size100_approx
<img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier1-approx460/plot_dataset.png" width="200" alt="0-MLPClassifier1-approx460"><img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier2-approx460/plot_dataset.png" width="200" alt="0-MLPClassifier2-approx460"><img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier3-approx460/plot_dataset.png" width="200" alt="0-MLPClassifier3-approx460"><img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier4-approx460/plot_dataset.png" width="200" alt="0-MLPClassifier4-approx460">

<img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier1-approx460/plot_dataset_splitted.png" width="200" alt="0-MLPClassifier1-approx460"><img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier2-approx460/plot_dataset_splitted.png" width="200" alt="0-MLPClassifier2-approx460"><img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier3-approx460/plot_dataset_splitted.png" width="200" alt="0-MLPClassifier3-approx460"><img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier4-approx460/plot_dataset_splitted.png" width="200" alt="0-MLPClassifier4-approx460">

<img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier1-approx460/plot_shapley_values.png" width="200" alt="0-MLPClassifier1-approx460"><img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier2-approx460/plot_shapley_values.png" width="200" alt="0-MLPClassifier2-approx460"><img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier3-approx460/plot_shapley_values.png" width="200" alt="0-MLPClassifier3-approx460"><img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier4-approx460/plot_shapley_values.png" width="200" alt="0-MLPClassifier4-approx460">

<img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier1-approx460/plot_shapley_values_sorted.png" width="200" alt="0-MLPClassifier1-approx460"><img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier2-approx460/plot_shapley_values_sorted.png" width="200" alt="0-MLPClassifier2-approx460"><img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier3-approx460/plot_shapley_values_sorted.png" width="200" alt="0-MLPClassifier3-approx460"><img src="GaussianExperimentA-1-size100_approx/0-MLPClassifier4-approx460/plot_shapley_values_sorted.png" width="200" alt="0-MLPClassifier4-approx460">

#### GaussianExperimentA-2-size200_approx
<img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier1-approx1060/plot_dataset.png" width="200" alt="0-MLPClassifier1-approx1060"><img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier2-approx1060/plot_dataset.png" width="200" alt="0-MLPClassifier2-approx1060"><img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier3-approx1060/plot_dataset.png" width="200" alt="0-MLPClassifier3-approx1060"><img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier4-approx1060/plot_dataset.png" width="200" alt="0-MLPClassifier4-approx1060">

<img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier1-approx1060/plot_dataset_splitted.png" width="200" alt="0-MLPClassifier1-approx1060"><img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier2-approx1060/plot_dataset_splitted.png" width="200" alt="0-MLPClassifier2-approx1060"><img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier3-approx1060/plot_dataset_splitted.png" width="200" alt="0-MLPClassifier3-approx1060"><img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier4-approx1060/plot_dataset_splitted.png" width="200" alt="0-MLPClassifier4-approx1060">

<img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier1-approx1060/plot_shapley_values.png" width="200" alt="0-MLPClassifier1-approx1060"><img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier2-approx1060/plot_shapley_values.png" width="200" alt="0-MLPClassifier2-approx1060"><img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier3-approx1060/plot_shapley_values.png" width="200" alt="0-MLPClassifier3-approx1060"><img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier4-approx1060/plot_shapley_values.png" width="200" alt="0-MLPClassifier4-approx1060">

<img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier1-approx1060/plot_shapley_values_sorted.png" width="200" alt="0-MLPClassifier1-approx1060"><img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier2-approx1060/plot_shapley_values_sorted.png" width="200" alt="0-MLPClassifier2-approx1060"><img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier3-approx1060/plot_shapley_values_sorted.png" width="200" alt="0-MLPClassifier3-approx1060"><img src="GaussianExperimentA-2-size200_approx/0-MLPClassifier4-approx1060/plot_shapley_values_sorted.png" width="200" alt="0-MLPClassifier4-approx1060">
