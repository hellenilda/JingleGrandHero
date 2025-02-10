# import socket
# localIP     = "10.0.0.118"


# def receber_ramking(): 	
# 		localPort   = 20030
# 		bufferSize  = 1024
# 		msgFromServer       = "Hello UDP Client"
# 		bytesToSend         = str.encode(msgFromServer)
# 		UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# 		UDPServerSocket.bind((localIP, localPort))
# 		print("SERVER ONLINE")
# 		bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
# 		message = bytesAddressPair[0]
# 		address = bytesAddressPair[1]
# 		print(f"Pontuação | {message}")
# 		UDPServerSocket.sendto(bytesToSend, address)



# def enviar_pontuacao():
# 	msg = input("> ")
# 	bytesToSend         = str.encode(msg)
# 	serverAddressPort   = (localIP, 2001)
# 	bufferSize          = 1024
# 	UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# 	UDPClientSocket.sendto(bytesToSend, serverAddressPort)
# 	UDPClientSocket.recvfrom(bufferSize)
	

# while True:
# 	enviar_pontuacao()
# 	receber_ramking()


































import socket
localIP     = "10.0.0.118"


def receber_ramking(): 	
		localPort   = 20030
		bufferSize  = 1024
		msgFromServer       = "Hello UDP Client"
		bytesToSend         = str.encode(msgFromServer)
		UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
		UDPServerSocket.bind((localIP, localPort))
		print("SERVER ONLINE")
		bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
		message = bytesAddressPair[0]
		address = bytesAddressPair[1]
		print(f"Pontuação | {message}")
		UDPServerSocket.sendto(bytesToSend, address)
		
def enviar_pontuacao():
	msg = input("> ")
	bytesToSend         = str.encode(msg)
	serverAddressPort   = (localIP, 2001)
	bufferSize          = 1024
	UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	UDPClientSocket.sendto(bytesToSend, serverAddressPort)
	UDPClientSocket.recvfrom(bufferSize)
	

while True:
	enviar_pontuacao()
	receber_ramking()
