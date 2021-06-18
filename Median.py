# to find median
def my_median(myList):
    mid = len(myList)//2  # finding the midpoint
    if len(myList) % 2:  # if list contains odd elements
        return sorted(myList)[mid]
    else:    # if list contains even elements
        return sum(sorted(myList)[mid-1 : mid+1])/2


n = int(input("Enter the number of elements: ")) # n = no. of elements
myList = [] #empty list

for i in range(n):  # getting the elements
    myList.append(float(input("  Enter the element "+str(i+1)+": ")))

print("    Median : {0:.2f}".format(my_median(myList)))