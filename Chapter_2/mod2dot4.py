def vice_versa_1(filepath):
	with open(filepath, 'r') as source, open("reverse_" + filepath, 'w') as reverse:
		for line in source:
			line_to_write = line.rstrip()[::-1]
			if line[line.__len__() - 1] == '\n':
				reverse.write(line_to_write + '\n')
			else:
				reverse.write(line_to_write)

def vice_versa(filepath):
	with open(filepath, 'r') as source, open("reverse_" + filepath, 'w') as reverse:
		q = source.readlines()
		for line in q[::-1]:
			print(line, file = reverse, end = '')

vice_versa("test.txt")

import os
filepath = r'sort_task'
os.chdir(filepath)
dirs_bulk = set()
for current_dir, dirs, files in os.walk('.'):
	for filename in files:
		if filename[-3:] == '.py':
			dirs_bulk.add(current_dir.replace('.\\', ''))

with open(r".\answer.txt", "w") as f:
	print('\n'.join(sorted(dirs_bulk, key=str.lower)), file = f)