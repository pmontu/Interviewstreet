# circular buffer
#
# Author: Manojkumar Purushothaman
#
# Date created: Aug 27 2012
# Date updated: Aug 27 2012
#===================================

# Implement a circular buffer of size N. Allow the caller to append, remove and list the contents of the buffer. Implement the buffer to achieve maximum performance for each of the operations.
# 
# The new items are appended to the end and the order is retained i.e elements are placed in increasing order of their insertion time. When the number of elements in the list elements exceeds the defined size, the older elements are overwritten.
#  
#  
# There are four types of commands.
#  
# "A"  n -  Append the following n lines to the buffer. If the buffer is full they replace the older entries.
# "R"  n -  Remove first n elements of the buffer. These n elements are the ones that were added earliest among the current elements.
# "L"   - List the elements of buffer in order of their inserting time.
# "Q"  - Quit.  
#  
# Your task is to execute commands on circular buffer.
#  
# Input format :
#  
# First line of input contains N ,  the size of the buffer.
# A n  - append the following n lines to the buffer.
# R n - remove first n elements of the buffer.
# L - list the buffer.
# Q - Quit.
#  
# Output format :
#  
# Whenever  L command appears in the input, print the elements of buffer in order of their inserting time. Element that was added first should appear first. 
#  
# Sample Input :
#  
# 10
# A 3
# Fee
# Fi
# Fo
# A 1
# Fum
# R 2
# L
# Q
#  
# Sample Output :
#  
# Fo
# Fum
#  
# Constraint :
#  
# 0 <= N <= 10000
# Number of removing elements will <= number of elements presents in circular buffer.
# total number of commands <= 50000.
# total number of characters in input <= 20000000.

class CBNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class CBuffer:
    def __init__(self, size):
        self.remove = self.add = None
        self.elements = 0
        self.size = size
    def insert(self, key):
        if self.add:
            self.add.next = CBNode(key)
            self.add = self.add.next
            self.elements += 1
        else:
            self.add = CBNode(key)
            self.remove = self.add
            self.elements = 1
        if self.elements>self.size:
            self.delete()
    def printbuffer(self):
        node = self.remove
        while node:
            print(node.key)
            node = node.next
    def delete(self):
        if self.remove == self.add:
            self.remove = self.add = None
            self.elements = 0
        else:
            self.remove = self.remove.next
            self.elements -= 1

N = int(raw_input())
cbuf = CBuffer(N)
while True:
    command = raw_input().strip()
    if command=="Q":
        exit()
    elif command=="L":
        cbuf.printbuffer()
    else:
        command = command.split()
        num = int(command[1])
        command = command[0]
        if command == "A":
            for i in range(num):
                item = raw_input().strip()
                cbuf.insert(item)
        else:
            for i in range(num):
                cbuf.delete()