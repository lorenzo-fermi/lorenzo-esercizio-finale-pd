import numpy as np
#ECCO I COMANDI PRINCIPALI DI NUMPY SPIEGATI CON ESEMPI

# Creazione di array
arr = np.array([1, 2, 3])
print(arr)  # Output: [1 2 3]

# Creazione di array di zeri
arr_zeros = np.zeros((3, 3))
print(arr_zeros)
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

# Creazione di array di uno
arr_ones = np.ones((2, 4))
print(arr_ones)
# Output:
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

# Creazione di array con intervalli di valori
arr_range = np.arange(0, 10, 2)
print(arr_range)  # Output: [0 2 4 6 8]

# Creazione di array con valori equidistanti
arr_linspace = np.linspace(0, 1, 5)
print(arr_linspace)  # Output: [0.   0.25 0.5  0.75 1.  ]

# Modifica della forma dell'array
arr = np.array([1, 2, 3, 4, 5, 6])
arr_reshaped = arr.reshape((2, 3))
print(arr_reshaped)
# Output:
# [[1 2 3]
#  [4 5 6]]

# Somma degli elementi dell'array
arr = np.array([1, 2, 3])
sum_arr = np.sum(arr)
print(sum_arr)  # Output: 6

# Media degli elementi dell'array
mean_arr = np.mean(arr)
print(mean_arr)  # Output: 2.0

# Massimo degli elementi dell'array
max_arr = np.max(arr)
print(max_arr)  # Output: 3

# Concatenazione di array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr_concat = np.concatenate((arr1, arr2))
print(arr_concat)  # Output: [1 2 3 4 5 6]

# Creazione di array casuali (valori tra 0 e 1)
arr_random = np.random.rand(2, 3)
print(arr_random)
# Output (esempio):
# [[0.5488135  0.71518937 0.60276338]
#  [0.54488318 0.4236548  0.64589411]]

# Creazione di array casuali di interi
arr_randint = np.random.randint(0, 10, (2, 3))
print(arr_randint)
# Output (esempio):
# [[6 3 7]
#  [4 6 9]]
















