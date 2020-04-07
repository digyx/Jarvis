from exceptions import InvalidConfig
from docker import Docker
import json
import sys

# TODO: Add Flask web server

def load_config():
    try:
        with open("conf.json", "r") as file:
            conf = json.load(file)
    except FileNotFoundError:
        with open("conf.json", "w") as file:
            file.write("{'jobs': []}")
    
    try:
        for job in jobs:
            name = job.name
            url = job.url
    except:
        raise InvalidConfig

    return conf


def start_engine():
    try:
        conf = load_config()
    except InvalidConfig:
        print("Invalid config file.  Please check the reference guide at https://github.com/digyx/Jarvis")
        exit()

    while True:
        for job in conf.jobs:
            # TODO: Spin up a new thread to manage and run the Docker container
            pass


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
    
    start_engine()
