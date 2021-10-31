import socket
import os
from threading import *

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost"
port = 12345

seprator_token = "<NEP>"
disconectMessage ="!DISCONNECT"
threadCount = 0
clientSockets = set()
nameaccess={}

Server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
	Server.bind((host, port))

except socket.error as e:
	print(str(e))

print("Server Listening on port " + str(port))

Server.listen(5)

def ServerListner(cs):
	while True:
		try:
			msg = cs.recv(1024).decode()
		except Exception as e:
			print(f"Error: {e}")
			cs.close()
			break
			# clientSockets.remove(cs)
		else:
			if msg == disconectMessage:
				cs.close()
				break

			msg = msg.replace(seprator_token, ": ")
			print(msg)
			counter=0
			finname=''
			while msg[counter]!=':':
				finname+=msg[counter]
				counter+=1
			counter+=2
			namestr=''
			counter2=0
			underscorePresent=0
			while counter2<len(msg):
			    if msg[counter2]=='_':
			        underscorePresent=1
			        break
			    counter2+=1
			if underscorePresent==0:
			    namestr="all"
			else:
			    while msg[counter]!=' ':
			        namestr+=msg[counter]
			        counter+=1
			names=[] 
			temp=''
			print(namestr)
			msg2=''
			while counter<len(msg):
				msg2+=msg[counter]
				counter+=1
			for letter in namestr:
			    if letter!='_':
			        temp+=letter
			    else:
			        if temp=='all':
			            names=clientSockets
			            break
			        if temp not in nameaccess.keys():
			            print('mentioned user not present')
			            continue
			        names.append(nameaccess[temp])
			        temp=''
		msg=finname+': '+msg2
		if(len(names)==0):
			names=clientSockets
		
		for client_socket in names:
		    if client_socket not in clientSockets:
		        print(f"{client_socket} has been terminated, can't send message")
		        continue
		    try:
		        client_socket.send(msg.encode())
		    except socket.error as e:
		        client_socket.close()
		        clientSockets.remove(client_socket)
		        
	clientSockets.remove(cs)


while True:
	cs, caddr = Server.accept()
	print(f"[+] {caddr} connected to server.")
	
	clientSockets.add(cs)
	print(f"Total active connections: {len(clientSockets)}")
	welcome = f"Thanks for Connecting to the server {caddr}"
	cs.send(welcome.encode())
	usname = cs.recv(1024).decode()
	print(usname)
	nameaccess[usname]=cs
	t = Thread(target=ServerListner, args=(cs,))
	t.daemon = True
	t.start()


for cs in clientSockets:
	cs.close()

Server.close()