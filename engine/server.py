import socket
import time
from connection import Connection

class Server:
    counter = 0

    def __init__(self, conf):
        self.conf = conf

    @classmethod
    def start(cls):
        sock = socket.socket()
        port = 8080

        sock.bind(('', port))
        sock.listen(16)
        print("Server is listening...")

        while True:
            if cls.counter == 16:
                time.sleep(1)
                continue
            client, _ = sock.accept()
            conn = Connection(client)
            conn.start()
