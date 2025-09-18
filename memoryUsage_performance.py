import numpy as np, sys, time


# comparing the performance
elements = 150
my_list1 = range(elements)
my_list2 = range(elements)

my_array1 = np.arange(elements) 
my_array2 = np.arange(elements) 
list_start = time.time()
list_result = [(n1 + n2) for n1,n2 in zip(my_list1,my_list2)]
print(f"List Time: {time.time() - list_start}")

array_start = time.time()
array_result = my_array1 + my_array2
print(f"List Time: {time.time() - array_start}")

print("#" * 50)

# comparing memory usage
my_array = np.arange(100)
print(my_array)
print(my_array.itemsize)
print(my_array.size)
print(f"All Bytes: {my_array.itemsize* my_array.size}")

my_list = range(100)
print(sys.getsizeof(1))
print(len(my_list))
print(f"All Bytes: {sys.getsizeof(1)* len(my_list)}")

print("#" * 50)
d = np.array([['A','B','X'],['C','D','Y'],['M','N','O']])
print(d[50:100]) # output=> []
# NumPy allows you to slice arrays beyond their actual size without raising an IndexError.
print(d[1: ,0])

a = np.array([[1,2,3,4,5], [1,2,3,4,5]])
b = np.array([1,2,3,4,5])
print(a == b)
print(np.array_equal(a,b))

