from pathlib import Path
from os import environ


def read_env():

    env_file = Path(__file__).parent.joinpath("../.env").absolute()
    env_dict = {}
    if env_file.exists():
        with env_file.open("r") as env_file:
            for line in env_file.readlines():
                if line.strip().startswith("#") or line.isspace():
                    continue
                line = line.rstrip()
                key, val = line.split("=")
                env_dict[key] = val
    env_dict = {**env_dict, **environ}
    return env_dict
