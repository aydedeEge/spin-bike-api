import json
import os

filename = "config.json"

def read_config():
    with open(filename, 'r') as f:
        data = json.load(f)

    write_env_vars(data)

def write_env_vars(data):
    os.environ["HOST"] = data["host"]
    os.environ["USER"] = data["user"]
    os.environ["PASSWORD"] = data["password"]
    os.environ["PORT"] = data["port"]
    os.environ["DB"] = data["db"]
    os.environ["EUSER"] = data["email_user"]
    os.environ["EPWD"] = data["email_pwd"]
