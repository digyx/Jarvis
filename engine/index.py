import json
from config import EngineConfig, InvalidConfig
from server import Server

class Engine:

    @staticmethod
    def start():
        conf = EngineConfig()

        server = Server(conf)
        server.start()
