# date extraction form a paragraph (mm.dd.yyyy)
import sys

print("Enter the paragraph :")
input_paragraph = sys.stdin.readlines();  # reads paragraph
dates = []  # empty list

for item in input_paragraph:  # iterating the paragraph
    i = 0
    while(i < len(item)):   # iterating the lines
        # if pattern mm.dd.yyyy matches
        if item[i:i+2].isnumeric() and item[i+3:i+5].isnumeric() and item[i+6:i+9].isnumeric() and (item[i+2]=="." and item[i+5]=="." or item[i+2]=="-"and item[i+5]=="-" or item[i+2]=="/"and item[i+5]=="/"):
            dates.append(item[i:i+10])
            i += 10
        else: 
            i+=1

print("Dates in the paragraph :")
print(dates)