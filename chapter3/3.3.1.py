import numpy as np
A = np.array([1, 2, 3, 4])
print(f'A = {A}')
print(f'A.ndim = {A.ndim}')
print(f'A.shape = {A.shape}')
print(f'A.shape[0] = {A.shape[0]}')

B=np.array([[1,2],[3,4],[5,6]])
print(f'B = {B}')
print(f'B.ndim = {B.ndim}')
print(f'B.shape = {B.shape}')

#这里生成了一个3 × 2的数组B。
#3 × 2的数组表示第一个维度有3个元素(3行,每行2个数字)，第二个维度有2个元素(2列,每列3个数字)。
#另外，第一个维度对应第0维，第二个维度对应第1维（Python的索引从0开始）

#For dimension 0 (rows), we fix the row index and use a colon : to select all elements in that row.
# Access elements in dimension 0 (rows)
row0 = B[0, :]  # [1, 2]
row1 = B[1, :]  # [3, 4]
row2 = B[2, :]  # [5, 6]
print(f'row0 = {row0}, row1 = {row1}, row2 = {row2}')

#For dimension 1 (columns), we fix the column index and use a colon : to select all elements in that column
# Access elements in dimension 1 (columns)
col0 = B[:, 0]  # [1, 3, 5]
col1 = B[:, 1]  # [2, 4, 6]
print(f'col0 = {col0}, col1 = {col1}')