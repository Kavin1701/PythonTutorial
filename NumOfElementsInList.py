# to count the number of different elements in a list

n = int(input("\nEnter the number of elements : "))  # n = no. of elements
myList = []   # empty list

for i in range(n):  # getting the elements
    myList.append(input("  Enter the element "+str(i+1)+": "))

myDict = {}   # empty dictionary
for i in myList:   # iterating myList
    if myDict.get(i) == None:   # not already present in dictionary
        myDict[i] = 1
    else:   # already present in dictionary
        myDict[i] += 1

# printing the no. of occurence
for key,value in myDict.items():
    print("      "+str(key)+" - "+str(value))