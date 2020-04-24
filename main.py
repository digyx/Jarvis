from engine.index import Engine
import json
import sys

def run_subprocess():
    return


if __name__ == "__main__":
    subprocess = False

    for flag in sys.argv:
        if flag == "--docker":
            subprocess = True

    if subprocess:
        run_subprocess()
        exit()
    
    Engine.start()
