# Heavily relied on https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/ to learn the basic functions and syntaxes of python

def randomShuffle(n):
	array = [None] * n
	for i in range(n):
		array[i] = i + 1
	import random
	#array.reverse()
	random.shuffle(array)
	#print array
	flips = 0
	for i in range(len(array)):
		i=0
		flipped = False
		for i in range(len(array) - 1):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
				flipped = True
				flips+=1
			i+=1
		if flipped == False: 
			break
	#print array
	print flips

def main ():
	randomShuffle(1)
	randomShuffle(2)
	randomShuffle(3)
	randomShuffle(4)
	randomShuffle(5)


	

