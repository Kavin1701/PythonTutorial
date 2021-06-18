# to find variance and standard deviation
import math
def find_mean(myList,n):  # to find the mean
    return sum(myList)/n


def find_variance(myList,n):
    mean = find_mean(myList,n)
    deviations = [(x - mean) ** 2 for x in myList]
    variance = find_mean(deviations, n)
    return variance

# driver program
n=int(input("\nEnter the number of elements: "))  # n = no. of elements
myList = []

for i in range(n):  # getting the elements
    myList.append(int(input("  Enter the element "+str(i+1)+": ")))

variance = find_variance(myList,n)
std_deviation = math.sqrt(variance)

print("\n   Variance : {0:.2f}".format(variance))
print("   Standard Deviation : {0:.2f}\n".format(std_deviation))