# Task02 

### 时间

:calendar:2021年10月13日9:00~2021年10月19日21:00

### 内容

西瓜书第3章

### 目标

学习几种经典的线性模型

### 暂时可忽略内容

无



# 笔记

## 一元线性回归

### 前置知识

凸集

梯度

Hessian矩阵

证明f(x)是凸函数的定理

凸充分性定理

### 模型

给定数据集$D=\{(x_i,y_i)\}_{i=1}^m$，每个数据$x_i$**只有一个属性**。则模型为
$$
f(x_i)=wx_i+b,使得f(x_i)\approx y_i
$$

### 优化目标及模型参数求解

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
(w^*,b^*)={\underset {(w,b)}{\operatorname {arg\,max} }}\,lnL(w,b)={\underset {(w,b)}{\operatorname {arg\,min}}\sum_{i=1}^m(y_i-wx_i-b)^2}
$$
可以看出，**最小二乘法**和**极大似然**估计推导的**优化目标相同**。

### 求解过程推导

#### 1. 证明目标函数是凸函数

### 2. 求解$w,b$

## 参考资料

- [【吃瓜教程】《机器学习公式详解》（南瓜书）与西瓜书公式推导直播合集](https://www.bilibili.com/video/BV1Mh411e7VU)
- 周志华《机器学习》
- [南瓜书](https://github.com/datawhalechina/pumpkin-book/releases)

