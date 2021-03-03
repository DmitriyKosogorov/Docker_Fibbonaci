#!/usr/bin/env python3

import sys

fib_nums=[1,1]
def fib(N):
	if N < 2:
		return 1
	if N > len(fib_nums):
		return fib(N-1)+fib(N-2)
	elif N==len(fib_nums):
		fib_nums.append(fib(N-1)+fib(N-2))
	return fib_nums[N]
for a in sys.argv:
	if a.isdigit():
		print(fib(int(a)))
