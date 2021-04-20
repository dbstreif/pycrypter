import pyfiglet
from colorama import Fore, Back, Style, init
import time
from platform import system
import base64
from sys import exit
from signal import signal, SIGINT
import os
from cryptography.fernet import Fernet

def handler(signal_received, frame):
	print(Fore.GREEN + "\n\nGoodbye!" + Style.RESET_ALL)
	exit(0)

def main():
	path = None

	def base32en():
		imports_array = ['import base64']
		code_array = []
		code_str = ""
		try:
			input_file = open(path).read().splitlines()
		except:
			print(Fore.RED + "Invalid file path!" + Style.RESET_ALL)
			return
		for i in input_file:
			if i.startswith("import") or i.startswith("from"):
				imports_array.append(i)
			else:
				code_array.append(i)
		try:
			os.mkdir("output")
		except:
			pass
		output_file = open(os.path.join("output", "output.py"), "w+")
		for i in imports_array:
			output_file.write(i + '\n')
		for i in code_array:
			code_str += '\n' + i
		encoded = base64.b32encode(bytes(code_str, "utf-8"))
		output_file.write('\n' + "exec(base64.b32decode(" + str(encoded) + "))")
		output_file.close()

	def ferneten():
		imports_array = ['from cryptography.fernet import Fernet']
		code_array = []
		code_str = ""
		try:
			input_file = open(path).read().splitlines()
		except:
			print(Fore.RED + "Invalid file path!" + Style.RESET_ALL)
			return
		for i in input_file:
			if i.startswith("import") or i.startswith("from"):
				imports_array.append(i)
			else:
				code_array.append(i)
		try:
			os.mkdir("output")
		except:
			pass
		output_file = open(os.path.join("output", "output.py"), "w+")
		for i in imports_array:
			output_file.write(i + '\n')
		for i in code_array:
			code_str += '\n' + i
		key = Fernet.generate_key()
		f = Fernet(key)
		encrypted = f.encrypt(bytes(code_str, "utf-8"))
		output_file.write('\n' + "key = " + str(key) + "\nf = Fernet(key)" + "\n\nexec(f.decrypt(" + str(encrypted) + "))")
		output_file.close()

	def base64en():
		imports_array = ['import base64']
		code_array = []
		code_str = ""
		try:
			input_file = open(path).read().splitlines()
		except:
			print(Fore.RED + "Invalid file path!" + Style.RESET_ALL)
			return
		for i in input_file:
			if i.startswith("import") or i.startswith("from"):
				imports_array.append(i)
			else:
				code_array.append(i)
		try:
			os.mkdir("output")
		except:
			pass
		output_file = open(os.path.join("output", "output.py"), "w+")
		for i in imports_array:
			output_file.write(i + '\n')
		for i in code_array:
			code_str += '\n' + i
		encoded = base64.b64encode(bytes(code_str, "utf-8"))
		output_file.write('\n' + "exec(base64.b64decode(" + str(encoded) + "))")
		output_file.close()
		

	print("\nUse the \"help\" command to display options\n")

	while True:
		prompt = input(Fore.YELLOW + "(Pycrypter$) " + Style.RESET_ALL)
		if prompt == "base64":
			path = input("Enter the absolute path of your file: ")
			base64en()
		elif prompt == "base32":
			path = input("Enter the absolute path of your file: ")
			base32en()
		elif prompt == "fernet":
			path = input("Enter the absolute path of your file: ")
			ferneten()
		elif prompt == "path":
			print("Your current path is: " + str(path))
		elif prompt == "exit":
			print(Fore.GREEN + "\nGoodbye!" + Style.RESET_ALL)
			exit(0)
		elif prompt == "help":
			print("Encrytion types: Fernet, Base32, Base64\nOptions: help, exit, path")
		elif prompt == "clear":
			if system() == "Linux":
				os.system("clear")
			elif system() == "Windows":
				os.system("cls")
		else:
			print(Fore.RED + "Invalid option" + Style.RESET_ALL)

if __name__ == '__main__':
	signal(SIGINT, handler)
	if system() == "Windows":
		init(convert=True)
	print(Fore.RED + pyfiglet.figlet_format('Pycrypter', font='slant') + Style.RESET_ALL)
	print(Back.BLUE + "*A Python encrypter for bypassing AV*" + Style.RESET_ALL + "\n" + Back.RED + "            By Dom13377               " + Style.RESET_ALL)
	main()
