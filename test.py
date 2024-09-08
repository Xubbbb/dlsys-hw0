# import numpy as np

# # 创建一个3x4的二维数组
# array_2d = np.array([[1, 2, 3, 4],
#                      [5, 6, 7, 8],
#                      [9, 10, 11, 12]], dtype=np.float32)

# # 对列求和（压缩行）
# sum_over_rows = np.sum(array_2d, axis=0)
# print("Sum over rows (axis=0):", sum_over_rows)

# # 对行求和（压缩列）
# sum_over_cols = np.sum(array_2d, axis=1)
# print("Sum over columns (axis=1):", sum_over_cols)

# # 创建一个3x4x5的三维数组
# array_3d = np.random.randint(1, 10, (3, 4, 5))
# print(array_3d)

# # 对第一个和第三个维度求和
# sum_over_axes = np.sum(array_3d, axis=(0, 2))
# print("Sum over axes 0 and 2:", sum_over_axes)

# print(array_2d - np.max(array_2d, axis=1, keepdims=True))

# def softmax_2d(A):
#     exp_a = np.exp(A - np.max(A, axis=1, keepdims=True))
#     softmax_a = exp_a / np.sum(exp_a, axis=1, keepdims=True)
#     A -= softmax_a
    
#     return softmax_a

# softmax_2d(array_2d)

# print(array_2d)


# import numpy as np

# # 假设 A 和 B 是两个形状相同的二维矩阵
# A = np.array([[1, 2, 3], [4, 5, 6]])
# B = np.array([[7, 8, 9], [10, 11, 12]])

# # 方法一：使用 * 运算符
# C1 = A * B

# # 方法二：使用 np.multiply 函数
# C2 = np.multiply(A, B)

# print("C1:\n", C1)
# print("C2:\n", C2)






