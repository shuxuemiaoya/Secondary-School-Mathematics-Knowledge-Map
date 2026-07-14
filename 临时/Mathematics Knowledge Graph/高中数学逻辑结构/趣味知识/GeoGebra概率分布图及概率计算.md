# 信息技术应用

# 概率分布图及概率计算

利用GeoGebra动态教学软件,可以画二项分布、超几何分布、正态分布等概率分布图,计算随机变量取值于某区间内的概率。

打开软件,进入GeoGebra的界面,点击右侧边框中的小三角,在显示的经典菜单中选择"概率统计"。

1. 二项分布

选择二项分布,输入试验次数  $n = 20$  及成功概率  $p = 0.5$  ,即  $B(20,0.5)$  如图1,绘图区显示二项概率分布图,右侧显示分布列,输入随机变量的取值范围,窗口底部显示随机变量落在该范围的概率,例如

$$
P(8\leqslant X\leqslant 12) = 0.7368.
$$

![](images/7e9d7eaff6587a5e4aa49503eab032b3e17dbc416b29edf16a5e9332fb6ef2c9.jpg)  
图1

![](images/e4dcf8af32e5fea10f32209aa11c3425f19900b7dc03bbfbb00d218f01dd4bdb.jpg)  
图2

2. 超几何分布

选择超几何分布,输入总体  $N = 100$  ,  $M = 10$  及样本量  $n = 30$  ,即  $h(30,100,10)$  。如图2,绘图区显示超几何概率分布图,右侧显示分布列,输入随机变量的取值范围,窗口底部显示随机变量落在该范围的概率,例如

$$
P(1\leqslant X\leqslant 5) = 0.9383.
$$

3. 正态分布

选择正态分布,输入均值  $\mu = 0$  ,标准差  $\sigma = 1$  ,即  $N(0,1)$  。如图3,绘图区显示正态密度曲线图,输入随机变量的取值范围,窗口底部显示随机变量落在该范围的概率,例如

$$
\begin{array}{l}P(-1\leqslant X\leqslant 1) = 0.6827, \\ P(-2\leqslant X\leqslant 2) = 0.9545, \\ P(-3\leqslant X\leqslant 3) = 0.9973. \end{array}
$$

![](images/a6c1764121dac395ee0a3f1a848b4ba30d2a7db78ed6deff7b40917929ca5751.jpg)  
图3

通过窗口左下角的按钮,还可以求变量落在单边区间内的概率,例如

$$
P(X\leqslant 1.5) = 0.9332.
$$

请你再选择一些正态分布  $N(\mu ,\sigma^{2})$  ,分别计算  $P(\mu - \sigma \leqslant X\leqslant \mu +\sigma)$ $P(\mu - 2\sigma \leqslant X\leqslant \mu +2\sigma)$  ,  $P(\mu - 3\sigma \leqslant X\leqslant \mu +3\sigma)$  的值,并总结这些值的规律