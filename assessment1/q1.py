#!/usr/bin/env python3

def move_zeroes(x):
	l = [0]
	non_zeroes = [i for i in x if i not in l]
	zeroes = [i for i in x if i not in non_zeroes]
	return non_zeroes + zeroes

'''
if __name__=='__main__':
    print(move_zeroes([0,3,0,1,22,12,0]))

'''