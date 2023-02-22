"""
该文件只用于查询常用的方法，语法不对，不能直接运行。
"""


from pandas import Series
import numpy as np
import pandas as pd
import pandas.io.sql as sql

print("========================================================")
print("======================== df ===========================")
print("========================================================")


print("====================== df初始化 =========================")
# 二维列表初始化
df = pd.DataFrame([
    ['a1', 1],
    ['a2', 4]
],
    columns=['uid', 'score'])

# dict按"行"构造dataframe
df = pd.DataFrame({'col1': np.arange(3), 'col2': np.arange(5, 8)})
df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': ['a', 'b', 'c', 'd']})
'''
   col1 col2
0     1    a
1     2    b
2     3    c
3     4    d
'''
# dict按"列"构造dataframe
data = {}
data['a'] = [1, 2, 3]
data['b'] = [4, 5, 6]
print(pd.DataFrame(list(data.values())))
'''
   0  1  2
0  1  2  3
1  4  5  6
'''

# 通过文件初始化
df = pd.read_excel(excel_path, header=1)  # header表示从第几行开始读。索引从0开始
df = pd.read_csv()

# 通过sql初始化
sql.read_frame('select * from test', conn)


print("====================== df索引 =========================")
df = pd.DataFrame([
    ['a1', 1],
    ['a2', 4]
],
    columns=['uid', 'score'])
df[1]  # 取列名为1的列。df里没有，所以会报错
df.loc[1]  # 取index值为1的行。df的index默认从0开始，[0, 1, 2, ...]
df.iloc[1]  # 取第2行，这里1是下标，不是索引名也不是列名。
df.iloc[:, 2]  # 取第3列

###
# loc是索引index和column 
# 而iloc是索引位置赋值，第几行第几列
###

print("====================== df输出 =========================")
df.to_excel()
df.to_csv()


print("====================== df取值 =========================")
# df取出某些列
df = df[["col1", "col2", "col3"]]  # 取出col1, col2, col3列
# df取出某一列转成list或set
myList, mySet = list(df["col"]), set(df["col"])
# df取出满足条件的行
name_index = df["name"] == "wuxiang"  # 取出name列值为wuxiang的行
age_index = df["age"] > 18  # 取出age列值 > 18的行
# 取出满足以上两个条件的行的col1 col2 col3列
df.loc[name_index & age_index, ["col1", "col2", "col3"]]
# df条件索引
df[df["col1"] > 2]
df[df["name"].isin(mySet)]
df[df["name"].str[0] != "H"]  # 取出name列首字母不是H的行


print("====================== df添加行、列 =========================")
# 添加一行数据1 2 3, 列名为col1 col2 col3
df = df.append(pd.DataFrame([["1", "2", "3"]],
               columns=["col1", "col2", "col3"]))
# df添加列
df["new_col"] = list(range(10))  # 用列表为一列添加数据


print("====================== df删除行、列 =========================")
# df删除行
df = df.drop(index=i)  # 删除行索引为i的行
# df删除列
del df["col"]
del df[df.keys()[0]]  # 删除第一列
del df[df.keys()[1]]  # 删除第二列
df.drop('column_name', axis=1, inplace=True)  # 删除'column_name'列
df.drop(columns=drop_cols, inplace=True)  # 删除多列
df.dropna(axis=0, how='all')  # 删除全部为NaN的行
df.dropna(axis=0, how='any')  # 删除含有NaN的行
df.dropna(axis=1, how='all')  # 删除全部为NaN的列
df.dropna(axis=1, how='any')  # 删除含有NaN的列

# df删除某列满足某条件的行
df = df[df["col1"] > 2]  # 取出满足col1 > 2的行


print("====================== df修改 =========================")
# df修改某个单元格的数据
df.loc[index, "col"] = new_val  # 将索引为index行的col列修改为new_val
# df修改某一列
df.loc[:, "col"] = list(new_val_arr)
# df同时给多列赋值
df.loc[index, ["col1", "col2", "col3"]] = new_val_matrix

print("====================== df常用操作 =========================")
# df遍历
for i, row in df.iterrows():
    print(i, row)  # i是索引index，row是一行数据，可以用列名索引这一行的列
# df合并
df = df.append(df2)  # 2022/8/10 马上要废弃了
df = pd.concat([df, df2], ignore_index=True)
# df条件索引
df[df["col1"] > 2]
df[df["name"].isin(mySet)]
df[df["name"].str[0] != "H"]  # 取出name列首字母不是H的行
# df将某一列看成字符串处理
df["col"] = df["col"].str.split()  # .str之后，就可以按string操作了
df["col"] = df["col"].str.count("是")  # 统计每一行的col列中，有多少个是
# df分组groupby统计数量
df = df.groupby(["col"]).count()  # 按col分组统计数量
# df分组查看每组信息
df_grouped = df.groupby(["col1", "col2", "col3"])
for name, group in df_grouped:
    print(name)
    print(group)


print("====================== df index =========================")
df = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 2, 3],
])
df.index  # 取索引series
df = df.rename(index={0: "a", 1: "b", 2: "c", 3: "d"})  # 修改索引
# 将index重置为默认值，即[0, 1, 2, ...], drop=True表示将旧列名删掉
df = df.reset_index(drop=True)  # 或者 df.reset_index(drop=True, inplace=True)
df = df.sort_index()  # 按列名排序（默认升序）

print("====================== df columns =========================")
df.columns  # 取列名series
# 读取时修改列名
df = pd.read_excel('data', names=['new1', 'new2'...'newn'], header=0)

print("====================== df 排序 =========================")
df.sort_index(inplace=True)  # 按列名排序（默认升序）
df.sort_values(by='学号', inplace=True)  # 对某列排序

print("====================== df 按行（列）移动 =========================")
df = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 2, 3],
])
df.shift(1, axis=0)  # 将dataframe按行整体下移1行，+1表示下移
'''
	1	2
0	NaN	NaN	NaN
1	1.0	2.0	3.0
2	4.0	5.0	6.0
3	7.0	8.0	9.0
'''
df.shift(-1, axis=0)  # 将dataframe按行整体上移1行，-1表示上移
'''
结果：
	1	2
0	4.0	5.0	6.0
1	7.0	8.0	9.0
2	1.0	2.0	3.0
3	NaN	NaN	NaN
'''

print("====================== df 窗口操作 =========================")
df = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 2, 3],
])
# 将dataframe按行进行窗口操作。rolling会遍历每一行，每次取当前行和它前面的若干行，满足个数 = 窗口大小，最终组成一个Rolling。然后对Rolling可以执行min/max/mean/aggregate等操作
# 比如window=2，取mean操作，则从第二行开始，每一行的结果 = 当前行 与 前一行的平均值。由于第一行没有前一行，所以结果为NaN
df.rolling(window=2, axis=0).mean()
'''
结果：
	1	2
0	NaN	NaN	NaN
1	2.5	3.5	4.5
2	5.5	6.5	7.5
3	4.0	5.0	6.0
'''
df.rolling(window=2, axis=0).apply(lambda x: fn(x))  # 对窗口中元素做指定操作，x表示窗口中的所有元素

print("============================ df fillna 缺失值填充 =================================")
df = pd.DataFrame([
    [1, 2, np.nan],
    [2, np.nan, 5],
    [np.nan, 3, np.nan]
])


def fill_missing(df: pd.DataFrame):
    """缺失值填充"""
    ret_df = df.copy()  # 深拷贝，避免原始dataframe被修改
    for col in df.columns:
        ret_df[col] = df[col].fillna(df[col].mean())   # 均值填充
        # df = df[col].fillna(df[col].median())  # 中位数填充
        # df = df[col].fillna(df[col].mode()[0])  # 众数填充（可能会有多个，取第一个）'Age'].fillna(df['Age'].median(), inplace=True)  # 中位数
    return ret_df


print("============================ df replace 值替换 =================================")
df.replace(to_replace=-1,
           value=np.nan, inplace=True)  # to_replace是代替换值，value是替换值

print("============================ df diff 差分 =================================")
df = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 7, 7]
])
ans = df.diff(axis=0).sum(axis=0)
print(ans)
print(ans.values)

print("====================== df 时间列解析 =========================")
# 将DataFrame的某一列解析成时间
df = pd.DataFrame([
    ['2022/1/1 0:00', 0.1, 0.2, 0.3],
    ['2022/1/2 2:00', 0.1, 0.2, 0.3],
    ['2022/1/3 4:00', 0.1, 0.2, 0.3],
], columns=['STime', 't0_max', 't0_min', 't0_mean'])
df['STime'] = pd.to_datetime(df['STime'])
print(df)
'''
结果
                STime  t0_max  t0_min  t0_mean
0 2022-01-01 00:00:00     0.1     0.2      0.3
1 2022-01-02 02:00:00     0.1     0.2      0.3
2 2022-01-03 04:00:00     0.1     0.2      0.3
'''
# 在读取文件时，直接解析成时间
df = pd.read_csv(path, parse_dates=['STime'],
                 infer_datetime_format=True)  # STime是要解析的时间列

print("============================ df 合并 =================================")
df1 = pd.DataFrame({'STime': [1, 2], 'b': [5, 6]})
df2 = pd.DataFrame({'STime': [1, 2], 'y': [6, 7]})
df = pd.merge(df1, df2, on='STime', how='inner')  # 合并df1、df2，按STime合并

print("---------------------------------------------------------------------------------------------------------------------------")
print("====================== series运算 =========================")
# 创建Series
s = Series([195, 73], index=[">825.625", "<=825.625"])
# Series数学运算
s + 100
s - 100
s * 100
s / 100

np.sqrt(s)  # numpy实现开方运算
s[0] * 2
s[[0, 1, 2]] * 2  # 对指定的某些单元格运算

print("====================== series mask 将满足条件的单元格替换为指定值 =========================")
s = pd.Series([1, 2, 3, 100, 200, 10000, 50000])
print(s.mask(s > 1, other='123123'))  # > 1的值替换为123123
