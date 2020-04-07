import yaml

class Config:
    def __init__(self, yaml_file, name, git_repo):
        raw_conf = yaml.load(yaml_file)

        self.name = name
        self.git_repo = git_repo
        self.language = raw_conf["lanugage"]
        self.dependencies = raw_conf["dependencies"]
        self.env_vars = raw_conf["env"]
        self.commands = raw_conf["commands"]
