import yaml
import click

from stubilous.server import run
from stubilous.config import Config


@click.command()
@click.option("--config", help="Service configuration file")
def main(config_file):
    with open(config_file, "r") as f:
        config = Config.from_dict(yaml.load(f))
    run(config)


if __name__ == "__main__":
    main()
