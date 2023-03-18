import numpy as np
A = np.array([[1, 2], [3, 4]])
print(f'A = {A}')
print(f'A.shape = {A.shape}')
print(f'A.dtype = {A.dtype}')
print()

A1 = np.array([[1, 2], [3, 4]], dtype=np.int64)
print(f'A1 = {A1}')
print(f'A1.shape = {A1.shape}')
print(f'A1.dtype = {A1.dtype}')
print()

B = np.array([[3, 0], [0, 6]])
print(f'B={B}')
print()

print(f'A+B={A+B}')
print(f'A*B={A*B}')
print(f'A*10={A*10}')