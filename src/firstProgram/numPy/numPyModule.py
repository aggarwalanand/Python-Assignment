import numpy as np

# The last value is excluded
# Prints the range for the specified values
print(np.arange(-50, -10))
print("\n")
print(np.arange(10, 50))
print("\n")
print(np.arange(10, 50, 0.5))
print("\n")
print(np.arange(24))
print("\n")

# Array of Zeros
print("ZEROS")
print(np.zeros(10))
print("\n")

# Matrix of Zeros
print(np.zeros((3, 3)))
print("\n")

# Array of Ones
print("ONES")
print(np.ones(10))
print("\n")

# Matrix of Ones
print(np.ones((3, 3)))
print("\n")

# Equally, spaced values between start and ending value
print("LINSPACE")
print(np.linspace(1, 10, 6))
print("\n")

# Random number between values specified
print("RANDINT")
print(np.random.randint(1, 50))
print("\n")

print(np.random.randint(1, 50, 50))
print("\n")

# An array of 10 values between 0 and 1 such that the values are less than 1 and their mean in 1
print("RANDOM")
print(np.random.random(10))
print("\n")

# Any values between 10 and -10
print("RANDN")
print(np.random.randn(10))
print("\n")

# Same as above rows and cols are specified
print("RAND")
print(np.random.rand(8, 5))
print("\n")

ranarr = np.random.randint(0, 50, 10)
arr = np.arange(24)
print(arr.reshape(6, 4))

# Identity Matrix
print(np.eye(3, 3))
print("\n")

print(ranarr.max())
print(ranarr.min())
print("\n")
print(ranarr.argmax())
print(ranarr.argmin())
print("\n")
print(arr.shape)
print(arr.reshape(1, 24))
print("\n")
print(arr.dtype)
print("\n")
print("SELCTION")

arr = np.arange(1, 11)
print(arr)
print(arr > 4)
boolArr = arr > 4
print(boolArr)
print(arr[arr > 2])
x = 4
print(arr[arr > x])
x = 11
print(arr[arr > x])  # Retuns an empty array

print("\nARITHMETIC OPERATIONS")
arr = np.arange(1, 11)
print("ADD")
print(arr + arr)
print("SUBTRACT")
print(arr - arr)
print("DIVISION")
print(arr / arr)
print("CUBE")
print(arr ** 3)
print("SQRT")
print(np.sqrt(arr))
print("EXPONENTIAL")
print(np.exp(arr))
print("MEAN")
print(np.mean(arr))
print("MEDIAN")
print(np.median(arr))
print("VARIANCE")
print(np.var(arr))
