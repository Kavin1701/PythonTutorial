# to count the number of different elements in a list

n = int(input("\nEnter the number of elements : "))  # n = no. of elements
myList = []   # empty list

for i in range(n):  # getting the elements
    myList.append(input("  Enter the element "+str(i+1)+": "))

count = 0
myList2 = []   # empty list
for i in myList:   # iterating myList
    if i not in myList2:   # not already present in myList2
        myList2.append(i)
        count += 1

# printing no. of different elements
print("No. of different elements : "+str(count))