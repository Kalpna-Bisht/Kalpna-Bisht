import numpy as np

# Question 1: Array Creation  
# 1.1 
array_1d = np.arange(5, 26)
print("1D Array:", array_1d)
#1.2:
array_2d = np.random.randint(10, 51, size=(3, 4))
print("2D Array:\n", array_2d)


# Question 2: Array Attributes  
# 2.1 
array_1d = np.arange(5, 26)
print("Shape:", array_1d.shape)
print("Size:", array_1d.size)
print("Data type:", array_1d.dtype)
#2.2 
array_2d = np.random.randint(10, 51, size=(3, 4))
print("Shape:", array_2d.shape)
print("Size:", array_2d.size)
print("Data type:", array_2d.dtype)

# Question 3: Array Operations  
# 3.1 
Array1 = np.array([2, 4, 6, 8, 10])
Array2 = np.array([1, 3, 5, 7, 9])
print("Array1:", Array1)
print("Array2:", Array2)
# 3.2
# Addition
addition = Array1 + Array2
print("Addition:", addition)
# Subtraction
subtraction = Array1 - Array2
print("Subtraction:", subtraction)
# Element-wise multiplication
multiplication = Array1 * Array2
print("Multiplication:", multiplication)
# Element-wise division
division = Array1 / Array2
print("Division:", division)

# Question 4: Broadcasting  
# 4.1 
array_2d = np.arange(1, 10).reshape(3, 3)
print("Original 2D Array:\n", array_2d)
# 4.2
broadcasted_array = array_2d * 5
print("Broadcasted Array (Multiplied by 5):\n", broadcasted_array)


# Question 5: Slicing and Indexing  
# 5.1
array_2d = np.arange(10, 26).reshape(4, 4)
print("Original Array:\n", array_2d)
# 5.2
second_row = array_2d[1]
last_column = array_2d[:, -1]
print("Second Row:", second_row)
print("Last Column:", last_column)
# 5.3
array_2d[0] = 0
print("Modified Array:\n", array_2d)

# Question 6: Boolean Indexing  
# 6.1
array_1d = np.random.randint(20, 41, size=10)
print("Original Array:", array_1d)
# 6.2
greater_than_30 = array_1d[array_1d > 30]
print("Elements greater than 30:", greater_than_30)


# Question 7: Reshaping  
# 7.1 
array_1d = np.arange(11, 23)  # 12 elements: from 11 to 22
print("1D Array:", array_1d)
# 7.2
reshaped_array = array_1d.reshape(3, 4)
print("Reshaped 2D Array:\n", reshaped_array)


# Question 8: Matrix Operations  
# 8.1
Matrix_A = np.array([[1, 2], [3, 4]])
Matrix_B = np.array([[5, 6], [7, 8]])
print("Matrix A:\n", Matrix_A)
print("Matrix B:\n", Matrix_B)
# 8.2
# Matrix Multiplication
matrix_product = np.dot(Matrix_A, Matrix_B)
print("Matrix Multiplication (A × B):\n", matrix_product)
# Transpose of Matrix A
transpose_A = Matrix_A.T
print("Transpose of Matrix A:\n", transpose_A)


# Question 9: Statistical Functions  
# 9.1 
array_1d = np.random.randint(10, 61, size=15)
print("1D Array:", array_1d)
# 9.2
# Mean
mean_value = np.mean(array_1d)
print("Mean:", mean_value)
# Median
median_value = np.median(array_1d)
print("Median:", median_value)
# Standard Deviation
std_dev = np.std(array_1d)
print("Standard Deviation:", std_dev)


# Question 10: Linear Algebra  
# 10.1
A = np.array([[2, 1, 3],
              [0, 5, 6],
              [7, 8, 9]])

print("Matrix A:\n", A)
# 10.2
det_A = np.linalg.det(A)
print("Determinant of A:", det_A)
inverse_A = np.linalg.inv(A)
print("Inverse of A:\n", inverse_A)
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A:", eigenvalues)
print("Eigenvectors of A:\n", eigenvectors)


# Question 11
positions = np.array([[0, 0], [2, 3], [4, 7], [7, 10], [10, 15]])
# 11.1
distance = np.linalg.norm(positions[-1] - positions[0])
print("Euclidean Distance (start to end):", distance)
# 11.2
step_distances = np.linalg.norm(np.diff(positions, axis=0), axis=1)
total_distance = np.sum(step_distances)
print("Step-by-step distances:", step_distances)
print("Total Distance Traveled:", total_distance)

