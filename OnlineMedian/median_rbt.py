# This code is adapted from a RBT module
# downloaded from http://newcenturycomputers.net/projects/rbtree.html
#
# Author: Manojkumar Purushothaman
#
# Date Created: July 23 2012
# Date Modified: July 25 2012

# The median of M numbers is defined as the middle number after sorting them in order, if M is odd or the average number of the middle 2 numbers (again after sorting) if M is even. You have an empty number list at first. Then you can add or remove some number from the list. For each add or remove operation, output the median of numbers in the list.
#
# Example : For a set of m = 5 numbers, { 9, 2, 8, 4, 1 } the median is the third number in sorted set { 1, 2, 4, 8, 9 } which is 4. Similarly for set of m = 4, { 5, 2, 10, 4 }, the median is the average of second and the third element in the sorted set { 2, 4, 5, 10 } which is (4+5)/2 = 4.5
#
# Input:
#
# The first line is an integer n indicates the number of operations. Each of the next n lines is either "a x" or "r x" which indicates the operation is add or remove.
#
# Output:
#
# For each operation: If the operation is add output the median after adding x in a single line. If the operation is remove and the number x is not in the list, output "Wrong!" in a single line. If the operation is remove and the number x is in the list, output the median after deleting x in a single line. (if the result is an integer DO NOT output decimal point. And if the result is a double number , DO NOT output trailing 0s.)
#
# Constraints:
#
# 0 < n <= 100,000
#
# for each "a x" or "r x" , x will fit in 32-bit integer.
#
# Sample Input:
#
# 7
# r 1
# a 1
# a 2
# a 1
# r 1
# r 2
# r 1
#
# Sample Output:
# Wrong!
# 1
# 1.5
# 1
# 1.5
# 1
# Wrong!
#
# Note: As evident from the last line of the input, if after remove operation the list becomes empty you have to print "Wrong!" ( quotes are for clarity ).

BLACK = 0
RED = 1

class RBNode(object):

    def __init__(self, key = None, color = RED):
        self.left = self.right = self.parent = None
        self.color = color
        self.key = key
        self.nonzero = 1

    def __nonzero__(self):
        return self.nonzero

class RBTree:
    def __init__(self):
        self.sentinel = RBNode()
        self.sentinel.left = self.sentinel.right = self.sentinel
        self.sentinel.color = BLACK
        self.sentinel.nonzero = 0
        self.root = self.sentinel
        self.elements = 0

    def rotateLeft(self, x):

        y = x.right

        # establish x.right link
        x.right = y.left
        if y.left != self.sentinel:
            y.left.parent = x

        # establish y.parent link
        if y != self.sentinel:
            y.parent = x.parent
        if x.parent:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        else:
            self.root = y

        # link x and y
        y.left = x
        if x != self.sentinel:
            x.parent = y

    def rotateRight(self, x):

        #***************************
        #  rotate node x to right
        #***************************

        y = x.left

        # establish x.left link
        x.left = y.right
        if y.right != self.sentinel:
            y.right.parent = x

        # establish y.parent link
        if y != self.sentinel:
            y.parent = x.parent
        if x.parent:
            if x == x.parent.right:
                x.parent.right = y
            else:
                x.parent.left = y
        else:
            self.root = y

        # link x and y
        y.right = x
        if x != self.sentinel:
            x.parent = y

    def insertFixup(self, x):
        #************************************
        #  maintain Red-Black tree balance  *
        #  after inserting node x           *
        #************************************

        # check Red-Black properties

        while x != self.root and x.parent.color == RED:

            # we have a violation

            if x.parent == x.parent.parent.left:

                y = x.parent.parent.right

                if y.color == RED:
                    # uncle is RED
                    x.parent.color = BLACK
                    y.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent

                else:
                    # uncle is BLACK
                    if x == x.parent.right:
                        # make x a left child
                        x = x.parent
                        self.rotateLeft(x)

                    # recolor and rotate
                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self.rotateRight(x.parent.parent)
            else:

                # mirror image of above code

                y = x.parent.parent.left

                if y.color == RED:
                    # uncle is RED
                    x.parent.color = BLACK
                    y.color = BLACK
                    x.parent.parent.color = RED
                    x = x.parent.parent

                else:
                    # uncle is BLACK
                    if x == x.parent.left:
                        x = x.parent
                        self.rotateRight(x)

                    x.parent.color = BLACK
                    x.parent.parent.color = RED
                    self.rotateLeft(x.parent.parent)

        self.root.color = BLACK

    def deleteFixup(self, x):
        #************************************
        #  maintain Red-Black tree balance  *
        #  after deleting node x            *
        #************************************

        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.rotateLeft(x.parent)
                    w = x.parent.right

                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.rotateRight(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self.rotateLeft(x.parent)
                    x = self.root

            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.rotateRight(x.parent)
                    w = x.parent.left

                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.rotateLeft(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self.rotateRight(x.parent)
                    x = self.root

        x.color = BLACK

    def insertNode(self, key):
        #**********************************************
        #  allocate node for data and insert in tree  *
        #**********************************************

        # find where node belongs
        current = self.root
        parent = None
        while current != self.sentinel:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        # setup new node
        x = RBNode(key)
        x.left = x.right = self.sentinel
        x.parent = parent

        self.elements = self.elements + 1

        # insert node in tree
        if parent:
            if key < parent.key:
                parent.left = x
            else:
                parent.right = x
        else:
            self.root = x

        self.insertFixup(x)
        return x

    def deleteNode(self, z, M2=None, M1=None):
        #****************************
        #  delete node z from tree  *
        #****************************

        if not z or z == self.sentinel:
            return M1, M2

        if z.left == self.sentinel or z.right == self.sentinel:
            # y has a self.sentinel node as a child
            y = z
        else:
            # find tree successor with a self.sentinel node as a child
            y = z.right
            while y.left != self.sentinel:
                y = y.left

        if y is M2:
            M2 = z
        elif y is M1:
            M1 = z

        # x is y's only child
        if y.left != self.sentinel:
            x = y.left
        else:
            x = y.right

        # remove y from the parent chain
        x.parent = y.parent
        if y.parent:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        else:
            self.root = x

        if y != z:
            z.key = y.key

        if y.color == BLACK:
            self.deleteFixup(x)

        del y
        self.elements = self.elements - 1
        return M1, M2

    def findNode(self, key):
        #******************************
        #  find node containing data
        #******************************

        current = self.root

        while current != self.sentinel:
            if key == current.key:
                return current
            else:
                if key < current.key:
                    current = current.left
                else:
                    current = current.right

        return None

    def successor(self,node):
        if not node:
            return
        if node.right:
            n = node.right
            while n.left:
                n = n.left
            return n
        else:
            n = node
            while n.parent and n.parent.right is n:
                n = n.parent
            if n.parent and n.parent.left is n:
                return n.parent
            else:
                return

    def predecessor(self,node):
        if not node:
            return
        if node.left:
            n = node.left
            while n.right:
                n = n.right
            return n
        else:
            n = node
            while n.parent and n.parent.left is n:
                n = n.parent
            if n.parent and n.parent.right is n:
                return n.parent
            else:
                return

N = int(raw_input())
M1 = M2 = median = None
Tree = RBTree()
for i in range(N):
    s,x = raw_input().split()
    x=int(x)
    if s == "r":
        node = Tree.findNode(x)
        if not node:
            print("Wrong!")
            continue
        if M2 is None:
            print("Wrong!")
        elif M1 is None:
            if x == M2.key:
                val = M2
                M1 = Tree.predecessor(M2)
                M2 = Tree.successor(M2)
                M1, M2 = Tree.deleteNode(val, M2,M1)
                if Tree.elements == 0:
                    print("Wrong!")
                else:
                    median = (M1.key + M2.key)/2.0
                    if median%1 ==0:
                        median = int(median)
                    print(str(median))
            elif x<M2.key:
                M1 = M2
                M2 = Tree.successor(M2)
                M1, M2 = Tree.deleteNode(node,M2,M1)
                median = (M1.key + M2.key)/2.0
                if median%1 ==0:
                    median = int(median)
                print(str(median))
            else:
                M1 = Tree.predecessor(M2)
                M1, M2 = Tree.deleteNode(node,M2,M1)
                median = (M1.key + M2.key)/2.0
                if median%1 ==0:
                    median = int(median)
                print(str(median))
        else:
            if x == M1.key:
                val = M1
                M1 = None
                M1, M2 = Tree.deleteNode(val,M2)
            elif x == M2.key:
                val = M2
                M2 = M1
                M1 = None
                Tree.deleteNode(val)
            elif x < M1.key:
                M1 = None
                M1, M2 = Tree.deleteNode(node,M2,M1)
            elif x > M2.key:
                M2 = M1
                M1 = None
                Tree.deleteNode(node)
            median = M2.key
            print(str(median))
    else:
        if M2 is None:
            M2 = Tree.insertNode(x)
            median = M2.key
            print(str(median))
        elif M1 is None:
            if x >= M2.key:
                Tree.insertNode(x)
                M1 = M2
                M2 = Tree.successor(M2)
            elif x < M2.key:
                Tree.insertNode(x)
                M1 = Tree.predecessor(M2)
            median = (M1.key + M2.key)/2.0
            if median%1 ==0:
                median = int(median)
            print(str(median))
        else:
            if x>= M2.key:
                Tree.insertNode(x)
                M1 = None
            elif x< M1.key:
                Tree.insertNode(x)
                M2 = M1
                M1 = None
            else:
                Tree.insertNode(x)
                M2 = Tree.successor(M1)
                M1 = None
            median = M2.key
            print(str(median))