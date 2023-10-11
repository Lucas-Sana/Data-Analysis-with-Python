import sys
import numpy as np

# Basic Numpy Arrays

np.array([1, 2, 3, 4])
a = np.array([1, 2, 3, 4])
b = np.array([0, .5, 1, 1.5, 2])
a[0], a[1]
a[0:]
a[1:3]
a[1:-1]
a[::2]
b
b[0], b[2], b[-1]
b[[0, 2, -1]]

# Array Types

a
a.dtype
b
b.dtype
np.array([1, 2, 3, 4], dtype=np.float)
np.array([1, 2, 3, 4], dtype=np.int8)
c = np.array(['a', 'b', 'c'])
c.dtype
d = np.array([{'a': 1}, sys])
d.dtype

# Dimensions and shapes

A = np.array([[1, 2, 3], [4, 5, 6]])
A.shape
A.ndim
A.size
B = np.array([[[12, 11, 10], [9, 8, 7],], [[6, 5, 4], [3, 2, 1]]])
B
B.shape
B.ndim
B.size
C = np.array([[[12, 11, 10], [9, 8, 7],], [[6, 5, 4]]])
C.dtype
C.shape
C.size
type(C[0])

# Indexing and Slicing of Matrices

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
A[1]
A[1][0]
A[1, 0]
A[0:2]
A[:, :2]
A[:2, :2]
A[:2, 2:]
A
A[1] = np.array([10, 10, 10])
A
A[2] = 99
A

# Summary statistics

a = np.array([1, 2, 3, 4])
a.sum()
a.mean()
a.std()
a.var()
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
A.sum()
A.mean()
A.std()
A.sum(axis=0)
A.sum(axis=1)
A.mean(axis=0)
A.mean(axis=1)
A.std(axis=0)
A.std(axis=1)

# Broadcasting and Vectorized operations

a = np.arange(4)
a
a + 10
a * 10
a
a += 100
a
l = [0, 1, 2, 3]
[i * 10 for i in l]
a = np.arange(4)
a
b = np.array([10, 10, 10, 10])
b
a + b
a * b

# Boolean arrays (Also called masks)

a = np.arange(4)
a
a[0], a[-1]
a[[0, -1]]
a[[True, False, False, True]]
a
a >= 2
a[a >= 2]
a.mean()
a[a > a.mean()]
a[~(a > a.mean())]
a[(a == 0) | (a == 1)]
a[(a <= 2) & (a % 2 == 0)]
A = np.random.randint(100, size=(3, 3))
A
A[np.array([[True, False, True], [False, True, False], [True, False, True]])]
A > 30
A[A > 30]

# Linear Algebra

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[6, 5], [4, 3], [2, 1]])
A.dot(B)
A @ B
B.T
A
B.T @ A

# Size of objects in Memory

sys.getsizeof(1)
sys.getsizeof(10**100)
np.dtype(int).itemsize
np.dtype(np.int8).itemsize
np.dtype(float).itemsize

# Useful Numpy functions

np.random.random(size=2)
np.random.normal(size=2)
np.random.rand(2, 4)
np.arange(10)
np.arange(5, 10)
np.arange(0, 1, .1)
np.arange(10).reshape(2, 5)
np.arange(10).reshape(5, 2)
np.linspace(0, 1, 5)
np.linspace(0, 1, 20)
np.linspace(0, 1, 20, False)
np.zeros(5)
np.zeros((3, 3))
np.zeros((3, 3), dtype=np.int)
np.ones(5)
np.ones((3, 3))
np.empty(5)
np.empty((2, 2))
np.identity(3)
np.eye(3, 3)
np.eye(8, 4)
np.eye(8, 4, k=1)
np.eye(8, 4, k=-3)
"Hello World"[6]
