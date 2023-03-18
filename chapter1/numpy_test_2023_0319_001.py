import numpy as np
A = np.array([[1, 2], [3, 4]])
print(f'A = {A}')
print(f'A.shape = {A.shape}')
print(f'A.dtype = {A.dtype}')

A1 = np.array([[1, 2], [3, 4]], dtype=np.int64)
print(f'A1 = {A1}')
print(f'A1.shape = {A1.shape}')
print(f'A1.dtype = {A1.dtype}')