import sys
import re

def cat_finder():
	for line in sys.stdin:
		line = line.rstrip()
		q = re.findall(r'cat', line)
		if len(q) >= 2:
			print(line)

def cat_finder2():
	for line in sys.stdin:
		line = line.rstrip()
		if re.match(r'.*\bcat\b.*', line) is not None:
			print(line)
		
def z_finder():
	for line in sys.stdin:
		line = line.rstrip()
		if re.match(r'.*z.{3}z.*', line) is not None:
			print(line)

def slash_finder():
	for line in sys.stdin:
		line = line.rstrip()
		if re.match(r'.*\\+.*',
					line) is not None:
			print(line)

def tandem_finder():
	for line in sys.stdin:
		line = line.rstrip()
		if re.match(r'\b(\w+)\1\b', line) is not None:
			print(line)
			
def computer_changer():
	for line in sys.stdin:
		line = line.rstrip()
		print(re.sub(r'human', 'computer', line))

def aaa_changer():
	for line in sys.stdin:
		line = line.rstrip()
		print(re.sub(r'\b[aA]+\b', 'argh', line, 1))
		
def first_changer():
	for line in sys.stdin:
		line = line.rstrip()
		lst = str.split(line)
		new_list = list()
		for word in lst:
			new_word = word
			if re.match(r'.*\w{2,}.*', word) is not None:
				new_word = re.sub(r'(\b)(\w)(\w)(\w*)(\b)', r'\1\3\2\4\5', word)
			new_list.append(new_word)
		print(' '.join(new_list))

def return_group_1(m):
	return m.group(1)

def repeat_changer():
	for line in sys.stdin:
		line = line.rstrip()
		print(re.sub(r'(\w{1})\1+', return_group_1, line))
		
def bi_finder():
	for line in sys.stdin:
		line = line.rstrip()
		if re.match(r'^[01]+$', line) is not None:
			number = line[::-1]
			odd = 0
			even = 0
			i = 0
			for digit in number:
				if i % 2 == 0 and int(number[i]) == 1:
					even += 1
				elif i % 2 == 1 and int(number[i]) == 1:
					odd += 1
				i += 1
			if (abs(even - odd)) % 3 == 0:
				print(line)

bi_finder()