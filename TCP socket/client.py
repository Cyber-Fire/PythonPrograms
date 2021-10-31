import socket 
from colorama import Fore, init, Back;
from threading import *
import random 

init()

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

client_color = random.choice(colors)

clientSocket = socket.socket()
connected = False

def clientListener():
	while True:
		try:
			message = clientSocket.recv(1024).decode()
			print("\n", message)
		except socket.error as e:
			clientSocket.close()
			break


host = "localhost"
port = 12345
seprator_token = "<NEP>"
disconectMessage = "!DISCONNECT"

def serverConnect():
	print("waiting for connection")
	try:
		clientSocket.connect((host, port))
	except socket.error as e:
		print(str(e))
	t = Thread(target=clientListener, args=())
	t.daemon = True
	t.start()
	name = input("Enter your name")
	clientSocket.send(name.encode())
	print("To quit type q\ntype receiver username before typing message-username_\nfor multiple users use username1_username2_...\nFor sending to all users, type all_")
	while True:
		data = input()
		if data.lower() == "q":
			break

		datasend = f"{client_color} {name}{seprator_token}{data}{Fore.RESET}"

		clientSocket.send(datasend.encode())

	clientSocket.send(disconectMessage.encode())
	clientSocket.close()



while True:
	print("To connect to the server press c and q to quit the program")

	a = input()

	if a.lower() == "c":
		connected = True
		serverConnect()
	else:
		if a.lower() == "q":
			break





