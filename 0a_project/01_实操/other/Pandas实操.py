import pandas as pd
import numpy as np

# ----------------------------------------------------------
# 创建DataFrame
# ----------------------------------------------------------
# 生成作为行索引的时间序列
data_s = pd.date_range('20190601', periods=7)
print(data_s)
print("__" * 26)
# 使用随机的numpy数组作为数据，传入列索引A B C D。
# 生成一个DataFrame数据，data是数据，index是索引，column是列名。
df = pd.DataFrame(np.random.randn(7, 4),
                  index=data_s,
                  columns=list('ABCD'))
print(df)
print("__" * 10)


# ----------------------------------------------------------
# 查看DataFrame中的数据
# ----------------------------------------------------------
# 生成一个维度（6，5）的数组
data2 = np.arange(30).reshape(6, 5)
# 创建DataFrame
df2 = pd.DataFrame(data2,
                   index=['a', 'b', 'c', 'd', 'e', 'f'],
                   columns=['A', 'B', 'C', 'D', 'E'])
print(df2)
print("__" * 10)

# Dataframe.head(n = 5)显示前n条数据。n表示显示的数据量
print(df2.head())
print("__" * 10)

# Dataframe.tail(n = 3)显示底部n条数据。和head的参数一样。
print(df2.tail(3))
print("__" * 10)
print("__" * 10)
print('\nindex is:')
print(df2.index)  # 输出行索引
print('\ncolumns is:')
print(df2.columns)  # 输出列索引
print('\nvalues is:')
print(df2.values)  # 输出数据
print("__" * 10)

# DataFrame.loc:按标签或布尔数组访问一组行和列
# 获取A列，索引为a到f（包括f）中的数据，步长为2
print(df2.loc['a':'f':2, 'A'])
print("__" * 10)

print(df2.describe())  # describe描述了数据的详细信息


# ----------------------------------------------------------
# DataFrame数据的操作
# ----------------------------------------------------------
data3 = np.arange(30).reshape(6, 5)
df3 = pd.DataFrame(data3,
                   index=['a', 'b', 'c', 'd', 'e', 'f'],
                   columns=['A', 'B', 'C', 'D', 'E'])
a = df3.drop(['a'], axis=0)  # axis=0时删除指定的行
b = df3.drop(['A'], axis=1)  # axis=1时删除指定的列
print('--------原始数据--------')
print(df3)
print('---------删除行---------')
print(a)
print('---------删除列---------')
print(b)
print("__" * 10)

# 使用append方法合并两个DataFrame
# 将其他行附加到调用者的末尾,返回一个新对象。others为要追加的数据
c = b.append(a)
print('----合并后产生的新数据----')
print(c)

# 使用reset_index方法还原索引，让索引变为数据中的一列
b.reset_index(inplace=True)
# inplace为true时会修改原始数据，为false会产生新的数据
print("__" * 10)


# ----------------------------------------------------------
# Pandas中缺失数据的操作
# ----------------------------------------------------------
df6 = pd.DataFrame(np.random.randn(5, 3),
                   index=['a', 'c', 'e', 'f', 'h'],
                   columns=['one', 'two', 'three'])
# 使用reindex方法设置新的索引，多出的索引对应的数据使用NaN填充
df6 = df6.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df6)
print("__" * 10)

# 检查是否存在缺失
df7 = pd.DataFrame(np.random.randn(5, 3),
                   index=['a', 'c', 'e', 'f', 'h'],
                   columns=['one', 'two', 'three'])
df7 = df7.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df7['one'].isnull())  # isnull方法可以检查数据中是否有空值
print("__" * 10)

# 缺失数据的计算
df8 = pd.DataFrame(np.random.randn(5, 3),
                   index=['a', 'c', 'e', 'f', 'h'],
                   columns=['one', 'two', 'three'])
df8 = df8.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df8)
print()
print(df8['one'].sum())
print("__" * 10)

# 用标量替换NaN
df9 = pd.DataFrame(np.random.randn(3, 3),
                   index=['a', 'c', 'e'],
                   columns=['one', 'two', 'three'])
df9 = df9.reindex(['a', 'b', 'c'])
print(df9)
print("Nan replace with '0':")
print(df9.fillna(0))  # fillna方法可以使用指定数据来填充NaN
