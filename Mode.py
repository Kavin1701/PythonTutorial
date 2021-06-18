# to find the Mode

n=int(input("\nEnter the number of elements: "))  # n = no. of elements
myList = []   # empty list

for i in range(n):  # getting the elements
    myList.append(float(input("  Enter the element "+str(i+1)+": ")))

myDict = {}  # empty dictionary

for i in myList:  # iterating the list
    if myDict.get(i) == None:    # not present already in dictionary
        myDict[i] = 1;
    else:    # present already in dictionary
        myDict[i] = myDict[i] + 1;

mode = []  # empty list
values = myDict.values();  # getting all the values from the dictionary
max_value = max(values)   # finding the max value

for key,value in myDict.items():  # iterating the dictionary
    if value == max_value:   # fetching the key's that are mode
        mode.append(key)

print("     Mode : "+str(mode))