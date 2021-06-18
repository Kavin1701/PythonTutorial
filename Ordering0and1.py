# an array contain mixture of 0s and 1s.
# to arrange 0s on one side and 1s on the other.

import array as arr
n = int(input("Enter the number of elements : "))   # n = no. of elements
myArr = arr.array('i',[])   # empty array

for i in range(n):   # getting the elements
    myArr.append(int(input("  Enter the element "+str(i+1)+": ")))

print("Array before ordering : "+str(myArr))

countZero = 0   # counter for no. of 0's in array
for i in range(n):   # counting number of zeros
    if myArr[i] == 0:
        countZero += 1

for i in range(n):
    if i < countZero:   # assigning 0 on one side
        myArr[i] = 0
    else:    # assigning 1 on other side
        myArr[i] = 1

print("Array after ordering : "+str(myArr))