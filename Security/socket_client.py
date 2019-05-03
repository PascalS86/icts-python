import socket
import traceback

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
sock.connect(('localhost', 12890))

try:
    # get message for sending
    message = input("enter your message: ")
    
    # send encoded data
    sock.sendall(message.encode('utf8'))
    
    # receive message from server
    receive_data = sock.recv(4096)
    result = receive_data.decode('utf8')

    print('Result: {}'.format(result))
except:  
    traceback.print_exc()
finally:
    print('closing socket')
    sock.close()

