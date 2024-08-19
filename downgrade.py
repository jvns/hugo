import subprocess
import toml

with open("Gopkg.lock") as f:
    lock = toml.load(f)


for project in lock["projects"]:
    name = project["name"]
    revision = project["revision"]
    subprocess.check_call(["go", "get", f"{name}@{revision}"])
