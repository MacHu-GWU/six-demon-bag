##encoding=UTF8

import configparser

config = configparser.ConfigParser()
# config["path_list"] = [r"C:\好的", r"C:\坏的"]

def write():
    config["DEFAULT"] = {
        "list": ["a", "b", "c"],
        "set": {1, 2, 3},
        "dic": {1: "a", 2: "b", 3: "c"},
        }
    config["user setting"] = {
        "value": 1
        }
    with open("config.cfg", "w") as f:
        config.write(f)
         
# write()

def read():
    with open("config.cfg", "rb") as f:
        content = f.read().decode("utf8")
    
    config.read_string(content)
    print(config.sections())
    print(config["DEFAULT"]["list"])
    print(config["user setting"]["value"])
    
read()