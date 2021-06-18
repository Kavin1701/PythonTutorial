# to find the mean

n=(int(input("\nEnter the number of elements: "))) # n = number of elements
myList = [] #empty list

for i in range(n):  # getting the elements
    myList.append(float(input("  Enter element "+str(i+1)+": ")))

mean = sum(myList)/n  #calculating mean
print("     Mean : {0:.2f}".format(mean))