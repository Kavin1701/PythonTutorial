# to find the maximum and minimum

n = int(input("\nEnter the number of elements: "))  # n = no. of elements
myList = []

for i in range(n):  # getting the elements
    myList.append(input("  Enter the element "+str(i+1)+": "))

print("\n     Max : "+str(max(myList))+",  Min : "+str(min(myList)))