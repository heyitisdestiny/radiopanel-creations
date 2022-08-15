"""
RadioPanel Creations: User Creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A basic wrapper for the Discord API.
Copyright: (c) 2022 Destiny Lumley
Llicense: MIT
"""

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


def print_welcome() -> None:
    print("RadioPanel Creations: User Creation")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def main() -> None:
    print_welcome()
    config = open_config()
    if config is None:
        return setup()


if __name__ == "__main__":
    main()
