# -*- coding: utf-8 -*-
import os
data = []
# 读取文件
filename = "data.txt"
with open(filename) as f_ob:
    lines = f_ob.readlines()

for line in lines:
    line = line.rstrip() # 删除换行
    result = ' '.join(line.split()) #删除多余空格，保存一个空格连接
    # 获取每行的五个值，将字符串格式转换为浮点数
    s = [float(x) for x in result.strip().split(' ')]
    print s
    data.append(s)  # 将数据存储在data

print("完整数据集")
print data          # 输出完整数据集
print type(data)    # 显示数据集的类型

print("第一列和第五列数据")
L2 = [n[0] for n in data]   # n[0]表示第一列
print L2
L5 = [n[4] for n in data]   # n[4]表示第五列
print L5

# 将两列数据生成二维矩阵
T = dict(zip(L2,L5))
"""zip函数：接受任意多个（包括0个和1个）序列作为参数，返回一个元组列表，
    再把元组列表以字典形式存在T中"""
print("T的类型" + str(type(T)))
print T

# dict类转化为list
X = list(map(lambda x,y: (x,y),T.keys(),T.values()))
print("X的类型" + str(type(X)))
print X

# 导入KMeans聚类相关模块
from sklearn.cluster import Birch
from sklearn.cluster import KMeans

clf = KMeans(n_clusters=3)  # 类簇数设置为3
y_pred = clf.fit_predict(X)
# 输出聚类结果，96行数据，每个y_pred对应X一行或一个球员，聚成3类，类标为0、1、2
print clf

# 可视化绘图
import numpy as np
import matplotlib.pyplot as plt

# 使用for循环获取第一列和第二列数据
x = [n[0] for n in X]
print x
y = [n[1] for n in X]
print y

# 坐标
x1 = []
y1 = []

x2 = []
y2 = []

x3 = []
y3 = []

# 分布获取类标0、1、2的数据，赋值给(x1,y1) (x2,y2) (x3,y3)
i = 0
while i < len(x):
    if y_pred[i] == 0:
        x1.append(X[i][0])
        y1.append(X[i][1])
    elif y_pred[i] == 1:
        x2.append(X[i][0])
        y2.append(X[i][1])
    elif y_pred[i] == 2:
        x3.append(X[i][0])
        y3.append(X[i][1])

    i = i + 1

# 四种颜色 红 绿 蓝 黑
plot1, = plt.plot(x1,y1,"or",marker="x")
plot2, = plt.plot(x2,y2,"og",marker="o")
plot3, = plt.plot(x3,y3,"ob",marker="*")

# 绘制标题
plt.title("Kmeans-Basketball Data")

# 绘制x轴和y轴坐标
plt.xlabel("assists_per_minute")
plt.ylabel("points_per_minute")

# 设置右上角图例
plt.legend((plot1,plot2,plot3),("A","B","C"),fontsize=10)

plt.show()