import numpy as np
import pandas as pd

a = np.array([1, 2, 3, 4])
X = a.copy()
Y = a.view()
print(a.base)
print(X.base)  # neu nhu no giu data thi return None
print(Y.base)

arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],
                [[9, 10, 11, 12], [13, 14, 15, 16]],
                [[17, 18, 19, 20], [21, 22, 23, 24]]])
# for idx, i in np.ndenumerate(arr):
#   print(idx, i)

arr1 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],
                 [[9, 10, 11, 12], [13, 14, 15, 16]],
                 [[17, 18, 19, 20], [21, 22, 23, 24]]])
print(arr1[:, ::2, ::2])
print("join")
arr2 = np.array([[1, 2], [3,4]])
arr3 = np.array([[5, 6], [7,8]])
print("concat")
print("0: {}".format(np.concatenate((arr2, arr3), axis=0)))
print("1: {}".format(np.concatenate((arr2, arr3), axis=1)))
print("stack")
print("0: {}".format(np.stack((arr2, arr3), axis=0)))
print("1: {}".format(np.stack((arr2, arr3), axis=1)))
print("hstack: {}".format(np.hstack((arr2, arr3))))
print("vstack: {}".format(np.vstack((arr2, arr3))))
print("dstack: {}".format(np.dstack((arr2, arr3))))