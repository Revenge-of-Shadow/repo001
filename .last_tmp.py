import time
t1 = time.time()
count = 0
file_1 = open('file1.txt', 'a')
file_1.close()
def strt():
	def sifer(arr):
		x = 0
		arr.reverse()
		abc = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W', 'X','Y','Z','1','2','3','4','5','6','7','8','9','0', '_', '.', ',', '-')
		for x in range(0, len(arr)):
			if ((abc.index(arr[x])+2) >= (len(abc)-1)):
				arr[x] = abc[abc.index(arr[x])+2 - len(abc)]
			else:
				arr[x] = abc[abc.index(arr[x])+2]
	def file_w(log, passw):
		log_s = ''.join(map(str, log))
		passw_s = ''.join(map(str, passw))
		file_1 = open('file1.txt', 'a')
		count =+ 1
		file_1.write(str(count) + ' ')
		file_1.write(log_s + " ")
		file_1.write(passw_s + " ")
		file_1.write('\n')
		file_1.close()
	def reg():
		login = input("Login:")
		corr_log = True
		if(len(login) < 3):
			print("Too short login.")
			corr_log = False
		elif(len(login) > 20):
			print("Too long login.")
			corr_log = False
		login_arr = list(login)
		wrong_symb = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", "~", ";", ":", "?", "/", "|", "\\", "{", "}", "[", "]", "<", ">")
		x = 0
		y = 0
		for x in range (len(login_arr)):
			if (login_arr[x] in wrong_symb):
				corr_log = False
			x = x + 1
		if(corr_log == False):
			x = 0
			print("Incorrect login.")
			print("Incorrect symbols: ")
			for x in range (len(login_arr)):
				if (login_arr[x] in wrong_symb):
					print(login_arr[x])
				x = x + 1
			reg()
		else:
			print("Correct login.")
			print("Password:")
			password = input()
			corr_passw = True
			if(len(password) < 3):
				print("Too short password.")
				corr_passw = False
			elif(len(password) > 20):
				print("Too long password.")
				corr_passw = False
			password_arr = list(password)
			x = 0
			y = 0
			for x in range (len(password_arr)):
				if (password_arr[x] in wrong_symb):
					corr_passw = False
					break
				x = x + 1
			if(corr_passw == False):
				print("Incorrect password.")
				print("Incorrect symbols: ")
				x = 0
				for x in range (len(password_arr)):
					if (password_arr[x] in wrong_symb):
						print(password_arr[x])
					x = x + 1
				reg()
			else:
				print("Correct password.")
				if(login == "admin" and password == "1234" or login == "Admin" and password == "1234"):
					print("congratulations, you are admin.")
				print("You registered as %s. Your password is %s." % (login, password))
				sifer(login_arr)
				sifer(password_arr)
				file_w(login_arr, password_arr)
				start()

	def start():
		print("Register? [Y/N]")
		if(input()=="Y"):reg()
		else:print(time.time() - t1)
	start()
strt()