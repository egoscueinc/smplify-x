from .main import main
from .cmd_parser import parse_config

if __name__ == "__main__":
    args = parse_config()
    main(**args)
