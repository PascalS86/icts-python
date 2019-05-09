import socket
import ssl
import traceback

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 12890)
try:
    print('starting up on {} port {}'.format(*server_address))
    # Bind to socket
    sock.bind(server_address)

    # start listening to 1 connection
    sock.listen(1)

    while True:
        # Wait for a connection
        conn, addr = sock.accept()
        secure_sock = ssl.wrap_socket(conn, server_side=True)
        try:
            print('Connection from ', addr)
            while True:
                receive_data = secure_sock.read(4096)
                if receive_data:
                    print('sending answer')
                    secure_sock.write('received'.encode('utf8'))
                else:
                    print('no data')
                    break
        except:
            traceback.print_exc()
            break
        finally:
            # Close connection
            secure_sock.close()
            conn.close()
except:
    traceback.print_exc()

