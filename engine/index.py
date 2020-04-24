import json
from engine.config import EngineConfig, InvalidConfig
from engine import server

class Engine:

    @staticmethod
    def start():
        conf = EngineConfig()
        server.run()
