from pathlib import Path


def read_env():

    env_file = Path(__file__).parent.joinpath("../.env").absolute()
    env_dict = {}
    with env_file.open("r") as env_file:
        for line in env_file.readlines():
            if line.strip().startswith("#"):
                continue
            line = line.rstrip()
            key, val = line.split("=")
            env_dict[key] = val
    return env_dict
