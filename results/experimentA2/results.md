# COS598 - Final Project
## Results of `experimentA2`

### Setup
- Dataset
    - Gaussian 1: $\mu_1 = \begin{pmatrix}2 \\ -2\end{pmatrix}$ and $\Sigma_1 = V_1 \Lambda_1 V_1^T$ with $\Lambda_1 = \begin{pmatrix}3 & 0 \\ 0 & 1\end{pmatrix}$ and $V_1 = \begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}$
    - Gaussian 2: $\mu_2 = \begin{pmatrix}-2 \\ 2\end{pmatrix}$ and $\Sigma_2 = V_2 \Lambda_2 V_2^T$ with $\Lambda_2 = \begin{pmatrix}3 & 0 \\ 0 & 1\end{pmatrix}$ and $V_2 = \begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}$
- Models
    - LogisticRegression (LR)
    - LinearSVC (SVC_lin)
    - SVC with RBF kernel (SVC_rbf)
    - MLPClassifier with (10, 10) layers (MLP)

### Exact Shapley values

\#| \| |size train|size test|num perm|seed| \| |size total|num eval| \| |LR|SVC_lin|SVC_rbf|MLP
-| - |-|-|-|-| - |-|-| - |-|-|-|-
3_size6_exact| \| |6|100|None|**0**| \| |12|50K| \| |0.9500 / 00:09|0.9500 / 00:05|0.8550 / 00:03|0.8200 / 00:41
3_size6_exact| \| |6|100|None|**1**| \| |12|50K| \| |0.9750 / 00:10|0.9750 / 00:05|0.8750 / 00:03|0.9800 / 00:20
3_size6_exact| \| |6|100|None|**2**| \| |12|50K| \| |0.9850 / 00:10|0.9900 / 00:05|0.6850 / 00:03|0.9900 / 00:21
4_size8_exact| \| |8|100|None|**0**| \| |16|1M| \| |0.9400 / 02:47|0.9350 / 01:21|0.8350 / 00:53|0.9300 / 06:08
4_size8_exact| \| |8|100|None|**1**| \| |16|1M| \| |0.9750 / 02:43|0.9750 / 01:21|0.8650 / 00:53|0.9200 / 08:44
4_size8_exact| \| |8|100|None|**2**| \| |16|1M| \| |0.9850 / 02:44|0.9900 / 01:22|0.9050 / 00:53|0.9950 / 05:51
1_size10_exact| \| |10|100|None|**0**| \| |20|20M| \| |0.9600 / 45:10|0.9500 / 22:12|0.7900 / 14:31|0.9600 / 1:41:48
1_size10_exact| \| |10|100|None|**1**| \| |20|20M| \| |0.9700 / 44:51|0.9650 / 22:06|0.9100 / 14:31|0.9050 / 2:05:44
1_size10_exact| \| |10|100|None|**2**| \| |20|20M| \| |0.9850 / 44:59|0.9850 / 21:55|0.8900 / 14:30|0.9900 / 1:31:03

#### GaussianExperiment_3_size6_exact
##### seed 0
<img src="GaussianExperiment_3_size6_exact/0_LogisticRegression_exact/plot_dataset.png" width="200" alt="0_LogisticRegression_exact"><img src="GaussianExperiment_3_size6_exact/3_LinearSVC_exact/plot_dataset.png" width="200" alt="3_LinearSVC_exact"><img src="GaussianExperiment_3_size6_exact/6_SVC_rbf_exact/plot_dataset.png" width="200" alt="6_SVC_rbf_exact"><img src="GaussianExperiment_3_size6_exact/9_MLPClassifier_exact/plot_dataset.png" width="200" alt="9_MLPClassifier_exact">

<img src="GaussianExperiment_3_size6_exact/0_LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="0_LogisticRegression_exact"><img src="GaussianExperiment_3_size6_exact/3_LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="3_LinearSVC_exact"><img src="GaussianExperiment_3_size6_exact/6_SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="6_SVC_rbf_exact"><img src="GaussianExperiment_3_size6_exact/9_MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="9_MLPClassifier_exact">

<img src="GaussianExperiment_3_size6_exact/0_LogisticRegression_exact/plot_shapley_values.png" width="200" alt="0_LogisticRegression_exact"><img src="GaussianExperiment_3_size6_exact/3_LinearSVC_exact/plot_shapley_values.png" width="200" alt="3_LinearSVC_exact"><img src="GaussianExperiment_3_size6_exact/6_SVC_rbf_exact/plot_shapley_values.png" width="200" alt="6_SVC_rbf_exact"><img src="GaussianExperiment_3_size6_exact/9_MLPClassifier_exact/plot_shapley_values.png" width="200" alt="9_MLPClassifier_exact">

<img src="GaussianExperiment_3_size6_exact/0_LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="0_LogisticRegression_exact"><img src="GaussianExperiment_3_size6_exact/3_LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="3_LinearSVC_exact"><img src="GaussianExperiment_3_size6_exact/6_SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="6_SVC_rbf_exact"><img src="GaussianExperiment_3_size6_exact/9_MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="9_MLPClassifier_exact">

##### seed 1
<img src="GaussianExperiment_3_size6_exact/1_LogisticRegression_exact/plot_dataset.png" width="200" alt="_LogisticRegression_exact"><img src="GaussianExperiment_3_size6_exact/4_LinearSVC_exact/plot_dataset.png" width="200" alt="_LinearSVC_exact"><img src="GaussianExperiment_3_size6_exact/7_SVC_rbf_exact/plot_dataset.png" width="200" alt="_SVC_rbf_exact"><img src="GaussianExperiment_3_size6_exact/10_MLPClassifier_exact/plot_dataset.png" width="200" alt="_MLPClassifier_exact">

<img src="GaussianExperiment_3_size6_exact/1_LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="_LogisticRegression_exact"><img src="GaussianExperiment_3_size6_exact/4_LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="_LinearSVC_exact"><img src="GaussianExperiment_3_size6_exact/7_SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="_SVC_rbf_exact"><img src="GaussianExperiment_3_size6_exact/10_MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="_MLPClassifier_exact">

<img src="GaussianExperiment_3_size6_exact/1_LogisticRegression_exact/plot_shapley_values.png" width="200" alt="1_LogisticRegression_exact"><img src="GaussianExperiment_3_size6_exact/4_LinearSVC_exact/plot_shapley_values.png" width="200" alt="4_LinearSVC_exact"><img src="GaussianExperiment_3_size6_exact/7_SVC_rbf_exact/plot_shapley_values.png" width="200" alt="7_SVC_rbf_exact"><img src="GaussianExperiment_3_size6_exact/10_MLPClassifier_exact/plot_shapley_values.png" width="200" alt="10_MLPClassifier_exact">

<img src="GaussianExperiment_3_size6_exact/1_LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="1_LogisticRegression_exact"><img src="GaussianExperiment_3_size6_exact/4_LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="4_LinearSVC_exact"><img src="GaussianExperiment_3_size6_exact/7_SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="7_SVC_rbf_exact"><img src="GaussianExperiment_3_size6_exact/10_MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="10_MLPClassifier_exact">

##### seed 2
<img src="GaussianExperiment_3_size6_exact/2_LogisticRegression_exact/plot_dataset.png" width="200" alt="2_LogisticRegression_exact"><img src="GaussianExperiment_3_size6_exact/5_LinearSVC_exact/plot_dataset.png" width="200" alt="5_LinearSVC_exact"><img src="GaussianExperiment_3_size6_exact/8_SVC_rbf_exact/plot_dataset.png" width="200" alt="8_SVC_rbf_exact"><img src="GaussianExperiment_3_size6_exact/11_MLPClassifier_exact/plot_dataset.png" width="200" alt="11_MLPClassifier_exact">

<img src="GaussianExperiment_3_size6_exact/2_LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="2_LogisticRegression_exact"><img src="GaussianExperiment_3_size6_exact/5_LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="5_LinearSVC_exact"><img src="GaussianExperiment_3_size6_exact/8_SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="8_SVC_rbf_exact"><img src="GaussianExperiment_3_size6_exact/11_MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="11_MLPClassifier_exact">

<img src="GaussianExperiment_3_size6_exact/2_LogisticRegression_exact/plot_shapley_values.png" width="200" alt="2_LogisticRegression_exact"><img src="GaussianExperiment_3_size6_exact/5_LinearSVC_exact/plot_shapley_values.png" width="200" alt="5_LinearSVC_exact"><img src="GaussianExperiment_3_size6_exact/8_SVC_rbf_exact/plot_shapley_values.png" width="200" alt="8_SVC_rbf_exact"><img src="GaussianExperiment_3_size6_exact/11_MLPClassifier_exact/plot_shapley_values.png" width="200" alt="11_MLPClassifier_exact">

<img src="GaussianExperiment_3_size6_exact/2_LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="2_LogisticRegression_exact"><img src="GaussianExperiment_3_size6_exact/5_LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="5_LinearSVC_exact"><img src="GaussianExperiment_3_size6_exact/8_SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="8_SVC_rbf_exact"><img src="GaussianExperiment_3_size6_exact/11_MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="11_MLPClassifier_exact">

#### GaussianExperiment_4_size8_exact
##### seed 0
<img src="GaussianExperiment_4_size8_exact/0_LogisticRegression_exact/plot_dataset.png" width="200" alt="0_LogisticRegression_exact"><img src="GaussianExperiment_4_size8_exact/3_LinearSVC_exact/plot_dataset.png" width="200" alt="3_LinearSVC_exact"><img src="GaussianExperiment_4_size8_exact/6_SVC_rbf_exact/plot_dataset.png" width="200" alt="6_SVC_rbf_exact"><img src="GaussianExperiment_4_size8_exact/9_MLPClassifier_exact/plot_dataset.png" width="200" alt="9_MLPClassifier_exact">

<img src="GaussianExperiment_4_size8_exact/0_LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="0_LogisticRegression_exact"><img src="GaussianExperiment_4_size8_exact/3_LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="3_LinearSVC_exact"><img src="GaussianExperiment_4_size8_exact/6_SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="6_SVC_rbf_exact"><img src="GaussianExperiment_4_size8_exact/9_MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="9_MLPClassifier_exact">

<img src="GaussianExperiment_4_size8_exact/0_LogisticRegression_exact/plot_shapley_values.png" width="200" alt="0_LogisticRegression_exact"><img src="GaussianExperiment_4_size8_exact/3_LinearSVC_exact/plot_shapley_values.png" width="200" alt="3_LinearSVC_exact"><img src="GaussianExperiment_4_size8_exact/6_SVC_rbf_exact/plot_shapley_values.png" width="200" alt="6_SVC_rbf_exact"><img src="GaussianExperiment_4_size8_exact/9_MLPClassifier_exact/plot_shapley_values.png" width="200" alt="9_MLPClassifier_exact">

<img src="GaussianExperiment_4_size8_exact/0_LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="0_LogisticRegression_exact"><img src="GaussianExperiment_4_size8_exact/3_LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="3_LinearSVC_exact"><img src="GaussianExperiment_4_size8_exact/6_SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="6_SVC_rbf_exact"><img src="GaussianExperiment_4_size8_exact/9_MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="9_MLPClassifier_exact">

##### seed 1
<img src="GaussianExperiment_4_size8_exact/1_LogisticRegression_exact/plot_dataset.png" width="200" alt="1_LogisticRegression_exact"><img src="GaussianExperiment_4_size8_exact/4_LinearSVC_exact/plot_dataset.png" width="200" alt="4_LinearSVC_exact"><img src="GaussianExperiment_4_size8_exact/7_SVC_rbf_exact/plot_dataset.png" width="200" alt="7_SVC_rbf_exact"><img src="GaussianExperiment_4_size8_exact/10_MLPClassifier_exact/plot_dataset.png" width="200" alt="10_MLPClassifier_exact">

<img src="GaussianExperiment_4_size8_exact/1_LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="1_LogisticRegression_exact"><img src="GaussianExperiment_4_size8_exact/4_LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="4_LinearSVC_exact"><img src="GaussianExperiment_4_size8_exact/7_SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="7_SVC_rbf_exact"><img src="GaussianExperiment_4_size8_exact/10_MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="10_MLPClassifier_exact">

<img src="GaussianExperiment_4_size8_exact/1_LogisticRegression_exact/plot_shapley_values.png" width="200" alt="1_LogisticRegression_exact"><img src="GaussianExperiment_4_size8_exact/4_LinearSVC_exact/plot_shapley_values.png" width="200" alt="4_LinearSVC_exact"><img src="GaussianExperiment_4_size8_exact/7_SVC_rbf_exact/plot_shapley_values.png" width="200" alt="7_SVC_rbf_exact"><img src="GaussianExperiment_4_size8_exact/10_MLPClassifier_exact/plot_shapley_values.png" width="200" alt="10_MLPClassifier_exact">

<img src="GaussianExperiment_4_size8_exact/1_LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="1_LogisticRegression_exact"><img src="GaussianExperiment_4_size8_exact/4_LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="4_LinearSVC_exact"><img src="GaussianExperiment_4_size8_exact/7_SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="7_SVC_rbf_exact"><img src="GaussianExperiment_4_size8_exact/10_MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="10_MLPClassifier_exact">

##### seed 2
<img src="GaussianExperiment_4_size8_exact/2_LogisticRegression_exact/plot_dataset.png" width="200" alt="2_LogisticRegression_exact"><img src="GaussianExperiment_4_size8_exact/5_LinearSVC_exact/plot_dataset.png" width="200" alt="5_LinearSVC_exact"><img src="GaussianExperiment_4_size8_exact/8_SVC_rbf_exact/plot_dataset.png" width="200" alt="8_SVC_rbf_exact"><img src="GaussianExperiment_4_size8_exact/11_MLPClassifier_exact/plot_dataset.png" width="200" alt="11_MLPClassifier_exact">

<img src="GaussianExperiment_4_size8_exact/2_LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="2_LogisticRegression_exact"><img src="GaussianExperiment_4_size8_exact/5_LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="5_LinearSVC_exact"><img src="GaussianExperiment_4_size8_exact/8_SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="8_SVC_rbf_exact"><img src="GaussianExperiment_4_size8_exact/11_MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="11_MLPClassifier_exact">

<img src="GaussianExperiment_4_size8_exact/2_LogisticRegression_exact/plot_shapley_values.png" width="200" alt="2_LogisticRegression_exact"><img src="GaussianExperiment_4_size8_exact/5_LinearSVC_exact/plot_shapley_values.png" width="200" alt="5_LinearSVC_exact"><img src="GaussianExperiment_4_size8_exact/8_SVC_rbf_exact/plot_shapley_values.png" width="200" alt="8_SVC_rbf_exact"><img src="GaussianExperiment_4_size8_exact/11_MLPClassifier_exact/plot_shapley_values.png" width="200" alt="11_MLPClassifier_exact">

<img src="GaussianExperiment_4_size8_exact/2_LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="2_LogisticRegression_exact"><img src="GaussianExperiment_4_size8_exact/5_LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="5_LinearSVC_exact"><img src="GaussianExperiment_4_size8_exact/8_SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="8_SVC_rbf_exact"><img src="GaussianExperiment_4_size8_exact/11_MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="11_MLPClassifier_exact">

#### GaussianExperiment_1_size10_exact
##### seed 0
<img src="GaussianExperiment_1_size10_exact/0_LogisticRegression_exact/plot_dataset.png" width="200" alt="0_LogisticRegression_exact"><img src="GaussianExperiment_1_size10_exact/3_LinearSVC_exact/plot_dataset.png" width="200" alt="3_LinearSVC_exact"><img src="GaussianExperiment_1_size10_exact/6_SVC_rbf_exact/plot_dataset.png" width="200" alt="6_SVC_rbf_exact"><img src="GaussianExperiment_1_size10_exact/9_MLPClassifier_exact/plot_dataset.png" width="200" alt="9_MLPClassifier_exact">

<img src="GaussianExperiment_1_size10_exact/0_LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="0_LogisticRegression_exact"><img src="GaussianExperiment_1_size10_exact/3_LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="3_LinearSVC_exact"><img src="GaussianExperiment_1_size10_exact/6_SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="6_SVC_rbf_exact"><img src="GaussianExperiment_1_size10_exact/9_MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="9_MLPClassifier_exact">

<img src="GaussianExperiment_1_size10_exact/0_LogisticRegression_exact/plot_shapley_values.png" width="200" alt="0_LogisticRegression_exact"><img src="GaussianExperiment_1_size10_exact/3_LinearSVC_exact/plot_shapley_values.png" width="200" alt="3_LinearSVC_exact"><img src="GaussianExperiment_1_size10_exact/6_SVC_rbf_exact/plot_shapley_values.png" width="200" alt="6_SVC_rbf_exact"><img src="GaussianExperiment_1_size10_exact/9_MLPClassifier_exact/plot_shapley_values.png" width="200" alt="9_MLPClassifier_exact">

<img src="GaussianExperiment_1_size10_exact/0_LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="0_LogisticRegression_exact"><img src="GaussianExperiment_1_size10_exact/3_LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="3_LinearSVC_exact"><img src="GaussianExperiment_1_size10_exact/6_SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="6_SVC_rbf_exact"><img src="GaussianExperiment_1_size10_exact/9_MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="9_MLPClassifier_exact">

##### seed 1
<img src="GaussianExperiment_1_size10_exact/1_LogisticRegression_exact/plot_dataset.png" width="200" alt="1_LogisticRegression_exact"><img src="GaussianExperiment_1_size10_exact/4_LinearSVC_exact/plot_dataset.png" width="200" alt="4_LinearSVC_exact"><img src="GaussianExperiment_1_size10_exact/7_SVC_rbf_exact/plot_dataset.png" width="200" alt="7_SVC_rbf_exact"><img src="GaussianExperiment_1_size10_exact/10_MLPClassifier_exact/plot_dataset.png" width="200" alt="10_MLPClassifier_exact">

<img src="GaussianExperiment_1_size10_exact/1_LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="1_LogisticRegression_exact"><img src="GaussianExperiment_1_size10_exact/4_LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="4_LinearSVC_exact"><img src="GaussianExperiment_1_size10_exact/7_SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="7_SVC_rbf_exact"><img src="GaussianExperiment_1_size10_exact/10_MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="10_MLPClassifier_exact">

<img src="GaussianExperiment_1_size10_exact/1_LogisticRegression_exact/plot_shapley_values.png" width="200" alt="1_LogisticRegression_exact"><img src="GaussianExperiment_1_size10_exact/4_LinearSVC_exact/plot_shapley_values.png" width="200" alt="4_LinearSVC_exact"><img src="GaussianExperiment_1_size10_exact/7_SVC_rbf_exact/plot_shapley_values.png" width="200" alt="7_SVC_rbf_exact"><img src="GaussianExperiment_1_size10_exact/10_MLPClassifier_exact/plot_shapley_values.png" width="200" alt="10_MLPClassifier_exact">

<img src="GaussianExperiment_1_size10_exact/1_LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="1_LogisticRegression_exact"><img src="GaussianExperiment_1_size10_exact/4_LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="4_LinearSVC_exact"><img src="GaussianExperiment_1_size10_exact/7_SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="7_SVC_rbf_exact"><img src="GaussianExperiment_1_size10_exact/10_MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="10_MLPClassifier_exact">

##### seed 2
<img src="GaussianExperiment_1_size10_exact/2_LogisticRegression_exact/plot_dataset.png" width="200" alt="2_LogisticRegression_exact"><img src="GaussianExperiment_1_size10_exact/5_LinearSVC_exact/plot_dataset.png" width="200" alt="5_LinearSVC_exact"><img src="GaussianExperiment_1_size10_exact/8_SVC_rbf_exact/plot_dataset.png" width="200" alt="8_SVC_rbf_exact"><img src="GaussianExperiment_1_size10_exact/11_MLPClassifier_exact/plot_dataset.png" width="200" alt="11_MLPClassifier_exact">

<img src="GaussianExperiment_1_size10_exact/2_LogisticRegression_exact/plot_dataset_splitted.png" width="200" alt="2_LogisticRegression_exact"><img src="GaussianExperiment_1_size10_exact/5_LinearSVC_exact/plot_dataset_splitted.png" width="200" alt="5_LinearSVC_exact"><img src="GaussianExperiment_1_size10_exact/8_SVC_rbf_exact/plot_dataset_splitted.png" width="200" alt="8_SVC_rbf_exact"><img src="GaussianExperiment_1_size10_exact/11_MLPClassifier_exact/plot_dataset_splitted.png" width="200" alt="11_MLPClassifier_exact">

<img src="GaussianExperiment_1_size10_exact/2_LogisticRegression_exact/plot_shapley_values.png" width="200" alt="2_LogisticRegression_exact"><img src="GaussianExperiment_1_size10_exact/5_LinearSVC_exact/plot_shapley_values.png" width="200" alt="5_LinearSVC_exact"><img src="GaussianExperiment_1_size10_exact/8_SVC_rbf_exact/plot_shapley_values.png" width="200" alt="8_SVC_rbf_exact"><img src="GaussianExperiment_1_size10_exact/11_MLPClassifier_exact/plot_shapley_values.png" width="200" alt="11_MLPClassifier_exact">

<img src="GaussianExperiment_1_size10_exact/2_LogisticRegression_exact/plot_shapley_values_sorted.png" width="200" alt="2_LogisticRegression_exact"><img src="GaussianExperiment_1_size10_exact/5_LinearSVC_exact/plot_shapley_values_sorted.png" width="200" alt="5_LinearSVC_exact"><img src="GaussianExperiment_1_size10_exact/8_SVC_rbf_exact/plot_shapley_values_sorted.png" width="200" alt="8_SVC_rbf_exact"><img src="GaussianExperiment_1_size10_exact/11_MLPClassifier_exact/plot_shapley_values_sorted.png" width="200" alt="11_MLPClassifier_exact">

---------------------------------------

### Approximate Shapley values

\#| \| |size train|size test|num perm|seed| \| |size total|num eval| \| |LR|SVC_lin|SVC_rbf|MLP
-| - |-|-|-|-| - |-|-| - |-|-|-|-
2_size100_approx| \| |100|1000|**200**|0| \| |200|40K| \| |0.9725 / 02:50|0.9735 / 01:35|0.9665 / 06:05|0.9675 / 26:10
2_size100_approx| \| |100|1000|**400**|0| \| |200|80K| \| |0.9725 / 05:36|0.9735 / 03:10|0.9665 / 12:19|0.9675 / 52:11
2_size100_approx| \| |100|1000|**600**|0| \| |200|120K| \| |0.9725 / 08:28|0.9735 / 04:46|0.9665 / 18:21|0.9675 / 1:13:22
5_size100_200_approx| \| |**100**|1000|**460**|0| \| |200|92K| \|0.9725 / 06:28|0.9735 / 03:39|0.9665 / 14:19|0.9675 / 1:00:25
5_size100_200_approx| \| |**200**|1000|**1060**|0| \| |400|424K| \| |0.9685 / 35:36|0.9695 / 18:30|0.9665 / 1:56:34|0.9645 / 8:20:27
6_size400_approx| \| |**400**|1000|**2400**|0| \| |800|2M| \| |0.9720 / 3:21:39|0.9720 / 1:46:19|0.9680 / 14:17:24|0.9667 / 51:35:45

#### GaussianExperiment_2_size100_approx
##### LogisticRegression
<img src="GaussianExperiment_2_size100_approx/0_LogisticRegression_approx200/plot_dataset.png" width="200" alt="0_LogisticRegression_approx200"><img src="GaussianExperiment_2_size100_approx/4_LogisticRegression_approx400/plot_dataset.png" width="200" alt="4_LogisticRegression_approx400"><img src="GaussianExperiment_2_size100_approx/8_LogisticRegression_approx600/plot_dataset.png" width="200" alt="8_LogisticRegression_approx600">

<img src="GaussianExperiment_2_size100_approx/0_LogisticRegression_approx200/plot_dataset_splitted.png" width="200" alt="0_LogisticRegression_approx200"><img src="GaussianExperiment_2_size100_approx/4_LogisticRegression_approx400/plot_dataset_splitted.png" width="200" alt="4_LogisticRegression_approx400"><img src="GaussianExperiment_2_size100_approx/8_LogisticRegression_approx600/plot_dataset_splitted.png" width="200" alt="8_LogisticRegression_approx600">

<img src="GaussianExperiment_2_size100_approx/0_LogisticRegression_approx200/plot_shapley_values.png" width="200" alt="0_LogisticRegression_approx200"><img src="GaussianExperiment_2_size100_approx/4_LogisticRegression_approx400/plot_shapley_values.png" width="200" alt="4_LogisticRegression_approx400"><img src="GaussianExperiment_2_size100_approx/8_LogisticRegression_approx600/plot_shapley_values.png" width="200" alt="8_LogisticRegression_approx600">

<img src="GaussianExperiment_2_size100_approx/0_LogisticRegression_approx200/plot_shapley_values_sorted.png" width="200" alt="0_LogisticRegression_approx200"><img src="GaussianExperiment_2_size100_approx/4_LogisticRegression_approx400/plot_shapley_values_sorted.png" width="200" alt="4_LogisticRegression_approx400"><img src="GaussianExperiment_2_size100_approx/8_LogisticRegression_approx600/plot_shapley_values_sorted.png" width="200" alt="8_LogisticRegression_approx600">

##### LinearSVC
<img src="GaussianExperiment_2_size100_approx/1_LinearSVC_approx200/plot_dataset.png" width="200" alt="1_LinearSVC_approx200"><img src="GaussianExperiment_2_size100_approx/5_LinearSVC_approx400/plot_dataset.png" width="200" alt="5_LinearSVC_approx400"><img src="GaussianExperiment_2_size100_approx/9_LinearSVC_approx600/plot_dataset.png" width="200" alt="9_LinearSVC_approx600">

<img src="GaussianExperiment_2_size100_approx/1_LinearSVC_approx200/plot_dataset_splitted.png" width="200" alt="1_LinearSVC_approx200"><img src="GaussianExperiment_2_size100_approx/5_LinearSVC_approx400/plot_dataset_splitted.png" width="200" alt="5_LinearSVC_approx400"><img src="GaussianExperiment_2_size100_approx/9_LinearSVC_approx600/plot_dataset_splitted.png" width="200" alt="9_LinearSVC_approx600">

<img src="GaussianExperiment_2_size100_approx/1_LinearSVC_approx200/plot_shapley_values.png" width="200" alt="1_LinearSVC_approx200"><img src="GaussianExperiment_2_size100_approx/5_LinearSVC_approx400/plot_shapley_values.png" width="200" alt="5_LinearSVC_approx400"><img src="GaussianExperiment_2_size100_approx/9_LinearSVC_approx600/plot_shapley_values.png" width="200" alt="9_LinearSVC_approx600">

<img src="GaussianExperiment_2_size100_approx/1_LinearSVC_approx200/plot_shapley_values_sorted.png" width="200" alt="1_LinearSVC_approx200"><img src="GaussianExperiment_2_size100_approx/5_LinearSVC_approx400/plot_shapley_values_sorted.png" width="200" alt="5_LinearSVC_approx400"><img src="GaussianExperiment_2_size100_approx/9_LinearSVC_approx600/plot_shapley_values_sorted.png" width="200" alt="9_LinearSVC_approx600">

##### SVC_rbf
<img src="GaussianExperiment_2_size100_approx/2_SVC_rbf_approx200/plot_dataset.png" width="200" alt="2_SVC_rbf_approx200"><img src="GaussianExperiment_2_size100_approx/6_SVC_rbf_approx400/plot_dataset.png" width="200" alt="6_SVC_rbf_approx400"><img src="GaussianExperiment_2_size100_approx/10_SVC_rbf_approx600/plot_dataset.png" width="200" alt="10_SVC_rbf_approx600">

<img src="GaussianExperiment_2_size100_approx/2_SVC_rbf_approx200/plot_dataset_splitted.png" width="200" alt="2_SVC_rbf_approx200"><img src="GaussianExperiment_2_size100_approx/6_SVC_rbf_approx400/plot_dataset_splitted.png" width="200" alt="6_SVC_rbf_approx400"><img src="GaussianExperiment_2_size100_approx/10_SVC_rbf_approx600/plot_dataset_splitted.png" width="200" alt="10_SVC_rbf_approx600">

<img src="GaussianExperiment_2_size100_approx/2_SVC_rbf_approx200/plot_shapley_values.png" width="200" alt="2_SVC_rbf_approx200"><img src="GaussianExperiment_2_size100_approx/6_SVC_rbf_approx400/plot_shapley_values.png" width="200" alt="6_SVC_rbf_approx400"><img src="GaussianExperiment_2_size100_approx/10_SVC_rbf_approx600/plot_shapley_values.png" width="200" alt="10_SVC_rbf_approx600">

<img src="GaussianExperiment_2_size100_approx/2_SVC_rbf_approx200/plot_shapley_values_sorted.png" width="200" alt="2_SVC_rbf_approx200"><img src="GaussianExperiment_2_size100_approx/6_SVC_rbf_approx400/plot_shapley_values_sorted.png" width="200" alt="6_SVC_rbf_approx400"><img src="GaussianExperiment_2_size100_approx/10_SVC_rbf_approx600/plot_shapley_values_sorted.png" width="200" alt="10_SVC_rbf_approx600">

##### MLPClassifier
<img src="GaussianExperiment_2_size100_approx/3_MLPClassifier_approx200/plot_dataset.png" width="200" alt="3_MLPClassifier_approx200"><img src="GaussianExperiment_2_size100_approx/7_MLPClassifier_approx400/plot_dataset.png" width="200" alt="7_MLPClassifier_approx400"><img src="GaussianExperiment_2_size100_approx/11_MLPClassifier_approx600/plot_dataset.png" width="200" alt="11_MLPClassifier_approx600">

<img src="GaussianExperiment_2_size100_approx/3_MLPClassifier_approx200/plot_dataset_splitted.png" width="200" alt="3_MLPClassifier_approx200"><img src="GaussianExperiment_2_size100_approx/7_MLPClassifier_approx400/plot_dataset_splitted.png" width="200" alt="7_MLPClassifier_approx400"><img src="GaussianExperiment_2_size100_approx/11_MLPClassifier_approx600/plot_dataset_splitted.png" width="200" alt="11_MLPClassifier_approx600">

<img src="GaussianExperiment_2_size100_approx/3_MLPClassifier_approx200/plot_shapley_values.png" width="200" alt="3_MLPClassifier_approx200"><img src="GaussianExperiment_2_size100_approx/7_MLPClassifier_approx400/plot_shapley_values.png" width="200" alt="7_MLPClassifier_approx400"><img src="GaussianExperiment_2_size100_approx/11_MLPClassifier_approx600/plot_shapley_values.png" width="200" alt="11_MLPClassifier_approx600">

<img src="GaussianExperiment_2_size100_approx/3_MLPClassifier_approx200/plot_shapley_values_sorted.png" width="200" alt="3_MLPClassifier_approx200"><img src="GaussianExperiment_2_size100_approx/7_MLPClassifier_approx400/plot_shapley_values_sorted.png" width="200" alt="7_MLPClassifier_approx400"><img src="GaussianExperiment_2_size100_approx/11_MLPClassifier_approx600/plot_shapley_values_sorted.png" width="200" alt="11_MLPClassifier_approx600">

#### GaussianExperiment_5_size100_200_approx
##### size: 100, permutations: 460
<img src="GaussianExperiment_5_size100_200_approx/0_LogisticRegression_approx460/plot_dataset.png" width="200" alt="0_LogisticRegression_approx460"><img src="GaussianExperiment_5_size100_200_approx/1_LinearSVC_approx460/plot_dataset.png" width="200" alt="1_LinearSVC_approx460"><img src="GaussianExperiment_5_size100_200_approx/2_SVC_rbf_approx460/plot_dataset.png" width="200" alt="2_SVC_rbf_approx460"><img src="GaussianExperiment_5_size100_200_approx/3_MLPClassifier_approx460/plot_dataset.png" width="200" alt="3_MLPClassifier_approx460">

<img src="GaussianExperiment_5_size100_200_approx/0_LogisticRegression_approx460/plot_dataset_splitted.png" width="200" alt="0_LogisticRegression_approx460"><img src="GaussianExperiment_5_size100_200_approx/1_LinearSVC_approx460/plot_dataset_splitted.png" width="200" alt="1_LinearSVC_approx460"><img src="GaussianExperiment_5_size100_200_approx/2_SVC_rbf_approx460/plot_dataset_splitted.png" width="200" alt="2_SVC_rbf_approx460"><img src="GaussianExperiment_5_size100_200_approx/3_MLPClassifier_approx460/plot_dataset_splitted.png" width="200" alt="3_MLPClassifier_approx460">

<img src="GaussianExperiment_5_size100_200_approx/0_LogisticRegression_approx460/plot_shapley_values.png" width="200" alt="0_LogisticRegression_approx460"><img src="GaussianExperiment_5_size100_200_approx/1_LinearSVC_approx460/plot_shapley_values.png" width="200" alt="1_LinearSVC_approx460"><img src="GaussianExperiment_5_size100_200_approx/2_SVC_rbf_approx460/plot_shapley_values.png" width="200" alt="2_SVC_rbf_approx460"><img src="GaussianExperiment_5_size100_200_approx/3_MLPClassifier_approx460/plot_shapley_values.png" width="200" alt="3_MLPClassifier_approx460">

<img src="GaussianExperiment_5_size100_200_approx/0_LogisticRegression_approx460/plot_shapley_values_sorted.png" width="200" alt="0_LogisticRegression_approx460"><img src="GaussianExperiment_5_size100_200_approx/1_LinearSVC_approx460/plot_shapley_values_sorted.png" width="200" alt="1_LinearSVC_approx460"><img src="GaussianExperiment_5_size100_200_approx/2_SVC_rbf_approx460/plot_shapley_values_sorted.png" width="200" alt="2_SVC_rbf_approx460"><img src="GaussianExperiment_5_size100_200_approx/3_MLPClassifier_approx460/plot_shapley_values_sorted.png" width="200" alt="3_MLPClassifier_approx460">

##### size: 200, permutations: 1060
<img src="GaussianExperiment_5_size100_200_approx/4_LogisticRegression_approx1060/plot_dataset.png" width="200" alt="4_LogisticRegression_approx1060"><img src="GaussianExperiment_5_size100_200_approx/5_LinearSVC_approx1060/plot_dataset.png" width="200" alt="5_LinearSVC_approx1060"><img src="GaussianExperiment_5_size100_200_approx/6_SVC_rbf_approx1060/plot_dataset.png" width="200" alt="6_SVC_rbf_approx1060"><img src="GaussianExperiment_5_size100_200_approx/7_MLPClassifier_approx1060/plot_dataset.png" width="200" alt="7_MLPClassifier_approx1060">

<img src="GaussianExperiment_5_size100_200_approx/4_LogisticRegression_approx1060/plot_dataset_splitted.png" width="200" alt="4_LogisticRegression_approx1060"><img src="GaussianExperiment_5_size100_200_approx/5_LinearSVC_approx1060/plot_dataset_splitted.png" width="200" alt="5_LinearSVC_approx1060"><img src="GaussianExperiment_5_size100_200_approx/6_SVC_rbf_approx1060/plot_dataset_splitted.png" width="200" alt="6_SVC_rbf_approx1060"><img src="GaussianExperiment_5_size100_200_approx/7_MLPClassifier_approx1060/plot_dataset_splitted.png" width="200" alt="7_MLPClassifier_approx1060">

<img src="GaussianExperiment_5_size100_200_approx/4_LogisticRegression_approx1060/plot_shapley_values.png" width="200" alt="4_LogisticRegression_approx1060"><img src="GaussianExperiment_5_size100_200_approx/5_LinearSVC_approx1060/plot_shapley_values.png" width="200" alt="5_LinearSVC_approx1060"><img src="GaussianExperiment_5_size100_200_approx/6_SVC_rbf_approx1060/plot_shapley_values.png" width="200" alt="6_SVC_rbf_approx1060"><img src="GaussianExperiment_5_size100_200_approx/7_MLPClassifier_approx1060/plot_shapley_values.png" width="200" alt="7_MLPClassifier_approx1060">

<img src="GaussianExperiment_5_size100_200_approx/4_LogisticRegression_approx1060/plot_shapley_values_sorted.png" width="200" alt="4_LogisticRegression_approx1060"><img src="GaussianExperiment_5_size100_200_approx/5_LinearSVC_approx1060/plot_shapley_values_sorted.png" width="200" alt="5_LinearSVC_approx1060"><img src="GaussianExperiment_5_size100_200_approx/6_SVC_rbf_approx1060/plot_shapley_values_sorted.png" width="200" alt="6_SVC_rbf_approx1060"><img src="GaussianExperiment_5_size100_200_approx/7_MLPClassifier_approx1060/plot_shapley_values_sorted.png" width="200" alt="7_MLPClassifier_approx1060">

##### size: 400, permutations: 2400
<img src="GaussianExperiment_6_size400_approx/0_LogisticRegression_approx2400/plot_dataset.png" width="200" alt="0_LogisticRegression_approx2400"><img src="GaussianExperiment_6_size400_approx/1_LinearSVC_approx2400/plot_dataset.png" width="200" alt="1_LinearSVC_approx2400"><img src="GaussianExperiment_6_size400_approx/2_SVC_rbf_approx2400/plot_dataset.png" width="200" alt="2_SVC_rbf_approx2400"><img src="GaussianExperiment_6_size400_approx/3_MLPClassifier_approx2400/plot_dataset.png" width="200" alt="3_MLPClassifier_approx2400">

<img src="GaussianExperiment_6_size400_approx/0_LogisticRegression_approx2400/plot_dataset_splitted.png" width="200" alt="0_LogisticRegression_approx2400"><img src="GaussianExperiment_6_size400_approx/1_LinearSVC_approx2400/plot_dataset_splitted.png" width="200" alt="1_LinearSVC_approx2400"><img src="GaussianExperiment_6_size400_approx/2_SVC_rbf_approx2400/plot_dataset_splitted.png" width="200" alt="2_SVC_rbf_approx2400"><img src="GaussianExperiment_6_size400_approx/3_MLPClassifier_approx2400/plot_dataset_splitted.png" width="200" alt="3_MLPClassifier_approx2400">

<img src="GaussianExperiment_6_size400_approx/0_LogisticRegression_approx2400/plot_shapley_values.png" width="200" alt="0_LogisticRegression_approx2400"><img src="GaussianExperiment_6_size400_approx/1_LinearSVC_approx2400/plot_shapley_values.png" width="200" alt="1_LinearSVC_approx2400"><img src="GaussianExperiment_6_size400_approx/2_SVC_rbf_approx2400/plot_shapley_values.png" width="200" alt="2_SVC_rbf_approx2400"><img src="GaussianExperiment_6_size400_approx/3_MLPClassifier_approx2400/plot_shapley_values.png" width="200" alt="3_MLPClassifier_approx2400">

<img src="GaussianExperiment_6_size400_approx/0_LogisticRegression_approx2400/plot_shapley_values_sorted.png" width="200" alt="0_LogisticRegression_approx2400"><img src="GaussianExperiment_6_size400_approx/1_LinearSVC_approx2400/plot_shapley_values_sorted.png" width="200" alt="1_LinearSVC_approx2400"><img src="GaussianExperiment_6_size400_approx/2_SVC_rbf_approx2400/plot_shapley_values_sorted.png" width="200" alt="2_SVC_rbf_approx2400"><img src="GaussianExperiment_6_size400_approx/3_MLPClassifier_approx2400/plot_shapley_values_sorted.png" width="200" alt="3_MLPClassifier_approx2400">