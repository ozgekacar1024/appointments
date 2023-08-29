import json


def get_db_config():
    with open("config.json") as config_file:
        config = json.load(config_file)
    return config["database"]