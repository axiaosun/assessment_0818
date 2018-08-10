#!/usr/bin/env python3

import sys

def move_zeroes(x):
	for i in range(len(x)):
		for j in range(0,len(x)-i-1): 
			if x[j] == 0:
				x.remove(x[j])
			print (x)

if __name__=='__main__':
    move_zeroes([0,1,0,3,12])