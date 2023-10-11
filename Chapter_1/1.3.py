def sum_orig(x, y = 666): return x + y

print(type(sum_orig(1,2)))
print(type(sum_orig))
print(id(sum_orig(1,2)))
print(id(sum_orig))

print(list(map(sum_orig, range(1,10))))
print(list(map(sum_orig, range(1,10), range(1,10))))

q = None
print(q)
print(type(q))
print(id(q))
print(id(None))

def closest_mod_5(x):
	while (x % 5 != 0):
		x += 1
	return x

print(closest_mod_5(0))
print(closest_mod_5(5))
print(closest_mod_5(7))
print(closest_mod_5(10))
print(closest_mod_5(151))

print(sum_orig(1,2))
print(sum_orig(y = 1, x = 2))
print(sum_orig(1, y = 2))
lst = [1,2]
print(sum_orig(*lst))
dict = {'x': 1, 'y': 2}  # ключи должны соответствовать названиям входных параметров
print(sum_orig(**dict))
print(sum_orig(1))

def sum(a, b, *cdef,  **kwargs):
	sum = a + b
	for item in cdef:
		sum += item
	for key in kwargs:
		sum += kwargs[key]
	return sum

print(sum(1,2,3,4,5,6))
print(sum(1,2, c = 3, d = 4, e = 5, f = 6))
print(sum(1, c = 3, d = 4, e = 5, f = 6, b = 2))

def fib(x): return 1 if (x == 0 or x == 1) else (fib(x-1) + fib(x-2))

cache = {}
def cached_fib(x):
	if(x == 0 or x == 1):
		return 1
	elif (cache.keys().__contains__(x)):
		return cache[x]
	else:
		y = cached_fib(x - 1) + cached_fib(x - 2)
		cache[x] = y
		return y

print(cached_fib(55))

def subset_count(n, k):
	if (k > n):
		return 0
	elif (k == 0):
		return 1
	else:
		return subset_count(n - 1, k) + subset_count(n - 1, k - 1)

n, k = map(int, input().split())
print(subset_count(n, k))