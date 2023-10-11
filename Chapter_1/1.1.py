def fib(x):
	y = 1 if x <= 2 else (fib(x - 1) + fib(x - 2))
	return y

def strange():
	i = 0
	n = 0
	rows_count = int(input())
	while i < rows_count:
		n += int(input())
		i += 1
	print(n)
	
# print(fib(31))
strange()