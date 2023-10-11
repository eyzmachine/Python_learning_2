class ExtendedStack(list):
	def sum(self):
			x = self.pop()
			y = self.pop()
			self.append(x + y)
	
	def sub(self):
			x = self.pop()
			y = self.pop()
			self.append(x - y)
	
	def mul(self):
			x = self.pop()
			y = self.pop()
			self.append(x * y)
	
	def div(self):
			x = self.pop()
			y = self.pop()
			self.append(x // y)


def test():
	ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
	ex_stack.div()
	assert ex_stack.pop() == 2
	ex_stack.sub()
	assert ex_stack.pop() == 6
	ex_stack.sum()
	assert ex_stack.pop() == 7
	ex_stack.mul()
	assert ex_stack.pop() == 2
	assert len(ex_stack) == 0


test()
