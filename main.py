from engine.index import Engine
import json
import sys

if __name__ == "__main__":
    subprocess = False

    for flag in sys.argv:
        if flag == "--docker":
            subprocess = True

    if subprocess:
        print("This is a subprocess")
        exit()
    
    Engine.start()
