__all__ = ["server"]

if __name__ == "__main__":
    from argparse import ArgumentParser

    from stubilous.server import run
    parser = ArgumentParser()
    parser.add_argument("--config", help="Service configuration file")
    run(parser.parse_args())
