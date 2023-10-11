x, y = 1, 2

def glob():
	global x
	x = 10

glob()
print(x)

def loc():
	x = 20
	print(x)
	def check_loc():
		nonlocal x
		x = 11
	check_loc()
	print(x)
		
loc()
print(x)

def something():
	parent_word = "parent"
	namespaces = {"global" : {parent_word : None}}
	n = int(input())
	def create(namespace_name, namespace_parent):
		nonlocal namespaces
		if not namespace_name in namespaces.keys():
			namespaces[namespace_name] = dict()
			namespaces[namespace_name][parent_word] = namespace_parent
	def add(namespace_name, var_name):
		nonlocal namespaces
		if namespace_name in namespaces.keys():
			namespaces[namespace_name][var_name] = var_name
	def get(namespace_name, var_name):
		nonlocal namespaces
		if namespace_name not in namespaces.keys():
			print(None)
		else:
			if var_name not in namespaces[namespace_name]:
				get(namespaces[namespace_name][parent_word], var_name)
			else:
				print(namespace_name)
	while n > 0:
		com, first, second = map(str, input().split())
		if(com == "create"):
			create(first, second)
		elif(com == "add"):
			add(first, second)
		elif(com == "get"):
			get(first, second)
		n -= 1
		continue
		
something()