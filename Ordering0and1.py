# ordering of 0's and 1's (Optimised)
import array as arr

str = input("\nEnter the sequence (containing 0's and 1's) : ")   # getting input as string
myArray = arr.array("i", [int(s) for s in list(str)])   # converting string to array
print("  Array before ordering : {}".format(myArray))

i, j = 0, len(str)-1   # to point the first and last element of array
while True:
    if myArray[i] != 1:  # if i not pointing to 1
        i += 1

    if myArray[j] != 0:  # if j not pointing to 0
        j -= 1

    if i>j:  # if i points ahead of j
        break
    elif myArray[i] == 1 and myArray[j] == 0:    # if i pointing to 1 and j pointing to 0
        myArray[i] = 0
        myArray[j] = 1
        i += 1
        j -= 1
print("  Array after ordering : {}\n".format(myArray))