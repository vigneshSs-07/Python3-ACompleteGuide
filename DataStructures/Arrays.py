import numpy as np

arr = [1,2,3,4,5]

arr = np.array(arr)

print(type(arr))


# returning the index of the value passed by user
arr = [51,43,55,78,99]
val = int(input("Enter the val: "))
k =0
for i in (arr):
    if i == val :
        print(k)
        break
    k +=1
#Same using inbuilt function 
import numpy as np
arr = [51,43,55,78,99]
arr = np.array(arr)
result = np.where(arr==51)
print(result)


#1) Create an array with 5 values & delete the value at index no. 2 without using in-built function. 
import numpy as np
arr = [1,2,3,4,5]
arr = np.array(arr)
index = 2
print(np.delete(arr, index))

#2) write a code to reverse an array without using in-built function.
import numpy as np
arr = [1,2,3,4,5]
arr = np.array(arr)
print(arr[::-1])

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
arr_2d = np.array([[1,2,3], [4,5,6]])
arr_1d = np.array([1,2,3])
print(arr_2d)
print(arr_3d)
print(arr_1d)
#Checking the dimension
print(arr_1d.ndim)
print(arr_3d.ndim)
print(arr_2d.ndim)


