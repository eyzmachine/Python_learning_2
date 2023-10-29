def changer():
	i = 0
	s = input()
	a = input()
	b = input()
	while s.find(a) != -1:
		s = s.replace(a, b)
		i += 1
		if i == 1000:
			print("Impossible")
			return
	print(i)


def finder():
	s = input()
	t = input()
	i = 0
	find_sum = 0
	while i < len(s):
		try:
			ind = s[i:].index(t)
			if ind == 0:
				find_sum += 1
			i += 1
		except ValueError:
			break
	print(find_sum)