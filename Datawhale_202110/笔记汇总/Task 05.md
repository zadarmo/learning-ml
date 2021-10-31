# Task05

### 时间

:calendar:2021年10月28日9:00~2021年10月31日21:00

### 内容

西瓜书第6章6.1\~6.2、6.4\~6.5

### 目标

学习支持向量机基本概念

### 暂时可忽略内容

无



# 笔记

## 一、样本空间中，任意点到超平面的距离推导

样本空间中，划分超平面可通过如下线性方程来描述：
$$
\boldsymbol w^T \boldsymbol x +b=0
$$
所以可以将超平面记为$(\boldsymbol w, b)$。

任意点到超平面$(\boldsymbol w, b)$的距离为
$$
r=\frac{|\boldsymbol w^T \boldsymbol x +b|}{||\boldsymbol w||}
$$
推导过程如下：

![image-20211031170434628](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211031170434628.png)

## 二、几何间隔

对于数据集$X$，$(\boldsymbol x_i, y_i), y_i\in \{-1,1 \}$。样本点$(\boldsymbol x_i, y_i)$关于超平面的几何间隔为
$$
\gamma_i=\frac{y_i(\boldsymbol w^T \boldsymbol x_i+b)}{||\boldsymbol w||}
$$
数据集$X$关于超平面的几何间隔为
$$
\gamma = min \gamma_i
$$

## 三、支持向量机

策略：给定线性可分数据集$X$，设$X$中几何间隔最小的样本为$(\boldsymbol x_{min}, y_{min})$，那么支持向量机找超平面的过程可以转换：
$$
max \gamma &\\
s.t. \gamma_i \ge \gamma
$$
然后可以经过如下变换：

![image-20211031181812445](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211031181812445.png)

进一步转换为求最小值问题
$$
min \frac{1}{2}||\boldsymbol w||^2 \\
s.t. 1-y_i(\boldsymbol w ^T \boldsymbol x_i + b) \le 0
$$
此问题为凸优化问题。在支持向量机中，通常采用拉格朗日对偶来求解。

为什么通常采用拉格朗日对偶呢？

![image-20211031184902713](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211031184902713.png)

## 四、拉格朗日对偶

凸优化问题：

![image-20211031182150559](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211031182150559.png)

对于这种优化问题（不一定是凸优化），其**拉格朗日对偶函数**为
$$
\Gamma(\boldsymbol \mu, \boldsymbol \lambda)=inf L(\boldsymbol x, \boldsymbol \mu, \boldsymbol \lambda)=inf(f(\boldsymbol x) + \sum_{i=1}^m\mu_ig_i(\boldsymbol x) + \sum_{j=1}^n\lambda_jh_j(\boldsymbol x))
$$
该函数有如下性质：

- 无论上述问题是否为凸优化问题，其对偶函数恒为凹函数
- 当$\boldsymbol \mu \ge 0 $时，该函数构成了上述优化问题最优值$p^*$的下界，也即$\Gamma(\boldsymbol \mu, \lambda) \le p^*$

定义**拉格朗日对偶问题**为
$$
max \Gamma(\boldsymbol \mu, \boldsymbol \lambda) \\
s.t. \boldsymbol \mu > 0
$$
该优化问题最优解为$d^*$，

- 当$d^* \le p^*$时，称为弱对偶性
- 当$d^* = p^*$时，称为强对偶性

KKT条件

![image-20211031184049572](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211031184049572.png)

## 五、软间隔

在现实任务中，**线性不可分的情形才是最常见的，因此需要允许支持向量机犯错。**软间隔，就是允许部分样本不满足下式约束条件
$$
min \frac {1}{2}||\boldsymbol w||^2\\
s.t. y_i(\boldsymbol w ^T \boldsymbol x_i+b) \ge 1
$$
因此，可以将必须严格执行的约束条件转换为具有一定灵活性的损失函数。合格的损失函数要求如下

- 当满足约束条件时，损失为0
- 当不满足约束条件时，损失不为0，且损失与其违反约束条件的程度成正比

软间隔的损失函数如下：
$$
min \frac {1}{2}||\boldsymbol w||^2 + C\sum_{i=1}^m ℓ_{0/1}(y_i(\boldsymbol w ^T \boldsymbol x_i+b)-1	)
$$
其中，$C>0$是一个常数，用来调节损失权重，$ℓ_{0/1}$是"0/1损失函数"
$$
ℓ_{0/1}(z)=1 \space if z<0,else0
$$
由于$ℓ_{0/1}$非凸、不连续，数学性质不好，使得上式不容易求解，因此常用一些数学性质较好的“替代损失函数”来代替$ℓ_{0/1}$。软间隔支持向量机通常采用hinge（合页）损失来代替
$$
hinge损失：ℓ_{hinge}(z)=max(0,1-z)
$$
替换之后，变成如下式子

![image-20211031192618565](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211031192618565.png)

引入松弛变量$\xi _i$，则上述问题转换为

![image-20211031192810527](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211031192810527.png)

## 六、支持向量回归

相比于线性回归用一条线来拟合训练样本，支持向量回归（SVR）采用一个以$f(\boldsymbol w ^T \boldsymbol  x + b)$为中心，宽度为$2\epsilon$的间隔带，来拟合训练样本。

落在带子上的样本不计算损失，不在袋子上的以偏离带子的距离作为损失。

SVR优化问题可以写为
$$
min \frac {1}{2}||\boldsymbol w||^2 + C\sum_{i=1}^m ℓ_{\epsilon}(f(\boldsymbol x_i)-y_i)
$$
其中，
$$
ℓ_{\epsilon}= max(0, |z|-\epsilon)
$$
引入松弛变量

![image-20211031200746535](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211031200746535.png)



则SVR优化问题可改写为![image-20211031200800267](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211031200800267.png)