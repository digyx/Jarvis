from config import Config
import threading
import subprocess

class Docker:
    def __init__(self, name, git_repo):
        with open("jarvis.yml", "r") as conf_file:
            self.conf = Config(conf_file, name, git_repo)
        
        self.install_dependencies()

    def run(self):
        subprocess.run("cd %s" % self.conf.name)
        for cmd in self.conf.commands:
            proc = subprocess.Popen(cmd)
            proc.communicate()

    def install_dependencies(self):
        lang = self.conf.language

        if lang == "python":
            proc = subprocess.Popen("pip install -r %s" % self.conf.dependencies, shell=False)
            proc.communicate()
        elif lang == "golang":
            proc = subprocess.Popen("go mod download")
            proc.communicate
