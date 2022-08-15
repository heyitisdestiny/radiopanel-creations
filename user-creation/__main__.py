from typing import Union
from json import loads


def open_config() -> Union[None, dict]:
    try:
        with open("./config.json") as f:
            c = r.read()
        j = loads(c)
        return j
    except FileNotFoundError:
        return None


def setup() -> None:
    pass


def main() -> None:
    config = open_config()
    if config is None:
        return setup()


if __name__ == "__main__":
    main()
