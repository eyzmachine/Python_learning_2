# mod21 = __import__('mod2dot1')
# import sys
#
# print(sys.modules)
# import mod2dot1 as mod21
# print(sys.modules)

import datetime

def days_count():
	date_from_str = datetime.datetime.strptime(input(), '%Y %m %d')
	days_to = int(input())
	result = datetime.timedelta(days = days_to) + date_from_str
	print(result.year, result.month, result.day)
	
# days_count()

# import simplecrypt
#
# with open('password_task\encrypted.bin', 'rb') as encr_file:
# 	encr_data = encr_file.read()
# 	with open('password_task\passwords.txt', 'r') as passwords:
# 		stop = False
# 		for passw in passwords:
# 			try:
# 				print(passw, end = "")
# 				print(simplecrypt.decrypt(passw.strip(), encr_data).decode('utf8'))
# 				break
# 			except simplecrypt.DecryptionException:
# 				pass

x = list(range(10)[::-1])
print(x)