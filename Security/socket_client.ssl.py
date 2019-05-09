import socket
import ssl
import traceback

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Setup SSL Context
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # optional

# Connect the socket to the port where the server is listening
conn = context.wrap_socket(sock,'localhost')

try:
    conn.connect( ('localhost', 12890))
    # get message for sending
    message = input("enter your message: ")
    
    # send encoded data
    conn.write(message.encode('utf8'))
    
    # receive message from server
    receive_data = conn.read(4096)
    result = receive_data.decode('utf8')

    print('Result: {}'.format(result))
except:  
    traceback.print_exc()
finally:
    print('closing socket')
    conn.close()
    sock.close()

