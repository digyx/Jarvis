import threading
import json
from docker import Docker

class Connection(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        msg = self.client.recv(4096).decode('ascii')
        job = json.loads(msg)

        name = job["repository"]["name"]
        repo = job["repository"]["html_url"]

        docker = Docker(name, repo)
        docker.run()

        self.client.close()
