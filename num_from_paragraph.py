# extract numbers from a paragraph
import sys

print("Enter the paragraph :")
input_paragraph = sys.stdin.readlines()  # reads paragraph
numeric = []  # empty list

temp = 0
for item in input_paragraph:  # iterating the paragraph
    for i in item:   # iterating the line
        if i.isnumeric():   # if a numeric value, adding to temp var
            temp = temp*10 + int(i)
        elif temp!=0:   # else append to list
            numeric.append(temp)
            temp = 0

print("\nNumbers in the paragraph :")
print(numeric)