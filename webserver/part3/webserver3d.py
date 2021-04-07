import os
import socket
import time

SERVER_ADDRESS = (HOST, PORT) = "", 8888
REQUEST_QUEUE_SIZE = 5


def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(f"Child PID: {os.getpid()} / Parent PID {os.getppid()}")
    print(request.decode())
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    time.sleep(60)


def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print(f"Serving HTTP on port {PORT} ...")
    print(f"Parent PID (PPID): {os.getpid()}\n")

    clients = []
    while True:
        client_connection, client_address = listen_socket.accept()
        clients.append(client_connection)
        pid = os.fork()
        if pid == 0:    # child
            listen_socket.close()   # close child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)  # child exits here
        else:   # parent
            # client_connection.close()   # close parent copy and loop over
            print(len(clients))


if __name__ == "__main__":
    serve_forever()
