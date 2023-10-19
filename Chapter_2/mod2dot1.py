print(AssertionError.mro())
print(ZeroDivisionError.mro())

def foo():
	raise AssertionError

try:
	foo()
except ZeroDivisionError:
	print(ZeroDivisionError.__name__)
except ArithmeticError:
	print(ArithmeticError.__name__)
except AssertionError:
	print(AssertionError.__name__)
	
exceptions = dict()

def check_exp(anc, desc):
	if list(exceptions[desc]).__contains__(anc):
		return True
	else:
		decision = False
		for exp in exceptions[desc]:
			decision = check_exp(anc, exp)
			if decision:
				return decision
		return decision

def graphs():
	n = int(input())
	while n > 0:
		input_exp = input()
		split_exp = list(map(str.strip, input_exp.split(":")))
		if split_exp.__len__() == 1:
			exceptions[split_exp[0]] = list()
		else:
			exceptions[split_exp[0]] = split_exp[1].split(' ')
		n -= 1

	q = int(input())
	prev_exps = list()
	while q > 0:
		input_exp = input()
		for prev_exp in prev_exps:
			if(check_exp(prev_exp, input_exp)):
				print(input_exp)
				break
		if(not prev_exps.__contains__(input_exp)):
			prev_exps.append(input_exp)
		q -= 1

if (__name__ == "__main__"):
	graphs()

class NonPositiveError(Exception):
	pass

class PositiveList(list):
	def append(self, x):
		if (x <= 0):
			raise NonPositiveError
		else:
			super().append(x)