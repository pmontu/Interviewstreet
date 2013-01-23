# Frequency Words
#
# Author: Manojkumar Purushothaman
#
# Date created: Aug 24 2012
# Date updated: Aug 24 2012
#===================================

# Given an unordered list of N elements, write a function to find the top four elements of the given list. Make sure your function runs in linear time O(N).
#  
# Input format :
#  
# First line of input contains N , number of elements in list.
# Next N line , each contains a element.
#  
# Output format :
#  
# Print the top four elements of list.
#  
# Sample input :
#  
# 8
# 6930886
# -1692777
# 4636915
# 7747793
# -4238335
# 9885386
# 9760492
# 6516649
#  
# Sample ouput :
#  
# 9885386
# 9760492
# 7747793
# 6930886
#  
# Constraint :
#  
# N < 1000000.
# all numbers will fit  in 32-bit integer.

N = int(raw_input())
items = []
for i in range(N):
    items.append(int(raw_input()))
lenitems = len(items)

#first
minq = []
minq.insert(0,items[0])

if items[1]>minq[0]:
    minq.insert(0,items[1])
else:
    minq.append(items[1])

if items[2]>minq[0]:
    minq.insert(0,items[2])
elif items[2]<minq[1]:
    minq.append(items[2])
else:
    minq.insert(1,items[2])

if items[3]>minq[0]:
    minq.insert(0,items[3])
elif items[3]<=minq[2]:
    minq.append(items[3])
elif items[3]<=minq[0] and items[3]>minq[1]:
    minq.insert(1,items[3])
else:
    minq.insert(2,items[3])

for i in range(4,N):
    num = items[i]
    if num>minq[0]:
        minq.insert(0,num)
        minq.pop()
    elif num<=minq[0] and num>minq[1]:
        minq.insert(1,num)
        minq.pop()
    elif num<=minq[1] and num>minq[2]:
        minq.insert(2,num)
        minq.pop()
    elif num<=minq[2] and num>minq[3]:
        minq.insert(3,num)
        minq.pop()

print(minq[0])
print(minq[1])
print(minq[2])
print(minq[3])
