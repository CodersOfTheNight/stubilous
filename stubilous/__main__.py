if __name__ == "__main__":
    from argparse import ArgumentParser
    import yaml

    from stubilous.server import run
    from stubilous.config import Config
    parser = ArgumentParser()
    parser.add_argument("--config", help="Service configuration file")
    args = parser.parse_args()
    with open(args.config, "r") as f:
        config = Config.from_dict(yaml.load(f))
    run(config)
