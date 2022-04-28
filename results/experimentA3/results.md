# COS598 - Final Project
## Results of `experimentA3`

### Setup
- Dataset
    - Gaussian 1: $\mu_1 = \begin{pmatrix}1.25 \\ -1.25\end{pmatrix}$ and $\Sigma_1 = V_1 \Lambda_1 V_1^T$ with $\Lambda_1 = \begin{pmatrix}3 & 0 \\ 0 & 1\end{pmatrix}$ and $V_1 = \begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}$
    - Gaussian 2: $\mu_2 = \begin{pmatrix}-1.25 \\ 1.25\end{pmatrix}$ and $\Sigma_2 = V_2 \Lambda_2 V_2^T$ with $\Lambda_2 = \begin{pmatrix}3 & 0 \\ 0 & 1\end{pmatrix}$ and $V_2 = \begin{pmatrix}1 & 1 \\ -1 & 1\end{pmatrix}$
- Models
    - LogisticRegression (LR)
    - LinearSVC (SVC_lin)
    - SVC with RBF kernel (SVC_rbf)
    - MLPClassifier with (10, 10) layers (MLP)

### Exact Shapley values

\#| \| |size train|size test|num perm|seed| \| |size total|num eval| \| |LR|SVC_lin|SVC_rbf|MLP
-| - |-|-|-|-| - |-|-| - |-|-|-|-
3-size6_exact| \| |6|100|None|**0**| \| |12|50K| \| |0.8300 / 00:10|0.8100 / 00:05|0.5900 / 00:03|0.7000 / 00:52
3-size6_exact| \| |6|100|None|**1**| \| |12|50K| \| |0.8250 / 00:10|0.8250 / 00:05|0.6700 / 00:03|0.7400 / 00:47
3-size6_exact| \| |6|100|None|**2**| \| |12|50K| \| |0.7700 / 00:10|0.7750 / 00:05|0.5850 / 00:03|0.7100 / 00:27
4-size8_exact| \| |8|100|None|**0**| \| |16|1M| \| |0.7600 / 02:56|0.7550 / 01:20|0.5850 / 00:52|0.5150 / 16:21
4-size8_exact| \| |8|100|None|**1**| \| |16|1M| \| |0.8350 / 02:41|0.8400 / 01:20|0.6800 / 00:51|0.6800 / 09:23
4-size8_exact| \| |8|100|None|**2**| \| |16|1M| \| |0.7950 / 02:44|0.7400 / 01:20|0.7150 / 00:52|0.7000 / 06:27
1-size10_exact| \| |10|100|None|**0**| \| |20|20M| \| |0.7950 / 43:23|0.7900 / 21:31|0.6250 / 14:24|0.6850 / 6:38:18
1-size10_exact| \| |10|100|None|**1**| \| |20|20M| \| |0.8650 / 42:33|0.8600 / 21:32|0.7200 / 14:24|0.6500 / 4:12:13
1-size10_exact| \| |10|100|None|**2**| \| |20|20M| \| |0.7600 / 43:38|0.7450 / 21:28|0.7000 / 14:19|0.6900 / 2:20:14

#### GaussianExperiment-3-size6_exact
##### seed 0
<img src="GaussianExperiment-3-size6_exact/0-LogisticRegression_exact/plot_dataset.png" width="200" alt="0-LogisticRegression_exact"><img src="GaussianExperiment-3-size6_exact/3-LinearSVC_exact/plot_dataset.png" width="200" alt="3-LinearSVC_exact"><img src="GaussianExperiment-3-size6_exact/6-SVC_rbf_exact/plot_dataset.png" width="200" alt="6-SVC_rbf_exact"><img src="GaussianExperiment-3-size6_exact/9-MLPClassifier_exact/plot_dataset.png" width="200" alt="9-MLPClassifier_exact">

<img src="GaussianExperiment-3-size6_exact/0-LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="0-LogisticRegression_exact"><img src="GaussianExperiment-3-size6_exact/3-LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="3-LinearSVC_exact"><img src="GaussianExperiment-3-size6_exact/6-SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="6-SVC_rbf_exact"><img src="GaussianExperiment-3-size6_exact/9-MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="9-MLPClassifier_exact">

<img src="GaussianExperiment-3-size6_exact/0-LogisticRegression_exact/plot_shapley_values.png" width="200" alt="0-LogisticRegression_exact"><img src="GaussianExperiment-3-size6_exact/3-LinearSVC_exact/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact"><img src="GaussianExperiment-3-size6_exact/6-SVC_rbf_exact/plot_shapley_values.png" width="200" alt="6-SVC_rbf_exact"><img src="GaussianExperiment-3-size6_exact/9-MLPClassifier_exact/plot_shapley_values.png" width="200" alt="9-MLPClassifier_exact">

<img src="GaussianExperiment-3-size6_exact/0-LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="0-LogisticRegression_exact"><img src="GaussianExperiment-3-size6_exact/3-LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="3-LinearSVC_exact"><img src="GaussianExperiment-3-size6_exact/6-SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="6-SVC_rbf_exact"><img src="GaussianExperiment-3-size6_exact/9-MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="9-MLPClassifier_exact">

##### seed 1
<img src="GaussianExperiment-3-size6_exact/1-LogisticRegression_exact/plot_dataset.png" width="200" alt="_LogisticRegression_exact"><img src="GaussianExperiment-3-size6_exact/4-LinearSVC_exact/plot_dataset.png" width="200" alt="_LinearSVC_exact"><img src="GaussianExperiment-3-size6_exact/7-SVC_rbf_exact/plot_dataset.png" width="200" alt="_SVC_rbf_exact"><img src="GaussianExperiment-3-size6_exact/10-MLPClassifier_exact/plot_dataset.png" width="200" alt="_MLPClassifier_exact">

<img src="GaussianExperiment-3-size6_exact/1-LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="_LogisticRegression_exact"><img src="GaussianExperiment-3-size6_exact/4-LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="_LinearSVC_exact"><img src="GaussianExperiment-3-size6_exact/7-SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="_SVC_rbf_exact"><img src="GaussianExperiment-3-size6_exact/10-MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="_MLPClassifier_exact">

<img src="GaussianExperiment-3-size6_exact/1-LogisticRegression_exact/plot_shapley_values.png" width="200" alt="1-LogisticRegression_exact"><img src="GaussianExperiment-3-size6_exact/4-LinearSVC_exact/plot_shapley_values.png" width="200" alt="4-LinearSVC_exact"><img src="GaussianExperiment-3-size6_exact/7-SVC_rbf_exact/plot_shapley_values.png" width="200" alt="7-SVC_rbf_exact"><img src="GaussianExperiment-3-size6_exact/10-MLPClassifier_exact/plot_shapley_values.png" width="200" alt="10-MLPClassifier_exact">

<img src="GaussianExperiment-3-size6_exact/1-LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="1-LogisticRegression_exact"><img src="GaussianExperiment-3-size6_exact/4-LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="4-LinearSVC_exact"><img src="GaussianExperiment-3-size6_exact/7-SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="7-SVC_rbf_exact"><img src="GaussianExperiment-3-size6_exact/10-MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="10-MLPClassifier_exact">

##### seed 2
<img src="GaussianExperiment-3-size6_exact/2-LogisticRegression_exact/plot_dataset.png" width="200" alt="2-LogisticRegression_exact"><img src="GaussianExperiment-3-size6_exact/5-LinearSVC_exact/plot_dataset.png" width="200" alt="5-LinearSVC_exact"><img src="GaussianExperiment-3-size6_exact/8-SVC_rbf_exact/plot_dataset.png" width="200" alt="8-SVC_rbf_exact"><img src="GaussianExperiment-3-size6_exact/11-MLPClassifier_exact/plot_dataset.png" width="200" alt="11-MLPClassifier_exact">

<img src="GaussianExperiment-3-size6_exact/2-LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="2-LogisticRegression_exact"><img src="GaussianExperiment-3-size6_exact/5-LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="5-LinearSVC_exact"><img src="GaussianExperiment-3-size6_exact/8-SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="8-SVC_rbf_exact"><img src="GaussianExperiment-3-size6_exact/11-MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="11-MLPClassifier_exact">

<img src="GaussianExperiment-3-size6_exact/2-LogisticRegression_exact/plot_shapley_values.png" width="200" alt="2-LogisticRegression_exact"><img src="GaussianExperiment-3-size6_exact/5-LinearSVC_exact/plot_shapley_values.png" width="200" alt="5-LinearSVC_exact"><img src="GaussianExperiment-3-size6_exact/8-SVC_rbf_exact/plot_shapley_values.png" width="200" alt="8-SVC_rbf_exact"><img src="GaussianExperiment-3-size6_exact/11-MLPClassifier_exact/plot_shapley_values.png" width="200" alt="11-MLPClassifier_exact">

<img src="GaussianExperiment-3-size6_exact/2-LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="2-LogisticRegression_exact"><img src="GaussianExperiment-3-size6_exact/5-LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="5-LinearSVC_exact"><img src="GaussianExperiment-3-size6_exact/8-SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="8-SVC_rbf_exact"><img src="GaussianExperiment-3-size6_exact/11-MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="11-MLPClassifier_exact">

#### GaussianExperiment-4-size8_exact
##### seed 0
<img src="GaussianExperiment-4-size8_exact/0-LogisticRegression_exact/plot_dataset.png" width="200" alt="0-LogisticRegression_exact"><img src="GaussianExperiment-4-size8_exact/3-LinearSVC_exact/plot_dataset.png" width="200" alt="3-LinearSVC_exact"><img src="GaussianExperiment-4-size8_exact/6-SVC_rbf_exact/plot_dataset.png" width="200" alt="6-SVC_rbf_exact"><img src="GaussianExperiment-4-size8_exact/9-MLPClassifier_exact/plot_dataset.png" width="200" alt="9-MLPClassifier_exact">

<img src="GaussianExperiment-4-size8_exact/0-LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="0-LogisticRegression_exact"><img src="GaussianExperiment-4-size8_exact/3-LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="3-LinearSVC_exact"><img src="GaussianExperiment-4-size8_exact/6-SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="6-SVC_rbf_exact"><img src="GaussianExperiment-4-size8_exact/9-MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="9-MLPClassifier_exact">

<img src="GaussianExperiment-4-size8_exact/0-LogisticRegression_exact/plot_shapley_values.png" width="200" alt="0-LogisticRegression_exact"><img src="GaussianExperiment-4-size8_exact/3-LinearSVC_exact/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact"><img src="GaussianExperiment-4-size8_exact/6-SVC_rbf_exact/plot_shapley_values.png" width="200" alt="6-SVC_rbf_exact"><img src="GaussianExperiment-4-size8_exact/9-MLPClassifier_exact/plot_shapley_values.png" width="200" alt="9-MLPClassifier_exact">

<img src="GaussianExperiment-4-size8_exact/0-LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="0-LogisticRegression_exact"><img src="GaussianExperiment-4-size8_exact/3-LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="3-LinearSVC_exact"><img src="GaussianExperiment-4-size8_exact/6-SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="6-SVC_rbf_exact"><img src="GaussianExperiment-4-size8_exact/9-MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="9-MLPClassifier_exact">

##### seed 1
<img src="GaussianExperiment-4-size8_exact/1-LogisticRegression_exact/plot_dataset.png" width="200" alt="1-LogisticRegression_exact"><img src="GaussianExperiment-4-size8_exact/4-LinearSVC_exact/plot_dataset.png" width="200" alt="4-LinearSVC_exact"><img src="GaussianExperiment-4-size8_exact/7-SVC_rbf_exact/plot_dataset.png" width="200" alt="7-SVC_rbf_exact"><img src="GaussianExperiment-4-size8_exact/10-MLPClassifier_exact/plot_dataset.png" width="200" alt="10-MLPClassifier_exact">

<img src="GaussianExperiment-4-size8_exact/1-LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="1-LogisticRegression_exact"><img src="GaussianExperiment-4-size8_exact/4-LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="4-LinearSVC_exact"><img src="GaussianExperiment-4-size8_exact/7-SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="7-SVC_rbf_exact"><img src="GaussianExperiment-4-size8_exact/10-MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="10-MLPClassifier_exact">

<img src="GaussianExperiment-4-size8_exact/1-LogisticRegression_exact/plot_shapley_values.png" width="200" alt="1-LogisticRegression_exact"><img src="GaussianExperiment-4-size8_exact/4-LinearSVC_exact/plot_shapley_values.png" width="200" alt="4-LinearSVC_exact"><img src="GaussianExperiment-4-size8_exact/7-SVC_rbf_exact/plot_shapley_values.png" width="200" alt="7-SVC_rbf_exact"><img src="GaussianExperiment-4-size8_exact/10-MLPClassifier_exact/plot_shapley_values.png" width="200" alt="10-MLPClassifier_exact">

<img src="GaussianExperiment-4-size8_exact/1-LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="1-LogisticRegression_exact"><img src="GaussianExperiment-4-size8_exact/4-LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="4-LinearSVC_exact"><img src="GaussianExperiment-4-size8_exact/7-SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="7-SVC_rbf_exact"><img src="GaussianExperiment-4-size8_exact/10-MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="10-MLPClassifier_exact">

##### seed 2
<img src="GaussianExperiment-4-size8_exact/2-LogisticRegression_exact/plot_dataset.png" width="200" alt="2-LogisticRegression_exact"><img src="GaussianExperiment-4-size8_exact/5-LinearSVC_exact/plot_dataset.png" width="200" alt="5-LinearSVC_exact"><img src="GaussianExperiment-4-size8_exact/8-SVC_rbf_exact/plot_dataset.png" width="200" alt="8-SVC_rbf_exact"><img src="GaussianExperiment-4-size8_exact/11-MLPClassifier_exact/plot_dataset.png" width="200" alt="11-MLPClassifier_exact">

<img src="GaussianExperiment-4-size8_exact/2-LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="2-LogisticRegression_exact"><img src="GaussianExperiment-4-size8_exact/5-LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="5-LinearSVC_exact"><img src="GaussianExperiment-4-size8_exact/8-SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="8-SVC_rbf_exact"><img src="GaussianExperiment-4-size8_exact/11-MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="11-MLPClassifier_exact">

<img src="GaussianExperiment-4-size8_exact/2-LogisticRegression_exact/plot_shapley_values.png" width="200" alt="2-LogisticRegression_exact"><img src="GaussianExperiment-4-size8_exact/5-LinearSVC_exact/plot_shapley_values.png" width="200" alt="5-LinearSVC_exact"><img src="GaussianExperiment-4-size8_exact/8-SVC_rbf_exact/plot_shapley_values.png" width="200" alt="8-SVC_rbf_exact"><img src="GaussianExperiment-4-size8_exact/11-MLPClassifier_exact/plot_shapley_values.png" width="200" alt="11-MLPClassifier_exact">

<img src="GaussianExperiment-4-size8_exact/2-LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="2-LogisticRegression_exact"><img src="GaussianExperiment-4-size8_exact/5-LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="5-LinearSVC_exact"><img src="GaussianExperiment-4-size8_exact/8-SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="8-SVC_rbf_exact"><img src="GaussianExperiment-4-size8_exact/11-MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="11-MLPClassifier_exact">

#### GaussianExperiment-1-size10_exact
##### seed 0
<img src="GaussianExperiment-1-size10_exact/0-LogisticRegression_exact/plot_dataset.png" width="200" alt="0-LogisticRegression_exact"><img src="GaussianExperiment-1-size10_exact/3-LinearSVC_exact/plot_dataset.png" width="200" alt="3-LinearSVC_exact"><img src="GaussianExperiment-1-size10_exact/6-SVC_rbf_exact/plot_dataset.png" width="200" alt="6-SVC_rbf_exact"><img src="GaussianExperiment-1-size10_exact/9-MLPClassifier_exact/plot_dataset.png" width="200" alt="9-MLPClassifier_exact">

<img src="GaussianExperiment-1-size10_exact/0-LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="0-LogisticRegression_exact"><img src="GaussianExperiment-1-size10_exact/3-LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="3-LinearSVC_exact"><img src="GaussianExperiment-1-size10_exact/6-SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="6-SVC_rbf_exact"><img src="GaussianExperiment-1-size10_exact/9-MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="9-MLPClassifier_exact">

<img src="GaussianExperiment-1-size10_exact/0-LogisticRegression_exact/plot_shapley_values.png" width="200" alt="0-LogisticRegression_exact"><img src="GaussianExperiment-1-size10_exact/3-LinearSVC_exact/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact"><img src="GaussianExperiment-1-size10_exact/6-SVC_rbf_exact/plot_shapley_values.png" width="200" alt="6-SVC_rbf_exact"><img src="GaussianExperiment-1-size10_exact/9-MLPClassifier_exact/plot_shapley_values.png" width="200" alt="9-MLPClassifier_exact">

<img src="GaussianExperiment-1-size10_exact/0-LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="0-LogisticRegression_exact"><img src="GaussianExperiment-1-size10_exact/3-LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="3-LinearSVC_exact"><img src="GaussianExperiment-1-size10_exact/6-SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="6-SVC_rbf_exact"><img src="GaussianExperiment-1-size10_exact/9-MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="9-MLPClassifier_exact">

##### seed 1
<img src="GaussianExperiment-1-size10_exact/1-LogisticRegression_exact/plot_dataset.png" width="200" alt="1-LogisticRegression_exact"><img src="GaussianExperiment-1-size10_exact/4-LinearSVC_exact/plot_dataset.png" width="200" alt="4-LinearSVC_exact"><img src="GaussianExperiment-1-size10_exact/7-SVC_rbf_exact/plot_dataset.png" width="200" alt="7-SVC_rbf_exact"><img src="GaussianExperiment-1-size10_exact/10-MLPClassifier_exact/plot_dataset.png" width="200" alt="10-MLPClassifier_exact">

<img src="GaussianExperiment-1-size10_exact/1-LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="1-LogisticRegression_exact"><img src="GaussianExperiment-1-size10_exact/4-LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="4-LinearSVC_exact"><img src="GaussianExperiment-1-size10_exact/7-SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="7-SVC_rbf_exact"><img src="GaussianExperiment-1-size10_exact/10-MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="10-MLPClassifier_exact">

<img src="GaussianExperiment-1-size10_exact/1-LogisticRegression_exact/plot_shapley_values.png" width="200" alt="1-LogisticRegression_exact"><img src="GaussianExperiment-1-size10_exact/4-LinearSVC_exact/plot_shapley_values.png" width="200" alt="4-LinearSVC_exact"><img src="GaussianExperiment-1-size10_exact/7-SVC_rbf_exact/plot_shapley_values.png" width="200" alt="7-SVC_rbf_exact"><img src="GaussianExperiment-1-size10_exact/10-MLPClassifier_exact/plot_shapley_values.png" width="200" alt="10-MLPClassifier_exact">

<img src="GaussianExperiment-1-size10_exact/1-LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="1-LogisticRegression_exact"><img src="GaussianExperiment-1-size10_exact/4-LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="4-LinearSVC_exact"><img src="GaussianExperiment-1-size10_exact/7-SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="7-SVC_rbf_exact"><img src="GaussianExperiment-1-size10_exact/10-MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="10-MLPClassifier_exact">

##### seed 2
<img src="GaussianExperiment-1-size10_exact/2-LogisticRegression_exact/plot_dataset.png" width="200" alt="2-LogisticRegression_exact"><img src="GaussianExperiment-1-size10_exact/5-LinearSVC_exact/plot_dataset.png" width="200" alt="5-LinearSVC_exact"><img src="GaussianExperiment-1-size10_exact/8-SVC_rbf_exact/plot_dataset.png" width="200" alt="8-SVC_rbf_exact"><img src="GaussianExperiment-1-size10_exact/11-MLPClassifier_exact/plot_dataset.png" width="200" alt="11-MLPClassifier_exact">

<img src="GaussianExperiment-1-size10_exact/2-LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="2-LogisticRegression_exact"><img src="GaussianExperiment-1-size10_exact/5-LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="5-LinearSVC_exact"><img src="GaussianExperiment-1-size10_exact/8-SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="8-SVC_rbf_exact"><img src="GaussianExperiment-1-size10_exact/11-MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="11-MLPClassifier_exact">

<img src="GaussianExperiment-1-size10_exact/2-LogisticRegression_exact/plot_shapley_values.png" width="200" alt="2-LogisticRegression_exact"><img src="GaussianExperiment-1-size10_exact/5-LinearSVC_exact/plot_shapley_values.png" width="200" alt="5-LinearSVC_exact"><img src="GaussianExperiment-1-size10_exact/8-SVC_rbf_exact/plot_shapley_values.png" width="200" alt="8-SVC_rbf_exact"><img src="GaussianExperiment-1-size10_exact/11-MLPClassifier_exact/plot_shapley_values.png" width="200" alt="11-MLPClassifier_exact">

<img src="GaussianExperiment-1-size10_exact/2-LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="2-LogisticRegression_exact"><img src="GaussianExperiment-1-size10_exact/5-LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="5-LinearSVC_exact"><img src="GaussianExperiment-1-size10_exact/8-SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="8-SVC_rbf_exact"><img src="GaussianExperiment-1-size10_exact/11-MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="11-MLPClassifier_exact">

---------------------------------------

### Approximate Shapley values

\#| \| |size train|size test|num perm|seed| \| |size total|num eval| \| |LR|SVC_lin|SVC_rbf|MLP
-| - |-|-|-|-| - |-|-| - |-|-|-|-
2-size100_approx| \| |100|1000|**200**|0| \| |200|40K| \| |0.8350 / 02:57|0.8345 / 01:43|0.8225 / 07:10|0.8055 / 51:04
2-size100_approx| \| |100|1000|**400**|0| \| |200|80K| \| |0.8350 / 05:18|0.8345 / 03:25|0.8225 / 14:20|0.8055 / 1:41:30
2-size100_approx| \| |100|1000|**600**|0| \| |200|120K| \| |0.8350 / 07:59|0.8345 / 05:08|0.8225 / 21:26|0.8054 / 2:32:39
5-size100_200_approx| \| |**100**|1000|**460**|0| \| |200|92K| \| |0.8350 / 06:25|0.8345 / 03:56|0.8225 / 16:33|0.8054 / 1:57:18
5-size100_200_approx| \| |**200**|1000|**1060**|0| \| |400|424K| \| |0.8375 / 30:43|0.8370 / 22:10|0.8365 / 2:02:43|0.8410 / 11:29:20
6-size400_approx| \| |**400**|1000|**2400**|0| \| |800|960K| \| |0.8390 / 2:38:52|0.8365 / 2:22:20|0.8410 / 19:03:13|0.8464 / 58:44:00

#### GaussianExperiment-2-size100_approx
##### 200 permutations
<img src="GaussianExperiment-2-size100_approx/0-LogisticRegression_approx200/plot_dataset.png" width="200" alt="0-LogisticRegression_approx200"><img src="GaussianExperiment-2-size100_approx/1-LinearSVC_approx200/plot_dataset.png" width="200" alt="1-LinearSVC_approx200"><img src="GaussianExperiment-2-size100_approx/2-SVC_rbf_approx200/plot_dataset.png" width="200" alt="2-SVC_rbf_approx200"><img src="GaussianExperiment-2-size100_approx/3-MLPClassifier_approx200/plot_dataset.png" width="200" alt="3-MLPClassifier_approx200">

<img src="GaussianExperiment-2-size100_approx/0-LogisticRegression_approx200/plot_dataset_splitted.png" width="200" alt="0-LogisticRegression_approx200"><img src="GaussianExperiment-2-size100_approx/1-LinearSVC_approx200/plot_dataset_splitted.png" width="200" alt="1-LinearSVC_approx200"><img src="GaussianExperiment-2-size100_approx/2-SVC_rbf_approx200/plot_dataset_splitted.png" width="200" alt="2-SVC_rbf_approx200"><img src="GaussianExperiment-2-size100_approx/3-MLPClassifier_approx200/plot_dataset_splitted.png" width="200" alt="3-MLPClassifier_approx200">

<img src="GaussianExperiment-2-size100_approx/0-LogisticRegression_approx200/plot_shapley_values.png" width="200" alt="0-LogisticRegression_approx200"><img src="GaussianExperiment-2-size100_approx/1-LinearSVC_approx200/plot_shapley_values.png" width="200" alt="1-LinearSVC_approx200"><img src="GaussianExperiment-2-size100_approx/2-SVC_rbf_approx200/plot_shapley_values.png" width="200" alt="2-SVC_rbf_approx200"><img src="GaussianExperiment-2-size100_approx/3-MLPClassifier_approx200/plot_shapley_values.png" width="200" alt="3-MLPClassifier_approx200">

<img src="GaussianExperiment-2-size100_approx/0-LogisticRegression_approx200/plot_shapley_values_sorted.png" width="200" alt="0-LogisticRegression_approx200"><img src="GaussianExperiment-2-size100_approx/1-LinearSVC_approx200/plot_shapley_values_sorted.png" width="200" alt="1-LinearSVC_approx200"><img src="GaussianExperiment-2-size100_approx/2-SVC_rbf_approx200/plot_shapley_values_sorted.png" width="200" alt="2-SVC_rbf_approx200"><img src="GaussianExperiment-2-size100_approx/3-MLPClassifier_approx200/plot_shapley_values_sorted.png" width="200" alt="3-MLPClassifier_approx200">

##### 400 permutations
<img src="GaussianExperiment-2-size100_approx/4-LogisticRegression_approx400/plot_dataset.png" width="200" alt="4-LogisticRegression_approx400"><img src="GaussianExperiment-2-size100_approx/5-LinearSVC_approx400/plot_dataset.png" width="200" alt="5-LinearSVC_approx400"><img src="GaussianExperiment-2-size100_approx/6-SVC_rbf_approx400/plot_dataset.png" width="200" alt="6-SVC_rbf_approx400"><img src="GaussianExperiment-2-size100_approx/7-MLPClassifier_approx400/plot_dataset.png" width="200" alt="7-MLPClassifier_approx400">

<img src="GaussianExperiment-2-size100_approx/4-LogisticRegression_approx400/plot_dataset_splitted.png" width="200" alt="4-LogisticRegression_approx400"><img src="GaussianExperiment-2-size100_approx/5-LinearSVC_approx400/plot_dataset_splitted.png" width="200" alt="5-LinearSVC_approx400"><img src="GaussianExperiment-2-size100_approx/6-SVC_rbf_approx400/plot_dataset_splitted.png" width="200" alt="6-SVC_rbf_approx400"><img src="GaussianExperiment-2-size100_approx/7-MLPClassifier_approx400/plot_dataset_splitted.png" width="200" alt="7-MLPClassifier_approx400">

<img src="GaussianExperiment-2-size100_approx/4-LogisticRegression_approx400/plot_shapley_values.png" width="200" alt="4-LogisticRegression_approx400"><img src="GaussianExperiment-2-size100_approx/5-LinearSVC_approx400/plot_shapley_values.png" width="200" alt="5-LinearSVC_approx400"><img src="GaussianExperiment-2-size100_approx/6-SVC_rbf_approx400/plot_shapley_values.png" width="200" alt="6-SVC_rbf_approx400"><img src="GaussianExperiment-2-size100_approx/7-MLPClassifier_approx400/plot_shapley_values.png" width="200" alt="7-MLPClassifier_approx400">

<img src="GaussianExperiment-2-size100_approx/4-LogisticRegression_approx400/plot_shapley_values_sorted.png" width="200" alt="4-LogisticRegression_approx400"><img src="GaussianExperiment-2-size100_approx/5-LinearSVC_approx400/plot_shapley_values_sorted.png" width="200" alt="5-LinearSVC_approx400"><img src="GaussianExperiment-2-size100_approx/6-SVC_rbf_approx400/plot_shapley_values_sorted.png" width="200" alt="6-SVC_rbf_approx400"><img src="GaussianExperiment-2-size100_approx/7-MLPClassifier_approx400/plot_shapley_values_sorted.png" width="200" alt="7-MLPClassifier_approx400">

##### 600 permutations
<img src="GaussianExperiment-2-size100_approx/8-LogisticRegression_approx600/plot_dataset.png" width="200" alt="8-LogisticRegression_approx600"><img src="GaussianExperiment-2-size100_approx/9-LinearSVC_approx600/plot_dataset.png" width="200" alt="9-LinearSVC_approx600"><img src="GaussianExperiment-2-size100_approx/10-SVC_rbf_approx600/plot_dataset.png" width="200" alt="10-SVC_rbf_approx600"><img src="GaussianExperiment-2-size100_approx/11-MLPClassifier_approx600/plot_dataset.png" width="200" alt="11-MLPClassifier_approx600">

<img src="GaussianExperiment-2-size100_approx/8-LogisticRegression_approx600/plot_dataset_splitted.png" width="200" alt="8-LogisticRegression_approx600"><img src="GaussianExperiment-2-size100_approx/9-LinearSVC_approx600/plot_dataset_splitted.png" width="200" alt="9-LinearSVC_approx600"><img src="GaussianExperiment-2-size100_approx/10-SVC_rbf_approx600/plot_dataset_splitted.png" width="200" alt="10-SVC_rbf_approx600"><img src="GaussianExperiment-2-size100_approx/11-MLPClassifier_approx600/plot_dataset_splitted.png" width="200" alt="11-MLPClassifier_approx600">

<img src="GaussianExperiment-2-size100_approx/8-LogisticRegression_approx600/plot_shapley_values.png" width="200" alt="8-LogisticRegression_approx600"><img src="GaussianExperiment-2-size100_approx/9-LinearSVC_approx600/plot_shapley_values.png" width="200" alt="9-LinearSVC_approx600"><img src="GaussianExperiment-2-size100_approx/10-SVC_rbf_approx600/plot_shapley_values.png" width="200" alt="10-SVC_rbf_approx600"><img src="GaussianExperiment-2-size100_approx/11-MLPClassifier_approx600/plot_shapley_values.png" width="200" alt="11-MLPClassifier_approx600">

<img src="GaussianExperiment-2-size100_approx/8-LogisticRegression_approx600/plot_shapley_values_sorted.png" width="200" alt="8-LogisticRegression_approx600"><img src="GaussianExperiment-2-size100_approx/9-LinearSVC_approx600/plot_shapley_values_sorted.png" width="200" alt="9-LinearSVC_approx600"><img src="GaussianExperiment-2-size100_approx/10-SVC_rbf_approx600/plot_shapley_values_sorted.png" width="200" alt="10-SVC_rbf_approx600"><img src="GaussianExperiment-2-size100_approx/11-MLPClassifier_approx600/plot_shapley_values_sorted.png" width="200" alt="11-MLPClassifier_approx600">

#### GaussianExperiment-5-size100_200_approx
##### size: 100, permutations: 460
<img src="GaussianExperiment-5-size100_200_approx/0-LogisticRegression_approx460/plot_dataset.png" width="200" alt="0-LogisticRegression_approx460"><img src="GaussianExperiment-5-size100_200_approx/1-LinearSVC_approx460/plot_dataset.png" width="200" alt="1-LinearSVC_approx460"><img src="GaussianExperiment-5-size100_200_approx/2-SVC_rbf_approx460/plot_dataset.png" width="200" alt="2-SVC_rbf_approx460"><img src="GaussianExperiment-5-size100_200_approx/3-MLPClassifier_approx460/plot_dataset.png" width="200" alt="3-MLPClassifier_approx460">

<img src="GaussianExperiment-5-size100_200_approx/0-LogisticRegression_approx460/plot_dataset_splitted.png" width="200" alt="0-LogisticRegression_approx460"><img src="GaussianExperiment-5-size100_200_approx/1-LinearSVC_approx460/plot_dataset_splitted.png" width="200" alt="1-LinearSVC_approx460"><img src="GaussianExperiment-5-size100_200_approx/2-SVC_rbf_approx460/plot_dataset_splitted.png" width="200" alt="2-SVC_rbf_approx460"><img src="GaussianExperiment-5-size100_200_approx/3-MLPClassifier_approx460/plot_dataset_splitted.png" width="200" alt="3-MLPClassifier_approx460">

<img src="GaussianExperiment-5-size100_200_approx/0-LogisticRegression_approx460/plot_shapley_values.png" width="200" alt="0-LogisticRegression_approx460"><img src="GaussianExperiment-5-size100_200_approx/1-LinearSVC_approx460/plot_shapley_values.png" width="200" alt="1-LinearSVC_approx460"><img src="GaussianExperiment-5-size100_200_approx/2-SVC_rbf_approx460/plot_shapley_values.png" width="200" alt="2-SVC_rbf_approx460"><img src="GaussianExperiment-5-size100_200_approx/3-MLPClassifier_approx460/plot_shapley_values.png" width="200" alt="3-MLPClassifier_approx460">

<img src="GaussianExperiment-5-size100_200_approx/0-LogisticRegression_approx460/plot_shapley_values_sorted.png" width="200" alt="0-LogisticRegression_approx460"><img src="GaussianExperiment-5-size100_200_approx/1-LinearSVC_approx460/plot_shapley_values_sorted.png" width="200" alt="1-LinearSVC_approx460"><img src="GaussianExperiment-5-size100_200_approx/2-SVC_rbf_approx460/plot_shapley_values_sorted.png" width="200" alt="2-SVC_rbf_approx460"><img src="GaussianExperiment-5-size100_200_approx/3-MLPClassifier_approx460/plot_shapley_values_sorted.png" width="200" alt="3-MLPClassifier_approx460">

##### size: 200, permutations: 1060
<img src="GaussianExperiment-5-size100_200_approx/4-LogisticRegression_approx1060/plot_dataset.png" width="200" alt="4-LogisticRegression_approx1060"><img src="GaussianExperiment-5-size100_200_approx/5-LinearSVC_approx1060/plot_dataset.png" width="200" alt="5-LinearSVC_approx1060"><img src="GaussianExperiment-5-size100_200_approx/6-SVC_rbf_approx1060/plot_dataset.png" width="200" alt="6-SVC_rbf_approx1060"><img src="GaussianExperiment-5-size100_200_approx/7-MLPClassifier_approx1060/plot_dataset.png" width="200" alt="7-MLPClassifier_approx1060">

<img src="GaussianExperiment-5-size100_200_approx/4-LogisticRegression_approx1060/plot_dataset_splitted.png" width="200" alt="4-LogisticRegression_approx1060"><img src="GaussianExperiment-5-size100_200_approx/5-LinearSVC_approx1060/plot_dataset_splitted.png" width="200" alt="5-LinearSVC_approx1060"><img src="GaussianExperiment-5-size100_200_approx/6-SVC_rbf_approx1060/plot_dataset_splitted.png" width="200" alt="6-SVC_rbf_approx1060"><img src="GaussianExperiment-5-size100_200_approx/7-MLPClassifier_approx1060/plot_dataset_splitted.png" width="200" alt="7-MLPClassifier_approx1060">

<img src="GaussianExperiment-5-size100_200_approx/4-LogisticRegression_approx1060/plot_shapley_values.png" width="200" alt="4-LogisticRegression_approx1060"><img src="GaussianExperiment-5-size100_200_approx/5-LinearSVC_approx1060/plot_shapley_values.png" width="200" alt="5-LinearSVC_approx1060"><img src="GaussianExperiment-5-size100_200_approx/6-SVC_rbf_approx1060/plot_shapley_values.png" width="200" alt="6-SVC_rbf_approx1060"><img src="GaussianExperiment-5-size100_200_approx/7-MLPClassifier_approx1060/plot_shapley_values.png" width="200" alt="7-MLPClassifier_approx1060">

<img src="GaussianExperiment-5-size100_200_approx/4-LogisticRegression_approx1060/plot_shapley_values_sorted.png" width="200" alt="4-LogisticRegression_approx1060"><img src="GaussianExperiment-5-size100_200_approx/5-LinearSVC_approx1060/plot_shapley_values_sorted.png" width="200" alt="5-LinearSVC_approx1060"><img src="GaussianExperiment-5-size100_200_approx/6-SVC_rbf_approx1060/plot_shapley_values_sorted.png" width="200" alt="6-SVC_rbf_approx1060"><img src="GaussianExperiment-5-size100_200_approx/7-MLPClassifier_approx1060/plot_shapley_values_sorted.png" width="200" alt="7-MLPClassifier_approx1060">

##### size: 400, permutations: 2400
<img src="GaussianExperiment-6-size400_approx/0-LogisticRegression_approx2400/plot_dataset.png" width="200" alt="0-LogisticRegression_approx2400"><img src="GaussianExperiment-6-size400_approx/1-LinearSVC_approx2400/plot_dataset.png" width="200" alt="1-LinearSVC_approx2400"><img src="GaussianExperiment-6-size400_approx/2-SVC_rbf_approx2400/plot_dataset.png" width="200" alt="2-SVC_rbf_approx2400"><img src="GaussianExperiment-6-size400_approx/3-MLPClassifier_approx2400/plot_dataset.png" width="200" alt="3-MLPClassifier_approx2400">

<img src="GaussianExperiment-6-size400_approx/0-LogisticRegression_approx2400/plot_dataset_splitted.png" width="200" alt="0-LogisticRegression_approx2400"><img src="GaussianExperiment-6-size400_approx/1-LinearSVC_approx2400/plot_dataset_splitted.png" width="200" alt="1-LinearSVC_approx2400"><img src="GaussianExperiment-6-size400_approx/2-SVC_rbf_approx2400/plot_dataset_splitted.png" width="200" alt="2-SVC_rbf_approx2400"><img src="GaussianExperiment-6-size400_approx/3-MLPClassifier_approx2400/plot_dataset_splitted.png" width="200" alt="3-MLPClassifier_approx2400">

<img src="GaussianExperiment-6-size400_approx/0-LogisticRegression_approx2400/plot_shapley_values.png" width="200" alt="0-LogisticRegression_approx2400"><img src="GaussianExperiment-6-size400_approx/1-LinearSVC_approx2400/plot_shapley_values.png" width="200" alt="1-LinearSVC_approx2400"><img src="GaussianExperiment-6-size400_approx/2-SVC_rbf_approx2400/plot_shapley_values.png" width="200" alt="2-SVC_rbf_approx2400"><img src="GaussianExperiment-6-size400_approx/3-MLPClassifier_approx2400/plot_shapley_values.png" width="200" alt="3-MLPClassifier_approx2400">

<img src="GaussianExperiment-6-size400_approx/0-LogisticRegression_approx2400/plot_shapley_values_sorted.png" width="200" alt="0-LogisticRegression_approx2400"><img src="GaussianExperiment-6-size400_approx/1-LinearSVC_approx2400/plot_shapley_values_sorted.png" width="200" alt="1-LinearSVC_approx2400"><img src="GaussianExperiment-6-size400_approx/2-SVC_rbf_approx2400/plot_shapley_values_sorted.png" width="200" alt="2-SVC_rbf_approx2400"><img src="GaussianExperiment-6-size400_approx/3-MLPClassifier_approx2400/plot_shapley_values_sorted.png" width="200" alt="3-MLPClassifier_approx2400">