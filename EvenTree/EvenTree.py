# circular buffer
#
# Author: Manojkumar Purushothaman
#
# Date created: Aug 28 2012
# Date updated: Aug 29 2012
#===================================

# You are given a tree (a simple connected graph with no cycles).You have to remove as many edges from the tree as possible to obtain a forest with the condition that : Each connected component of the forest contains even number of vertices
# 
# Your task is to calculate the number of removed edges in such a forest.
# 
# Input:
# The first line of input contains two integers N and M. N is the number of vertices and M is the number of edges. 2 <= N <= 100. 
# Next M lines contains two integers ui and vi which specifies an edge of the tree. (1-based index)
# 
# Output:
# Print a single integer which is the answer
# 
# Sample Input 
# 
# 10 9
# 2 1
# 3 1
# 4 3
# 5 2
# 6 1
# 7 2
# 8 6
# 9 8
# 10 8
#  
# Sample Output :
# 2
#  
# Explanation : On removing the edges (1, 3) and (1, 6), we can get the desired result.
# Original tree: 
# 
# 
# Decomposed tree:
# 
# 
# Note: The tree in the input will be such that it can always be decomposed into components containing even number of nodes. 

N, M = raw_input().strip().split()
N = int(N)
M = int(M)

#adjacency list
G = {}
for i in range(M):
    u, v = raw_input().strip().split()
    u = int(u)
    v = int(v)
    try:
        G[u].append([v,"-"])
    except KeyError:
        G[u] = []
        G[u].append([v,"-"])
    try:
        G[v].append([u,"-"])
    except KeyError:
        G[v] = []
        G[v].append([u,"-"])

def getLeaves(G):
    leaves = []
    for node in G:
        if len(G[node])==1:
            leaves.append(node)
    return leaves

def delete(G,fr,to):
    #print(fr,to)
    i=0
    for edge in G[to]:
        if edge[0] == fr:
            del(G[to][i])
            break
        i += 1
    if len(G[to]) == 0:
        del(G[to])

    i=0
    for edge in G[fr]:
        if edge[0] == to:
            del(G[fr][i])
            break
        i += 1
    if len(G[fr]) == 0:
        del(G[fr])
    else:
        #print(G[fr])
        edges = []
        for edge in G[fr]:
            edges.append(edge[0])
        for edge in edges:
            delete(G,edge,fr)

def disconnect(G,fr,to):
    delete(G,fr,to)
    return

result = 0
while True:
    disconnected = False
    #print("start")
    #print(G)
    leaves = getLeaves(G)
    #print(leaves)
    for leave in leaves:
        G[leave][0][1] = "x"
        #reverse
        for edge in G[G[leave][0][0]]:
            if edge[0] == leave:
                edge[1] = "x"
    #print("x on leaves")
    #print(G)
    for leaf in leaves:
        next = G[leaf][0][0]
        while True:
            count = len(G[next])
            count_x = 0
            i=0
            for edge in G[next]:
                if edge[1] == "x":
                    count_x += 1
                else:
                    oneedge = edge[0]
                    index = i
                i += 1
            if count == count_x + 1 and count_x%2==1:
                result += 1
                disconnect(G,next,oneedge)
                disconnected = True
                #print("disconnected")
                #print(G)
                break
            elif count == count_x + 1 and count_x%2==0:
                G[next][index][1] = "x"
                for edge in G[oneedge]:
                    if edge[0] == next:
                        edge[1] = "x"
                next = oneedge
                #print("even")
                #print(G)
            else:
                break
        if disconnected:
            break
        c = 0
        o = 0
        for node in G:
            for item in G[node]:
                if item[1] == "x":
                    c += 1
                o += 1
        if c == o:
            #print("end")
            #print(G)
            print(result)
            exit()