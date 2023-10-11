q = 1
qq = q
print(id(q))
print(id(1))
print(id(qq))
print(q == 1)

q = [1,2]
print(id(q))
print(id([1,2]))
print(q == [1,2])

qq = q
qqq = q
print(q)
print(qq)
print(qqq)
q[1] = 3
q.append(2)
print(q)
print(qq)
print(qqq)

print(type(q))
print(type(q[0]))
print(type(type(q[0])))

q = "123"
print(id(q))
q = "1234"
print(id(q))
q = "123"
print(id(q))

objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
objects.count([1,2])
q = list()
for item in objects:
	if(q.count(item) == 0):
		q.append(item)
print(len(q))

