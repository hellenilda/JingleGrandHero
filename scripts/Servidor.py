# import socket
# localIP     = "10.15.2.98"
# localPort   = 2001
# bufferSize  = 1024
# msgFromServer       = "Hello UDP Client"
# bytesToSend         = str.encode(msgFromServer)
# UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# UDPServerSocket.bind((localIP, localPort))



# def envio_da_pontuacao():
#     with open('Pontuação.txt' ,'r') as pt:
#         msg = pt.read()
#         bytesToSend         = str.encode( msg )
#         serverAddressPort   = (localIP, 20030)
#         bufferSize          = 1024
#         UDPClientSocket     = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#         UDPClientSocket.sendto(bytesToSend, serverAddressPort)
#         UDPClientSocket.recvfrom(bufferSize)   





# def recebimentos_pontos():
#     bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
#     message = bytesAddressPair[0]
#     address = bytesAddressPair[1]
#     print(f" Pontos | {message}")
#     with open('Pontuação.txt' ,'w') as pt:
#         message = str(message)
#         pt.write(message)
#     UDPServerSocket.sendto(bytesToSend, address)
#     envio_da_pontuacao()






# while True: 
#     recebimentos_pontos()














import socket
import pyautogui as pt
localIP     = "10.0.0.118"
localPort   = 2001
bufferSize  = 1024
msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))



def envio_da_pontuacao():
    with open('Pontuação.txt' ,'r') as pt:
        pt_1 = pt.read()
        bytesToSend         = str.encode(pt_1)
        serverAddressPort   = (localIP, 20030)
        bufferSize          = 1024
        UDPClientSocket     = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        print("MSG enviada")
        UDPClientSocket.recvfrom(bufferSize)   

    # if pt_2 > pt_1:
    #     print("Pontuação do segundo jogador é maior")
    #     bytesToSend         = str.encode( """ Pontuação do Jogador {pt_1}
    #     Pontuação do Jogador 2 {pt_2}""" )
    #     serverAddressPort   = (localIP, 20030)
    #     bufferSize          = 1024
    #     UDPClientSocket     = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    #     UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    #     UDPClientSocket.recvfrom(bufferSize)   





def recebimentos_pontos():
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        print(f" Pontos | {message}")
        print(f' Pessoa | {address}')
        with open('Pontuação.txt' ,'w') as pt:
            message = str(message)
            pt.write(message)
        UDPServerSocket.sendto(bytesToSend, address)
        # envio_da_pontuacao()

while True: 
    recebimentos_pontos()