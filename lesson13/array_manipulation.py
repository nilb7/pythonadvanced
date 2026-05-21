import numpy as np

#array 2D with 2 rows and 5 columns

array_2d = np.array([[1,2,3,4,5,],
                     [6,7,8,9,10]])

print(array_2d)

element = array_2d[1,2]

print(element)

dimension = array_2d.ndim
print(dimension)

array_size = array_2s.size

print(array_size)

sub_array = array_2d[:2,:2]
print(sub_array)

#negative slicing

sub_array2 = array_2d[-4:-4:]

print(sub_array2)

total_sum = np.sum(array_2d)
print(total_sum)

#sum along axis 0
sum_colons = np.dum(array_2d,axis=0)

print(sum_colons)

reshape_array = array_2d.reshape(
    (5,2)
)
print(reshape_array)