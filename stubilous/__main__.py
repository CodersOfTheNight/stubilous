import yaml

from argparse import ArgumentParser

from stubilous.server import run
from stubilous.config import Config


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--config", help="Service configuration file")
    args = parser.parse_args()
    with open(args.config, "r") as f:
        config = Config.from_dict(yaml.load(f))
    run(config)
