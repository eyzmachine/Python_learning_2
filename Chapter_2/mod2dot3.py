class multifilter:
	def judge_half(pos, neg): return pos >= neg

	def judge_any(pos, neg): return pos >= 1

	def judge_all(pos, neg): return neg == 0

	def __init__(self, iterable, *funcs, judge = judge_any):
		self.iterable = iterable
		self.funcs = funcs
		self.judge = judge
		
	def __iter__(self):
		pos = 0
		neg = 0
		for i in self.iterable:
			for f in self.funcs:
				res = f(i)
				if (res):
					pos += 1
				else:
					neg += 1
			if self.judge(pos, neg):
				yield i
			pos = 0
			neg = 0
		# return self.result_iterable.__iter__()
	
def mul2(x):
	return x % 2 == 0

def mul3(x):
	return x % 3 == 0

def mul5(x):
	return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]

import math
import itertools

def primes():
	i = 1
	while True:
		i += 1
		if ((math.factorial(i-1) + 1) % i == 0):
			yield i
			
print(list(itertools.takewhile(lambda x : x <= 31, primes())))