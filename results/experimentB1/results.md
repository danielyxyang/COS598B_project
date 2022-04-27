# COS598 - Final Project
## Results of `experimentB1`

### Setup
- Dataset
    - Gaussian 1: $\mu_1 = \begin{pmatrix}1 \\ -1\end{pmatrix}$ and $\Sigma_1 = V_1 \Lambda_1 V_1^T$ with $\Lambda_1 = \begin{pmatrix}3 & 0 \\ 0 & 1\end{pmatrix}$ and $V_1 = \begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}$
    - Gaussian 2: $\mu_2 = \begin{pmatrix}-1 \\ 1\end{pmatrix}$ and $\Sigma_2 = V_2 \Lambda_2 V_2^T$ with $\Lambda_2 = \begin{pmatrix}3 & 0 \\ 0 & 1\end{pmatrix}$ and $V_2 = \begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}$
- Models
    - LogisticRegression (LR)
    - LinearSVC (SVC_lin)
    - SVC with RBF kernel (SVC_rbf)
    - MLPClassifier with (10, 10) layers (MLP)

### Exact Shapley values

\#| \| |size train|size test|num perm|seed|without| \| |size total|num eval| \| |LR|SVC_lin|SVC_rbf|MLP
-| - |-|-|-|-|-| - |-|-| - |-|-|-|-
1-size10_exact| \| |6|100|None|**0**|**full**| \| |20|20M| \| |0.7100 / 56:02|0.7700 / 22:43|0.5900 / 14:56|0.6750 / 3:33:36
1-size10_exact| \| |6|100|None|**0**|**1**| \| |18|4M| \| |0.6250 / 00:15|0.6800 / 00:13|0.5750 / 00:13|0.4350 / 00:13
1-size10_exact| \| |6|100|None|**0**|**2**| \| |16|1M| \| |0.5750 / 00:03|0.5800 / 00:03|0.5450 / 00:03|0.5400 / 00:03
1-size10_exact| \| |6|100|None|**0**|**3**| \| |14|230K| \| |0.5050 / 00:00|0.4400 / 00:00|0.5400 / 00:00|0.4250 / 00:00
1-size10_exact| \| |6|100|None|**1**|**full**| \| |20|20M| \| |0.8650 / 48:42|0.8650 / 22:46|0.7500 / 14:55|0.7650 / 3:30:48
1-size10_exact| \| |6|100|None|**1**|**1**| \| |18|4M| \| |0.8600 / 00:13|0.8650 / 00:14|0.7450 / 00:13|0.7300 / 00:15
1-size10_exact| \| |6|100|None|**1**|**2**| \| |16|1M| \| |0.8150 / 00:03|0.8100 / 00:03|0.7450 / 00:03|0.7250 / 00:03
1-size10_exact| \| |6|100|None|**1**|**3**| \| |14|230K| \| |0.6900 / 00:00|0.7250 / 00:00|0.7200 / 00:00|0.7250 / 00:00
1-size10_exact| \| |6|100|None|**2**|**full**| \| |20|20M| \| |0.8550 / 47:50|0.8750 / 24:21|0.8500 / 14:52|0.8450 / 7:22:45
1-size10_exact| \| |6|100|None|**2**|**1**| \| |18|4M| \| |0.8350 / 00:14|0.8400 / 00:13|0.8150 / 00:13|0.8650 / 00:16
1-size10_exact| \| |6|100|None|**2**|**2**| \| |16|1M| \| |0.7950 / 00:03|0.8250 / 00:03|0.7750 / 00:03|0.7700 / 00:03
1-size10_exact| \| |6|100|None|**2**|**3**| \| |14|230K| \| |0.7500 / 00:00|0.7850 / 00:00|0.6800 / 00:00|0.6100 / 00:00

#### GaussianExperimentB-1-size10_exact
##### LogisticRegression, seed 0
<img src="GaussianExperimentB-1-size10_exact/0-LogisticRegression_exact-full/plot_dataset.png" width="200" alt="0-LogisticRegression_exact-full"><img src="GaussianExperimentB-1-size10_exact/0-LogisticRegression_exact-without1/plot_dataset.png" width="200" alt="0-LogisticRegression_exact-without1"><img src="GaussianExperimentB-1-size10_exact/0-LogisticRegression_exact-without2/plot_dataset.png" width="200" alt="0-LogisticRegression_exact-without2"><img src="GaussianExperimentB-1-size10_exact/0-LogisticRegression_exact-without3/plot_dataset.png" width="200" alt="0-LogisticRegression_exact-without3">

<img src="GaussianExperimentB-1-size10_exact/0-LogisticRegression_exact-full/plot_shapley_values.png" width="200" alt="0-LogisticRegression_exact-full"><img src="GaussianExperimentB-1-size10_exact/0-LogisticRegression_exact-without1/plot_shapley_values.png" width="200" alt="0-LogisticRegression_exact-without1"><img src="GaussianExperimentB-1-size10_exact/0-LogisticRegression_exact-without2/plot_shapley_values.png" width="200" alt="0-LogisticRegression_exact-without2"><img src="GaussianExperimentB-1-size10_exact/0-LogisticRegression_exact-without3/plot_shapley_values.png" width="200" alt="0-LogisticRegression_exact-without3">

##### LogisticRegression, seed 1
<img src="GaussianExperimentB-1-size10_exact/1-LogisticRegression_exact-full/plot_dataset.png" width="200" alt="0-LogisticRegression_exact-full"><img src="GaussianExperimentB-1-size10_exact/1-LogisticRegression_exact-without1/plot_dataset.png" width="200" alt="0-LogisticRegression_exact-without1"><img src="GaussianExperimentB-1-size10_exact/1-LogisticRegression_exact-without2/plot_dataset.png" width="200" alt="0-LogisticRegression_exact-without2"><img src="GaussianExperimentB-1-size10_exact/1-LogisticRegression_exact-without3/plot_dataset.png" width="200" alt="0-LogisticRegression_exact-without3">

<img src="GaussianExperimentB-1-size10_exact/1-LogisticRegression_exact-full/plot_shapley_values.png" width="200" alt="0-LogisticRegression_exact-full"><img src="GaussianExperimentB-1-size10_exact/1-LogisticRegression_exact-without1/plot_shapley_values.png" width="200" alt="0-LogisticRegression_exact-without1"><img src="GaussianExperimentB-1-size10_exact/1-LogisticRegression_exact-without2/plot_shapley_values.png" width="200" alt="0-LogisticRegression_exact-without2"><img src="GaussianExperimentB-1-size10_exact/1-LogisticRegression_exact-without3/plot_shapley_values.png" width="200" alt="0-LogisticRegression_exact-without3">

##### LogisticRegression, seed 2
<img src="GaussianExperimentB-1-size10_exact/2-LogisticRegression_exact-full/plot_dataset.png" width="200" alt="0-LogisticRegression_exact-full"><img src="GaussianExperimentB-1-size10_exact/2-LogisticRegression_exact-without1/plot_dataset.png" width="200" alt="0-LogisticRegression_exact-without1"><img src="GaussianExperimentB-1-size10_exact/2-LogisticRegression_exact-without2/plot_dataset.png" width="200" alt="0-LogisticRegression_exact-without2"><img src="GaussianExperimentB-1-size10_exact/2-LogisticRegression_exact-without3/plot_dataset.png" width="200" alt="0-LogisticRegression_exact-without3">

<img src="GaussianExperimentB-1-size10_exact/2-LogisticRegression_exact-full/plot_shapley_values.png" width="200" alt="0-LogisticRegression_exact-full"><img src="GaussianExperimentB-1-size10_exact/2-LogisticRegression_exact-without1/plot_shapley_values.png" width="200" alt="0-LogisticRegression_exact-without1"><img src="GaussianExperimentB-1-size10_exact/2-LogisticRegression_exact-without2/plot_shapley_values.png" width="200" alt="0-LogisticRegression_exact-without2"><img src="GaussianExperimentB-1-size10_exact/2-LogisticRegression_exact-without3/plot_shapley_values.png" width="200" alt="0-LogisticRegression_exact-without3">

##### LinearSVC, seed 0
<img src="GaussianExperimentB-1-size10_exact/3-LinearSVC_exact-full/plot_dataset.png" width="200" alt="3-LinearSVC_exact-full"><img src="GaussianExperimentB-1-size10_exact/3-LinearSVC_exact-without1/plot_dataset.png" width="200" alt="3-LinearSVC_exact-without1"><img src="GaussianExperimentB-1-size10_exact/3-LinearSVC_exact-without2/plot_dataset.png" width="200" alt="3-LinearSVC_exact-without2"><img src="GaussianExperimentB-1-size10_exact/3-LinearSVC_exact-without3/plot_dataset.png" width="200" alt="3-LinearSVC_exact-without3">

<img src="GaussianExperimentB-1-size10_exact/3-LinearSVC_exact-full/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact-full"><img src="GaussianExperimentB-1-size10_exact/3-LinearSVC_exact-without1/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact-without1"><img src="GaussianExperimentB-1-size10_exact/3-LinearSVC_exact-without2/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact-without2"><img src="GaussianExperimentB-1-size10_exact/3-LinearSVC_exact-without3/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact-without3">

##### LinearSVC, seed 1
<img src="GaussianExperimentB-1-size10_exact/4-LinearSVC_exact-full/plot_dataset.png" width="200" alt="3-LinearSVC_exact-full"><img src="GaussianExperimentB-1-size10_exact/4-LinearSVC_exact-without1/plot_dataset.png" width="200" alt="3-LinearSVC_exact-without1"><img src="GaussianExperimentB-1-size10_exact/4-LinearSVC_exact-without2/plot_dataset.png" width="200" alt="3-LinearSVC_exact-without2"><img src="GaussianExperimentB-1-size10_exact/4-LinearSVC_exact-without3/plot_dataset.png" width="200" alt="3-LinearSVC_exact-without3">

<img src="GaussianExperimentB-1-size10_exact/4-LinearSVC_exact-full/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact-full"><img src="GaussianExperimentB-1-size10_exact/4-LinearSVC_exact-without1/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact-without1"><img src="GaussianExperimentB-1-size10_exact/4-LinearSVC_exact-without2/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact-without2"><img src="GaussianExperimentB-1-size10_exact/4-LinearSVC_exact-without3/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact-without3">

##### LinearSVC, seed 2
<img src="GaussianExperimentB-1-size10_exact/5-LinearSVC_exact-full/plot_dataset.png" width="200" alt="3-LinearSVC_exact-full"><img src="GaussianExperimentB-1-size10_exact/5-LinearSVC_exact-without1/plot_dataset.png" width="200" alt="3-LinearSVC_exact-without1"><img src="GaussianExperimentB-1-size10_exact/5-LinearSVC_exact-without2/plot_dataset.png" width="200" alt="3-LinearSVC_exact-without2"><img src="GaussianExperimentB-1-size10_exact/5-LinearSVC_exact-without3/plot_dataset.png" width="200" alt="3-LinearSVC_exact-without3">

<img src="GaussianExperimentB-1-size10_exact/5-LinearSVC_exact-full/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact-full"><img src="GaussianExperimentB-1-size10_exact/5-LinearSVC_exact-without1/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact-without1"><img src="GaussianExperimentB-1-size10_exact/5-LinearSVC_exact-without2/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact-without2"><img src="GaussianExperimentB-1-size10_exact/5-LinearSVC_exact-without3/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact-without3">

##### SVC_rbf, seed 0
<img src="GaussianExperimentB-1-size10_exact/6-SVC_rbf_exact-full/plot_dataset.png" width="200" alt="3-SVC_rbf_exact-full"><img src="GaussianExperimentB-1-size10_exact/6-SVC_rbf_exact-without1/plot_dataset.png" width="200" alt="3-SVC_rbf_exact-without1"><img src="GaussianExperimentB-1-size10_exact/6-SVC_rbf_exact-without2/plot_dataset.png" width="200" alt="3-SVC_rbf_exact-without2"><img src="GaussianExperimentB-1-size10_exact/6-SVC_rbf_exact-without3/plot_dataset.png" width="200" alt="3-SVC_rbf_exact-without3">

<img src="GaussianExperimentB-1-size10_exact/6-SVC_rbf_exact-full/plot_shapley_values.png" width="200" alt="3-SVC_rbf_exact-full"><img src="GaussianExperimentB-1-size10_exact/6-SVC_rbf_exact-without1/plot_shapley_values.png" width="200" alt="3-SVC_rbf_exact-without1"><img src="GaussianExperimentB-1-size10_exact/6-SVC_rbf_exact-without2/plot_shapley_values.png" width="200" alt="3-SVC_rbf_exact-without2"><img src="GaussianExperimentB-1-size10_exact/6-SVC_rbf_exact-without3/plot_shapley_values.png" width="200" alt="3-SVC_rbf_exact-without3">

##### SVC_rbf, seed 1
<img src="GaussianExperimentB-1-size10_exact/7-SVC_rbf_exact-full/plot_dataset.png" width="200" alt="3-SVC_rbf_exact-full"><img src="GaussianExperimentB-1-size10_exact/7-SVC_rbf_exact-without1/plot_dataset.png" width="200" alt="3-SVC_rbf_exact-without1"><img src="GaussianExperimentB-1-size10_exact/7-SVC_rbf_exact-without2/plot_dataset.png" width="200" alt="3-SVC_rbf_exact-without2"><img src="GaussianExperimentB-1-size10_exact/7-SVC_rbf_exact-without3/plot_dataset.png" width="200" alt="3-SVC_rbf_exact-without3">

<img src="GaussianExperimentB-1-size10_exact/7-SVC_rbf_exact-full/plot_shapley_values.png" width="200" alt="3-SVC_rbf_exact-full"><img src="GaussianExperimentB-1-size10_exact/7-SVC_rbf_exact-without1/plot_shapley_values.png" width="200" alt="3-SVC_rbf_exact-without1"><img src="GaussianExperimentB-1-size10_exact/7-SVC_rbf_exact-without2/plot_shapley_values.png" width="200" alt="3-SVC_rbf_exact-without2"><img src="GaussianExperimentB-1-size10_exact/7-SVC_rbf_exact-without3/plot_shapley_values.png" width="200" alt="3-SVC_rbf_exact-without3">

##### SVC_rbf, seed 2
<img src="GaussianExperimentB-1-size10_exact/8-SVC_rbf_exact-full/plot_dataset.png" width="200" alt="3-SVC_rbf_exact-full"><img src="GaussianExperimentB-1-size10_exact/8-SVC_rbf_exact-without1/plot_dataset.png" width="200" alt="3-SVC_rbf_exact-without1"><img src="GaussianExperimentB-1-size10_exact/8-SVC_rbf_exact-without2/plot_dataset.png" width="200" alt="3-SVC_rbf_exact-without2"><img src="GaussianExperimentB-1-size10_exact/8-SVC_rbf_exact-without3/plot_dataset.png" width="200" alt="3-SVC_rbf_exact-without3">

<img src="GaussianExperimentB-1-size10_exact/8-SVC_rbf_exact-full/plot_shapley_values.png" width="200" alt="3-SVC_rbf_exact-full"><img src="GaussianExperimentB-1-size10_exact/8-SVC_rbf_exact-without1/plot_shapley_values.png" width="200" alt="3-SVC_rbf_exact-without1"><img src="GaussianExperimentB-1-size10_exact/8-SVC_rbf_exact-without2/plot_shapley_values.png" width="200" alt="3-SVC_rbf_exact-without2"><img src="GaussianExperimentB-1-size10_exact/8-SVC_rbf_exact-without3/plot_shapley_values.png" width="200" alt="3-LinearSVC_exact-without3">

##### MLPClassifier, seed 0
<img src="GaussianExperimentB-1-size10_exact/9-MLPClassifier_exact-full/plot_dataset.png" width="200" alt="3-MLPClassifier_exact-full"><img src="GaussianExperimentB-1-size10_exact/9-MLPClassifier_exact-without1/plot_dataset.png" width="200" alt="3-MLPClassifier_exact-without1"><img src="GaussianExperimentB-1-size10_exact/9-MLPClassifier_exact-without2/plot_dataset.png" width="200" alt="3-MLPClassifier_exact-without2"><img src="GaussianExperimentB-1-size10_exact/9-MLPClassifier_exact-without3/plot_dataset.png" width="200" alt="3-MLPClassifier_exact-without3">

<img src="GaussianExperimentB-1-size10_exact/9-MLPClassifier_exact-full/plot_shapley_values.png" width="200" alt="3-MLPClassifier_exact-full"><img src="GaussianExperimentB-1-size10_exact/9-MLPClassifier_exact-without1/plot_shapley_values.png" width="200" alt="3-MLPClassifier_exact-without1"><img src="GaussianExperimentB-1-size10_exact/9-MLPClassifier_exact-without2/plot_shapley_values.png" width="200" alt="3-MLPClassifier_exact-without2"><img src="GaussianExperimentB-1-size10_exact/9-MLPClassifier_exact-without3/plot_shapley_values.png" width="200" alt="3-MLPClassifier_exact-without3">

##### MLPClassifier, seed 1
<img src="GaussianExperimentB-1-size10_exact/10-MLPClassifier_exact-full/plot_dataset.png" width="200" alt="3-MLPClassifier_exact-full"><img src="GaussianExperimentB-1-size10_exact/10-MLPClassifier_exact-without1/plot_dataset.png" width="200" alt="3-MLPClassifier_exact-without1"><img src="GaussianExperimentB-1-size10_exact/10-MLPClassifier_exact-without2/plot_dataset.png" width="200" alt="3-MLPClassifier_exact-without2"><img src="GaussianExperimentB-1-size10_exact/10-MLPClassifier_exact-without3/plot_dataset.png" width="200" alt="3-MLPClassifier_exact-without3">

<img src="GaussianExperimentB-1-size10_exact/10-MLPClassifier_exact-full/plot_shapley_values.png" width="200" alt="3-MLPClassifier_exact-full"><img src="GaussianExperimentB-1-size10_exact/10-MLPClassifier_exact-without1/plot_shapley_values.png" width="200" alt="3-MLPClassifier_exact-without1"><img src="GaussianExperimentB-1-size10_exact/10-MLPClassifier_exact-without2/plot_shapley_values.png" width="200" alt="3-MLPClassifier_exact-without2"><img src="GaussianExperimentB-1-size10_exact/10-MLPClassifier_exact-without3/plot_shapley_values.png" width="200" alt="3-MLPClassifier_exact-without3">

##### MLPClassifier, seed 2
<img src="GaussianExperimentB-1-size10_exact/11-MLPClassifier_exact-full/plot_dataset.png" width="200" alt="3-MLPClassifier_exact-full"><img src="GaussianExperimentB-1-size10_exact/11-MLPClassifier_exact-without1/plot_dataset.png" width="200" alt="3-MLPClassifier_exact-without1"><img src="GaussianExperimentB-1-size10_exact/11-MLPClassifier_exact-without2/plot_dataset.png" width="200" alt="3-MLPClassifier_exact-without2"><img src="GaussianExperimentB-1-size10_exact/11-MLPClassifier_exact-without3/plot_dataset.png" width="200" alt="3-MLPClassifier_exact-without3">

<img src="GaussianExperimentB-1-size10_exact/11-MLPClassifier_exact-full/plot_shapley_values.png" width="200" alt="3-MLPClassifier_exact-full"><img src="GaussianExperimentB-1-size10_exact/11-MLPClassifier_exact-without1/plot_shapley_values.png" width="200" alt="3-MLPClassifier_exact-without1"><img src="GaussianExperimentB-1-size10_exact/11-MLPClassifier_exact-without2/plot_shapley_values.png" width="200" alt="3-MLPClassifier_exact-without2"><img src="GaussianExperimentB-1-size10_exact/11-MLPClassifier_exact-without3/plot_shapley_values.png" width="200" alt="3-MLPClassifier_exact-without3">

---------------------------------------

### Approximate Shapley values

\#| \| |size train|size test|num perm|seed|without| \| |size total|num eval| \| |LR|SVC_lin|SVC_rbf|MLP
-| - |-|-|-|-|-| - |-|-| - |-|-|-|-
2-size100_approx| \| |100|1000|**460**|**0**|**full**| \| |200|92K| \| |0.8230 / 08:10|0.8245 / 04:50|0.7820 / 16:27|0.7744 / 2:02:41
2-size100_approx| \| |100|1000|**460**|**0**|**1**| \| |198|91K| \| |0.8235 / 07:48|0.8245 / 04:44|0.7677 / 15:35|0.7713 / 1:57:17
2-size100_approx| \| |100|1000|**460**|**0**|**5**| \| |190|87K| \| |0.8235 / 07:14|0.8220 / 04:32|0.7595 / 14:34|0.7578 / 1:52:19
2-size100_approx| \| |100|1000|**460**|**0**|**10**| \| |180|83K| \| |0.8230 / 06:45|0.8215 / 04:11|0.7565 / 13:22|0.7480 / 1:45:01
3-size200_approx| \| |200|1000|**1060**|**0**|**full**| \| |400|424K| \| |0.8285 / 37:34|0.8275 / 26:29|0.8105 / 2:13:56|0.7935 / 12:00:06
3-size200_approx| \| |200|1000|**1060**|**0**|**2**| \| |396|420K| \| |0.8285 / 34:17|0.8265 / 26:07|0.8060 / 2:08:17|TBD
3-size200_approx| \| |200|1000|**1060**|**0**|**10**| \| |380|403K| \| |0.8285 / 33:06|0.8265 / 24:56|0.7925 / 1:49:37|TBD
3-size200_approx| \| |200|1000|**1060**|**0**|**20**| \| |360|382K| \| |0.8285 / 31:06|0.8275 / 23:09|0.7860 / 1:39:28|TBD
4-size400_approx| \| |400|1000|**2400**|**0**|**full**| \| |800|1.9M| \| |0.8265 / 2:49:52|0.8260 / 2:21:42|0.8180 / 16:58:26|TBD
4-size400_approx| \| |400|1000|**2400**|**0**|**4**| \| |792|1.9M| \| |0.8265 / 2:34:45|0.8260 / 2:39:38|0.8181 / 15:52:32|TBD
4-size400_approx| \| |400|1000|**2400**|**0**|**20**| \| |760|1.8M| \| |0.8260 / 2:20:03|0.8270 / 2:13:51|TBD|TBD
4-size400_approx| \| |400|1000|**2400**|**0**|**40**| \| |720|1.7M| \| |0.8260 / 1:54:14|0.8270 / 2:04:22|TBD|TBD

#### GaussianExperimentB-2-size100_approx
##### LogisticRegression
<img src="GaussianExperimentB-2-size100_approx/0-LogisticRegression_approx460-full/plot_dataset.png" width="200" alt="0-LogisticRegression_approx460-full"><img src="GaussianExperimentB-2-size100_approx/0-LogisticRegression_approx460-without1/plot_dataset.png" width="200" alt="0-LogisticRegression_approx460-without1"><img src="GaussianExperimentB-2-size100_approx/0-LogisticRegression_approx460-without5/plot_dataset.png" width="200" alt="0-LogisticRegression_approx460-without5"><img src="GaussianExperimentB-2-size100_approx/0-LogisticRegression_approx460-without10/plot_dataset.png" width="200" alt="0-LogisticRegression_approx460-without10">

<img src="GaussianExperimentB-2-size100_approx/0-LogisticRegression_approx460-full/plot_shapley_values.png" width="200" alt="0-LogisticRegression_approx460-full"><img src="GaussianExperimentB-2-size100_approx/0-LogisticRegression_approx460-without1/plot_shapley_values.png" width="200" alt="0-LogisticRegression_approx460-without1"><img src="GaussianExperimentB-2-size100_approx/0-LogisticRegression_approx460-without5/plot_shapley_values.png" width="200" alt="0-LogisticRegression_approx460-without5"><img src="GaussianExperimentB-2-size100_approx/0-LogisticRegression_approx460-without10/plot_shapley_values.png" width="200" alt="0-LogisticRegression_approx460-without10">

##### LinearSVC
<img src="GaussianExperimentB-2-size100_approx/1-LinearSVC_approx460-full/plot_dataset.png" width="200" alt="1-LinearSVC_approx460-full"><img src="GaussianExperimentB-2-size100_approx/1-LinearSVC_approx460-without1/plot_dataset.png" width="200" alt="1-LinearSVC_approx460-without1"><img src="GaussianExperimentB-2-size100_approx/1-LinearSVC_approx460-without5/plot_dataset.png" width="200" alt="1-LinearSVC_approx460-without5"><img src="GaussianExperimentB-2-size100_approx/1-LinearSVC_approx460-without10/plot_dataset.png" width="200" alt="1-LinearSVC_approx460-without10">

<img src="GaussianExperimentB-2-size100_approx/1-LinearSVC_approx460-full/plot_shapley_values.png" width="200" alt="1-LinearSVC_approx460-full"><img src="GaussianExperimentB-2-size100_approx/1-LinearSVC_approx460-without1/plot_shapley_values.png" width="200" alt="1-LinearSVC_approx460-without1"><img src="GaussianExperimentB-2-size100_approx/1-LinearSVC_approx460-without5/plot_shapley_values.png" width="200" alt="1-LinearSVC_approx460-without5"><img src="GaussianExperimentB-2-size100_approx/1-LinearSVC_approx460-without10/plot_shapley_values.png" width="200" alt="1-LinearSVC_approx460-without10">

##### SVC_rbf
<img src="GaussianExperimentB-2-size100_approx/2-SVC_rbf_approx460-full/plot_dataset.png" width="200" alt="2-SVC_rbf_approx460-full"><img src="GaussianExperimentB-2-size100_approx/2-SVC_rbf_approx460-without1/plot_dataset.png" width="200" alt="2-SVC_rbf_approx460-without1"><img src="GaussianExperimentB-2-size100_approx/2-SVC_rbf_approx460-without5/plot_dataset.png" width="200" alt="2-SVC_rbf_approx460-without5"><img src="GaussianExperimentB-2-size100_approx/2-SVC_rbf_approx460-without10/plot_dataset.png" width="200" alt="2-SVC_rbf_approx460-without10">

<img src="GaussianExperimentB-2-size100_approx/2-SVC_rbf_approx460-full/plot_shapley_values.png" width="200" alt="2-SVC_rbf_approx460-full"><img src="GaussianExperimentB-2-size100_approx/2-SVC_rbf_approx460-without1/plot_shapley_values.png" width="200" alt="2-SVC_rbf_approx460-without1"><img src="GaussianExperimentB-2-size100_approx/2-SVC_rbf_approx460-without5/plot_shapley_values.png" width="200" alt="2-SVC_rbf_approx460-without5"><img src="GaussianExperimentB-2-size100_approx/2-SVC_rbf_approx460-without10/plot_shapley_values.png" width="200" alt="2-SVC_rbf_approx460-without10">

##### MLPClassifier
<img src="GaussianExperimentB-2-size100_approx/3-MLPClassifier_approx460-full/plot_dataset.png" width="200" alt="3-MLPClassifier_approx460-full"><img src="GaussianExperimentB-2-size100_approx/3-MLPClassifier_approx460-without1/plot_dataset.png" width="200" alt="3-MLPClassifier_approx460-without1"><img src="GaussianExperimentB-2-size100_approx/3-MLPClassifier_approx460-without5/plot_dataset.png" width="200" alt="3-MLPClassifier_approx460-without5"><img src="GaussianExperimentB-2-size100_approx/3-MLPClassifier_approx460-without10/plot_dataset.png" width="200" alt="3-MLPClassifier_approx460-without10">

<img src="GaussianExperimentB-2-size100_approx/3-MLPClassifier_approx460-full/plot_shapley_values.png" width="200" alt="3-MLPClassifier_approx460-full"><img src="GaussianExperimentB-2-size100_approx/3-MLPClassifier_approx460-without1/plot_shapley_values.png" width="200" alt="3-MLPClassifier_approx460-without1"><img src="GaussianExperimentB-2-size100_approx/3-MLPClassifier_approx460-without5/plot_shapley_values.png" width="200" alt="3-MLPClassifier_approx460-without5"><img src="GaussianExperimentB-2-size100_approx/3-MLPClassifier_approx460-without10/plot_shapley_values.png" width="200" alt="3-MLPClassifier_approx460-without10">

#### GaussianExperimentB-3-size200_approx
##### LogisticRegression
<img src="GaussianExperimentB-3-size200_approx/0-LogisticRegression_approx1060-full/plot_dataset.png" width="200" alt="0-LogisticRegression_approx1060-full"><img src="GaussianExperimentB-3-size200_approx/0-LogisticRegression_approx1060-without2/plot_dataset.png" width="200" alt="0-LogisticRegression_approx1060-without2"><img src="GaussianExperimentB-3-size200_approx/0-LogisticRegression_approx1060-without10/plot_dataset.png" width="200" alt="0-LogisticRegression_approx1060-without10"><img src="GaussianExperimentB-3-size200_approx/0-LogisticRegression_approx1060-without20/plot_dataset.png" width="200" alt="0-LogisticRegression_approx1060-without20">

<img src="GaussianExperimentB-3-size200_approx/0-LogisticRegression_approx1060-full/plot_shapley_values.png" width="200" alt="0-LogisticRegression_approx1060-full"><img src="GaussianExperimentB-3-size200_approx/0-LogisticRegression_approx1060-without2/plot_shapley_values.png" width="200" alt="0-LogisticRegression_approx1060-without2"><img src="GaussianExperimentB-3-size200_approx/0-LogisticRegression_approx1060-without10/plot_shapley_values.png" width="200" alt="0-LogisticRegression_approx1060-without10"><img src="GaussianExperimentB-3-size200_approx/0-LogisticRegression_approx1060-without20/plot_shapley_values.png" width="200" alt="0-LogisticRegression_approx1060-without20">

##### LinearSVC
<img src="GaussianExperimentB-3-size200_approx/1-LinearSVC_approx1060-full/plot_dataset.png" width="200" alt="1-LinearSVC_approx1060-full"><img src="GaussianExperimentB-3-size200_approx/1-LinearSVC_approx1060-without2/plot_dataset.png" width="200" alt="1-LinearSVC_approx1060-without2"><img src="GaussianExperimentB-3-size200_approx/1-LinearSVC_approx1060-without10/plot_dataset.png" width="200" alt="1-LinearSVC_approx1060-without10"><img src="GaussianExperimentB-3-size200_approx/1-LinearSVC_approx1060-without20/plot_dataset.png" width="200" alt="1-LinearSVC_approx1060-without20">

<img src="GaussianExperimentB-3-size200_approx/1-LinearSVC_approx1060-full/plot_shapley_values.png" width="200" alt="1-LinearSVC_approx1060-full"><img src="GaussianExperimentB-3-size200_approx/1-LinearSVC_approx1060-without2/plot_shapley_values.png" width="200" alt="1-LinearSVC_approx1060-without2"><img src="GaussianExperimentB-3-size200_approx/1-LinearSVC_approx1060-without10/plot_shapley_values.png" width="200" alt="1-LinearSVC_approx1060-without10"><img src="GaussianExperimentB-3-size200_approx/1-LinearSVC_approx1060-without20/plot_shapley_values.png" width="200" alt="1-LinearSVC_approx1060-without20">

##### SVC_rbf
<img src="GaussianExperimentB-3-size200_approx/2-SVC_rbf_approx1060-full/plot_dataset.png" width="200" alt="2-SVC_rbf_approx1060-full"><img src="GaussianExperimentB-3-size200_approx/2-SVC_rbf_approx1060-without2/plot_dataset.png" width="200" alt="2-SVC_rbf_approx1060-without2"><img src="GaussianExperimentB-3-size200_approx/2-SVC_rbf_approx1060-without10/plot_dataset.png" width="200" alt="2-SVC_rbf_approx1060-without10"><img src="GaussianExperimentB-3-size200_approx/2-SVC_rbf_approx1060-without20/plot_dataset.png" width="200" alt="2-SVC_rbf_approx1060-without20">

<img src="GaussianExperimentB-3-size200_approx/2-SVC_rbf_approx1060-full/plot_shapley_values.png" width="200" alt="2-SVC_rbf_approx1060-full"><img src="GaussianExperimentB-3-size200_approx/2-SVC_rbf_approx1060-without2/plot_shapley_values.png" width="200" alt="2-SVC_rbf_approx1060-without2"><img src="GaussianExperimentB-3-size200_approx/2-SVC_rbf_approx1060-without10/plot_shapley_values.png" width="200" alt="2-SVC_rbf_approx1060-without10"><img src="GaussianExperimentB-3-size200_approx/2-SVC_rbf_approx1060-without20/plot_shapley_values.png" width="200" alt="2-SVC_rbf_approx1060-without20">

##### MLPClassifier
<img src="GaussianExperimentB-3-size200_approx/3-MLPClassifier_approx1060-full/plot_dataset.png" width="200" alt="3-MLPClassifier_approx1060-full"><img src="GaussianExperimentB-3-size200_approx/3-MLPClassifier_approx1060-without2/plot_dataset.png" width="200" alt="3-MLPClassifier_approx1060-without2"><img src="GaussianExperimentB-3-size200_approx/3-MLPClassifier_approx1060-without10/plot_dataset.png" width="200" alt="3-MLPClassifier_approx1060-without10"><img src="GaussianExperimentB-3-size200_approx/3-MLPClassifier_approx1060-without20/plot_dataset.png" width="200" alt="3-MLPClassifier_approx1060-without20">

<img src="GaussianExperimentB-3-size200_approx/3-MLPClassifier_approx1060-full/plot_shapley_values.png" width="200" alt="3-MLPClassifier_approx1060-full"><img src="GaussianExperimentB-3-size200_approx/3-MLPClassifier_approx1060-without2/plot_shapley_values.png" width="200" alt="3-MLPClassifier_approx1060-without2"><img src="GaussianExperimentB-3-size200_approx/3-MLPClassifier_approx1060-without10/plot_shapley_values.png" width="200" alt="3-MLPClassifier_approx1060-without10"><img src="GaussianExperimentB-3-size200_approx/3-MLPClassifier_approx1060-without20/plot_shapley_values.png" width="200" alt="3-MLPClassifier_approx1060-without20">

#### GaussianExperimentB-4-size200_approx
##### LogisticRegression
<img src="GaussianExperimentB-4-size400_approx/0-LogisticRegression_approx2400-full/plot_dataset.png" width="200" alt="0-LogisticRegression_approx2400-full"><img src="GaussianExperimentB-4-size400_approx/0-LogisticRegression_approx2400-without4/plot_dataset.png" width="200" alt="0-LogisticRegression_approx2400-without4"><img src="GaussianExperimentB-4-size400_approx/0-LogisticRegression_approx2400-without20/plot_dataset.png" width="200" alt="0-LogisticRegression_approx2400-without20"><img src="GaussianExperimentB-4-size400_approx/0-LogisticRegression_approx2400-without40/plot_dataset.png" width="200" alt="0-LogisticRegression_approx2400-without40">

<img src="GaussianExperimentB-4-size400_approx/0-LogisticRegression_approx2400-full/plot_shapley_values.png" width="200" alt="0-LogisticRegression_approx2400-full"><img src="GaussianExperimentB-4-size400_approx/0-LogisticRegression_approx2400-without4/plot_shapley_values.png" width="200" alt="0-LogisticRegression_approx2400-without4"><img src="GaussianExperimentB-4-size400_approx/0-LogisticRegression_approx2400-without20/plot_shapley_values.png" width="200" alt="0-LogisticRegression_approx2400-without20"><img src="GaussianExperimentB-4-size400_approx/0-LogisticRegression_approx2400-without40/plot_shapley_values.png" width="200" alt="0-LogisticRegression_approx2400-without40">

##### LinearSVC
<img src="GaussianExperimentB-4-size400_approx/1-LinearSVC_approx2400-full/plot_dataset.png" width="200" alt="1-LinearSVC_approx2400-full"><img src="GaussianExperimentB-4-size400_approx/1-LinearSVC_approx2400-without4/plot_dataset.png" width="200" alt="1-LinearSVC_approx2400-without4"><img src="GaussianExperimentB-4-size400_approx/1-LinearSVC_approx2400-without20/plot_dataset.png" width="200" alt="1-LinearSVC_approx2400-without20"><img src="GaussianExperimentB-4-size400_approx/1-LinearSVC_approx2400-without40/plot_dataset.png" width="200" alt="1-LinearSVC_approx2400-without40">

<img src="GaussianExperimentB-4-size400_approx/1-LinearSVC_approx2400-full/plot_shapley_values.png" width="200" alt="1-LinearSVC_approx2400-full"><img src="GaussianExperimentB-4-size400_approx/1-LinearSVC_approx2400-without4/plot_shapley_values.png" width="200" alt="1-LinearSVC_approx2400-without4"><img src="GaussianExperimentB-4-size400_approx/1-LinearSVC_approx2400-without20/plot_shapley_values.png" width="200" alt="1-LinearSVC_approx2400-without20"><img src="GaussianExperimentB-4-size400_approx/1-LinearSVC_approx2400-without40/plot_shapley_values.png" width="200" alt="1-LinearSVC_approx2400-without40">

##### SVC_rbf
<img src="GaussianExperimentB-4-size400_approx/2-SVC_rbf_approx2400-full/plot_dataset.png" width="200" alt="2-SVC_rbf_approx2400-full"><img src="GaussianExperimentB-4-size400_approx/2-SVC_rbf_approx2400-without4/plot_dataset.png" width="200" alt="2-SVC_rbf_approx2400-without4"><img src="GaussianExperimentB-4-size400_approx/2-SVC_rbf_approx2400-without20/plot_dataset.png" width="200" alt="2-SVC_rbf_approx2400-without20"><img src="GaussianExperimentB-4-size400_approx/2-SVC_rbf_approx2400-without40/plot_dataset.png" width="200" alt="2-SVC_rbf_approx2400-without40">

<img src="GaussianExperimentB-4-size400_approx/2-SVC_rbf_approx2400-full/plot_shapley_values.png" width="200" alt="2-SVC_rbf_approx2400-full"><img src="GaussianExperimentB-4-size400_approx/2-SVC_rbf_approx2400-without4/plot_shapley_values.png" width="200" alt="2-SVC_rbf_approx2400-without4"><img src="GaussianExperimentB-4-size400_approx/2-SVC_rbf_approx2400-without20/plot_shapley_values.png" width="200" alt="2-SVC_rbf_approx2400-without20"><img src="GaussianExperimentB-4-size400_approx/2-SVC_rbf_approx2400-without40/plot_shapley_values.png" width="200" alt="2-SVC_rbf_approx2400-without40">

##### MLPClassifier
<img src="GaussianExperimentB-4-size400_approx/3-MLPClassifier_approx2400-full/plot_dataset.png" width="200" alt="3-MLPClassifier_approx2400-full"><img src="GaussianExperimentB-4-size400_approx/3-MLPClassifier_approx2400-without4/plot_dataset.png" width="200" alt="3-MLPClassifier_approx2400-without4"><img src="GaussianExperimentB-4-size400_approx/3-MLPClassifier_approx2400-without20/plot_dataset.png" width="200" alt="3-MLPClassifier_approx2400-without20"><img src="GaussianExperimentB-4-size400_approx/3-MLPClassifier_approx2400-without40/plot_dataset.png" width="200" alt="3-MLPClassifier_approx2400-without40">

<img src="GaussianExperimentB-4-size400_approx/3-MLPClassifier_approx2400-full/plot_shapley_values.png" width="200" alt="3-MLPClassifier_approx2400-full"><img src="GaussianExperimentB-4-size400_approx/3-MLPClassifier_approx2400-without4/plot_shapley_values.png" width="200" alt="3-MLPClassifier_approx2400-without4"><img src="GaussianExperimentB-4-size400_approx/3-MLPClassifier_approx2400-without20/plot_shapley_values.png" width="200" alt="3-MLPClassifier_approx2400-without20"><img src="GaussianExperimentB-4-size400_approx/3-MLPClassifier_approx2400-without40/plot_shapley_values.png" width="200" alt="3-MLPClassifier_approx2400-without40">