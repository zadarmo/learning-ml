# Task04

### 时间

:calendar:2021年10月25日9:00~2021年10月27日21:00

### 内容

西瓜书第5章5.1~5.3

### 目标

学习深度学习

### 暂时可忽略内容

无



# 笔记

## 一、M-P神经元

接收n个输入，并给各个输入赋予权重计算加权和，然后和自身特有阈值$\theta$进行比较（作减法），最后经过激活函数（模拟“抑制”和“激活”）处理的二到输出
$$
y=f(\sum_{i=1}^nw_ix_i-\theta)=f(\boldsymbol{w}^T \boldsymbol{x}+b)
$$
其本质，就是线性模型再套一层激活函数：

- 如果激活函数为阶跃函数，则为**感知机**模型
- 如果激活函数为sigmoid，则为**对数几率回归**模型

## 二、感知机

### 1. 模型

感知机模型是激活函数为sgn（阶跃函数）的神经元
$$
y=sgn(\boldsymbol{w}^T \boldsymbol{x}-\theta)
$$
给定线性可分的数据集$T$，感知机的学习目标是求得能对数据集$T$中的正负样本完全正确划分的超平面，其中$\boldsymbol{w}^T \boldsymbol{x}-\theta$即为超平面方程。（下图为超平面实例）

![image-20211027224054342](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211027224054342.png)

这个超平面具有以下特征：

- 超平面不唯一
- 法向量$\boldsymbol w$垂直于超平面
- 法向量$\boldsymbol w$和位移项$b$确定一个唯一超平面
- 法向量$\boldsymbol w$指向的那一半空间为正空间，另一半为负空间

### 2. 策略

随机初始$\boldsymbol {w},b$，将样本带入模型找出误分类样本（记为集合$M$）。给定某个误分类样本$x$，分错的情况分为以下两种：

- $\boldsymbol{w}^T \boldsymbol{x}-\theta \geqslant 0$，模型输出$\hat y = 1$，样本真实标记$y=0$
- $\boldsymbol{w}^T \boldsymbol{x}-\theta < 0$，模型输出$\hat y = 1$，样本真实标记$y=0$

这两种情况下，以下等式恒成立
$$
(\hat y - y)(\boldsymbol{w}^T \boldsymbol{x}-\theta)\geqslant0
$$
**由于该式恒大于等于0，所以每多一个误分类样本时，这个值就会变大。**

所以给定数据集$T$，其损失函数可定义为
$$
L(\boldsymbol w, \theta)=\sum_{\boldsymbol x \in M}(\hat y - y)(\boldsymbol{w}^T \boldsymbol{x}-\theta)
$$
将$\theta$看做输入为-1的哑结点
$$
-\theta=-1*w_{n+1}=x_{n+1}*w_{n+1}
$$
则极小化损失函数可转化为
$$
minL(\boldsymbol w)=min\sum_{x_i\in M}(\hat {y_i}-y_i)\boldsymbol w^T \boldsymbol x_i
$$

### 3. 算法

$L(\boldsymbol w)$的梯度为
$$
\grad_wL(\boldsymbol w)=\sum_{x_i\in M}(\hat {y_i}-y_i)\boldsymbol x_i
$$
感知机采用的是**随机梯度下降**，也就是极小化过程中不是使所有的误分类点梯度下降，而是随机选取一个误分类点使其梯度下降。所以权重$\boldsymbol w$的更新公式为
$$
\boldsymbol w\leftarrow \boldsymbol w + \Delta\boldsymbol w \\
\Delta\boldsymbol w = -\eta(\hat {y_i}-y_i)\boldsymbol x_i
$$

## 三、神经网络

神经网络可以看作一个特征加工函数
$$
\boldsymbol x\in \mathbb{R}^d \rightarrow NN(\boldsymbol x)\rightarrow \boldsymbol y = \boldsymbol x^* \in \mathbb {R}^l
$$
![image-20211027224456755](C:\Users\destiny\AppData\Roaming\Typora\typora-user-images\image-20211027224456755.png)

假设多层前馈网络中的激活函数全为sigmoid函数，且要完成的任务为一个（多输出）回归任务，因此损失函数可以采用均方误差（分类任务则用交叉熵）。

网络模型、损失函数、参数更新如下图所示：

![IMG_20211027_223349](C:\Users\destiny\Documents\Tencent Files\240412375\FileRecv\MobileFile\IMG_20211027_223349.jpg)
