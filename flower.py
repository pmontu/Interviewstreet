#!/bin/python

#You and your K-1 friends want to buy N flowers. Flower number i has host ci. Unfortunately the seller does not like a customer to buy a lot of flowers, so he tries to change the price of flowers for customer who had bought flowers before. More precisely if a customer has already bought x flowers, he should pay (x+1)*ci dollars to buy flower number i.
#You and your K-1 firends want to buy all N flowers in such a way that you spend the as few money as possible.
#
#Input:
#
#The first line of input contains two integers N and K.
#next line contains N positive integers c1,c2,...,cN respectively.
#
#Output:
#
#Print the minimum amount of money you (and your friends) have to pay in order to buy all n flowers.
#
#Sample onput :
#
#3 3
#2 5 6
#
#Sample output :
#
#13
#
#Explanation :
#In the example each of you and your friends should buy one flower. in this case you have to pay 13 dollars.
#
#Constraint :
#
#1 <= N, K  <= 100
#Each ci is not more than 1000,000

def InsertionSort(numbers):
	N = len(numbers)
	for p in range(1,N):
		temp = numbers[p]
		j=p
		while j>0:
			if numbers[j-1] > temp:
				numbers[j] = numbers[j-1]
			else:
				break
			j = j-1
		numbers[j] = temp

def QS(numbers,left,right):
	if right - left<=2:
		InsertionSort(numbers)
	else:
		center = int((left + right)/2)
		if numbers[left]>numbers[center]:
			numbers[center],numbers[left] = numbers[left],numbers[center]
		if numbers[left]>numbers[right]:
			numbers[left],numbers[right] = numbers[right],numbers[left]
		if numbers[center]>numbers[right]:
			numbers[center],numbers[right] = numbers[right],numbers[center]
		numbers[center],numbers[right-1] =  numbers[right-1],numbers[center]
		pivot = numbers[right-1]
		i = 1
		j=right-2
		while(True):
			while numbers[i]<pivot:
				i=i+1
			while numbers[j]>pivot:
				j=j-1
			if i<j:
				numbers[i],numbers[j]=numbers[j],numbers[i]
			else:
				break;
		numbers[i],numbers[right-1] = numbers[right-1],numbers[i]
		QS(numbers,left,i-1)
		QS(numbers,i+1,right)

N, K = input().split()
N = int(N)
K = int(K)
C = []

numbers = input()

i = 0
for number in numbers.split():
	C.append( int(number) )
	i = i+1

result = 0

QS(C, 0, len(C) - 1)
len_c = len(C)
j=len_c-1
x=1
while j>=0:
	for i in range(0,K):
		result = result + (x*C[j])
		j=j-1
		if j<0:
			break
	x=x+1

print(result)