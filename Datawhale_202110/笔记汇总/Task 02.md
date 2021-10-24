# Task02 

### 时间

:calendar:2021年10月13日9:00~2021年10月21日21:00

### 内容

西瓜书第3章3.1~3.4

### 目标

学习几种经典的线性模型

### 暂时可忽略内容

无



# 笔记

## 一、一元线性回归

### 1. 前置知识

凸集

梯度

Hessian矩阵

证明f(x)是凸函数的定理

凸充分性定理

### 2. 模型

给定数据集$D=\{(x_i,y_i)\}_{i=1}^m$，每个数据$x_i$**只有一个属性**。则模型为
$$
f(x_i)=wx_i+b,使得f(x_i)\approx y_i
$$

### 3. 优化目标及模型参数求解

#### 最小二乘法

目标函数采用均方误差，即
$$
E_{(w,b)}=\sum_{i=1}^m(f(x_i)-y_i)^2=\sum_{i=1}^m(y_i-wx_i-b)^2
$$
通过最小化目标函数求解模型参数$w,b$，称为**最小二乘法**
$$
(w^*,b^*)={\underset {(w,b)}{\operatorname {arg\,min} }}\,E_{(w,b)}={\underset {(w,b)}{\operatorname {arg\,min}}\sum_{i=1}^m(y_i-wx_i-b)^2}
$$

#### 极大似然估计

对于线性回归来说，模型也可以假设为
$$
y=wx+b+\epsilon 
$$
其中$\epsilon $为不受控制的随机误差（有多种因素共同决定），通常假设其服从均值为0的正态分布$\epsilon \sim N(0,\sigma^2)$（高斯提出的，也可以用中心极限定理解释）。所以$\epsilon $的概率密度函数为
$$
p(\epsilon )=\frac {1}{\sqrt{2\pi \sigma}}exp(-\frac {\epsilon ^2}{2\sigma^2})
$$
若将$\epsilon $用$y-(wx+b)$等价替换可得，
$$
p(y )=\frac {1}{\sqrt{2\pi \sigma}}exp(-\frac {(y-(wx+b))^2}{2\sigma^2})
$$
上式可以看做$y\sim N(wx+b,\sigma^2)$。下面便可以用**极大似然估计**来估计$w$和$b$的值。似然函数为
$$
L(w,b)=\prod_{i=1}^mp(y_i)=\prod_{i=1}^m \frac {1}{\sqrt{2\pi \sigma}}exp(-\frac {(y_i-(wx_i+b))^2}{2\sigma^2})
$$

$$ {aligned}
ln{L(w,b)}&=\sum_{i=1}^mln\frac {1}{\sqrt{2\pi \sigma}}exp(-\frac {(y_i-(wx_i+b))^2}{2\sigma^2})  \\
&=\sum_{i=1}^mln \frac {1}{\sqrt{2\pi \sigma}}+\sum_{i=1}^mlnexp(-\frac {(y_i-(wx_i+b))^2}{2\sigma^2}) \\
&=mln \frac {1}{\sqrt{2\pi \sigma}}-\frac{1}{2\sigma^2}\sum_{i=1}^m(y_i-(wx_i+b))^2
$$ {aligned}

最大化$lnL(w,b)$等价于最小化$\sum_{i=1}^m(y_i-(wx_i+b))^2$，即
$$
(w^*,b^*)={\underset {(w,b)}{\operatorname {arg\,max} }}\,lnL(w,b)={\underset {(w,b)}{\operatorname {arg\,min}}\sum_{i=1}^m(y_i-(wx_i+b))^2}
$$
可以看出，**最小二乘法**和**极大似然**估计推导的**优化目标相同**。

### 4. 求解过程推导

#### （1）证明目标函数是凸函数

这里用到两个定理（不严谨的说法）：

- 若目标函数的Hessian矩阵是半正定的，则该函数是凸函数
- 若矩阵的所有顺序主子式非负，则该矩阵是半正定的

要证明目标函数是凸函数，只需证明目标函数的Hessian矩阵是半正定的。证明过程如下：

![img](file:///C:\Users\destiny\Documents\Tencent Files\240412375\Image\C2C\Image1\06EDC2F510A77B46B23CA4CA8BD1A262.jpg![image-20211016003606264](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211016003606264.png)



### （2）求解$w,b$

这里用到凸充分性定理：

- 若$f(x)$是凸函数，且$f(\boldsymbol x)$一阶连续可微，则$\boldsymbol x^*$是全局最优解的充分必要条件是$\nabla f(\boldsymbol x^*)=0$

所以，根据$E(w,b)$梯度为0，求解$w,b$的过程如下：

![image-20211016004932407](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211016004932407.png)

## 二、多元线性回归

### 1. 一元到多元线性回归的推导

#### 损失函数的推导

多元和一元的区别就在于数据有多个属性。推导过程中涉及到两次**向量化**，再向量化后就可以用$Python$中$numpy$加速运算，这是很重要的技巧。

推导过程如下：

![image-20211016014234093](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211016014234093.png)

#### 证明损失函数为凸函数

同样，证明损失函数为凸函数需证明其Hessian矩阵为正定矩阵。

推导过程如下：

![image-20211017192748610](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211017192748610.png)

### 求解$\hat w$

同样，另偏导数为0，求解$\hat {\boldsymbol w}$。

求解过程如下：

![image-20211017193306695](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211017193306695.png)

## 三、对数几率回归

### 1. 模型

通过Sigmoid函数将线性回归模型的输出映射到[0,1]。Sigmoid函数
$$
y=\frac{1}{1+e^{-z}}
$$
映射后的输出为
$$
y=\frac{1}{1+e^{\boldsymbol w^T \boldsymbol x+b}}
$$

### 2. 策略

#### 极大似然估计

通过极大似然估计推导优化目标，过程如下：

![IMG_20211018_224500](C:\Users\destiny\Documents\Tencent Files\240412375\FileRecv\MobileFile\IMG_20211018_224500.jpg)

#### 信息论

待完成

### 3. 算法

梯度下降和牛顿法（待完成）

## 四、线性判别分析（LDA）

对于二分类问题来说，LDA是希望找到一个方向，当样本都朝这个方向投影时，

- 异类样本中心尽可能远（1）
- 同类样本方差尽可能小（2）

### 1. 目标函数推导

最大化（1）、最小化（2），并进行优化目标的合并（实际就是二者组成一个分数）。

推导过程如下：

![IMG_20211019_002440](C:\Users\destiny\Documents\Tencent Files\240412375\FileRecv\MobileFile\IMG_20211019_002440.jpg)

通过观察发现，目标函数和$\boldsymbol w$的长度没关系。所以不失一般性，可以令分母（分母是一个标量）为1。

### 2. 参数求解

在求解带约束的优化问题时，可以利用**拉格朗日乘子法**求解。

推导过程如下：

![IMG_20211019_002505](C:\Users\destiny\Documents\Tencent Files\240412375\FileRecv\MobileFile\IMG_20211019_002505.jpg)

## 参考资料

- [【吃瓜教程】《机器学习公式详解》（南瓜书）与西瓜书公式推导直播合集](https://www.bilibili.com/video/BV1Mh411e7VU)
- 周志华《机器学习》
- [南瓜书](https://github.com/datawhalechina/pumpkin-book/releases)

