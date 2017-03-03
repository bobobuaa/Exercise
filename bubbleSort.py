#!/usr/bin/python    Running on other OS
# -*-coding:UTF-8-*- Chinese Instructions

def bubbleSort(number):
	for j in xrange(len(number)-1,-1,-1):
		for i in xrange(j):
			if number[i] > number[i+1]:
				number[i],number[i+1]=number[i+1],number[i]
	print number
def main():
	number=[1,3,8,4,2,6,7,9,10,0,11,63,78,52,14,13]
	bubbleSort(number)
	
if __name__=='__main__':
	main()
	