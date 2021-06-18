# to find the interquartile range and Outlier

def get_interquartile_range(myList, n):
    mid = n//2
    if n%2:  # if odd num of elements
        list1 = myList[ : mid]
        list2 = myList[mid+1 : ]
    else:  # if even num of elements
        list1 = myList[ : mid]
        list2 = myList[mid : ]

    mid1 = len(list1)//2
    if len(list1) % 2:
        q1 = list1[mid1]
    else:
        q1 = (float(list1[mid1]) + float(list1[mid1-1]))/2

    mid2 = len(list2)//2
    if len(list2) % 2:
        q2 = list2[mid2]
    else:
        q2 = (float(list2[mid2]) + float(list2[mid2-1]))/2

    return q1,q2,q2-q1;

n = int(input("\nEnter the number of elements:"))  # n = no. of elements
myList = []  # empty list

for i in range(n):  # getting the elements
    myList.append(float(input("  Enter the element "+str(i+1)+": ")))


q1,q3,iq_range = get_interquartile_range(sorted(myList), n)
print("\nInterquartile Range : {0:.2f}".format(iq_range))

outlier = []  # empty list
for i in myList:  # to find outlier
    if i > q3 + 1.5*iq_range:
        outlier.append(i)
    elif i < q1 - 1.5*iq_range:
        outlier.append(i)

print("Outlier : "+str(outlier))
