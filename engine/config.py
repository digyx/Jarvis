import json
import yaml

class EngineConfig:
    def __init__(self):
        try:
            with open("conf.json", "r") as file:
                conf = json.load(file)
        except FileNotFoundError:
            with open("conf.json", "w") as file:
                file.write("{\"jobs\": []}")
                conf = {"jobs": []}
        
        # Check to make sure config file is valid
        if "jobs" not in conf.keys():
            print("Invalid config: 'jobs' object does not exist")
            exit()

        self.jobs = conf["jobs"]


class JobConfig:
    def __init__(self, yaml_file, name, git_repo):
        raw_conf = yaml.load(yaml_file)

        self.name = name
        self.git_repo = git_repo
        self.language = raw_conf["lanugage"]
        self.dependencies = raw_conf["dependencies"]
        self.env_vars = raw_conf["env"]
        self.commands = raw_conf["commands"]


class InvalidConfig(Exception):
    """Raised when the JSON config file for Jarvis doesn't have the required sections."""
    pass
