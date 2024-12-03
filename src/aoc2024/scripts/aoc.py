import argparse
import sys
from http import HTTPStatus
from pathlib import Path

import requests

COOKIE_PATH = Path("session.txt")
INPUT_DIR = Path("input")
ENDPOINT_PATTERN = "https://adventofcode.com/2024/day/{}/input"


def main():
    arguments = handle_arguments()

    match arguments.command:
        case "download":
            download_input(arguments.day)


def download_input(day: int):
    input_path = INPUT_DIR / f"input_{day:02}.txt"

    if input_path.exists():
        sys.exit(f"Input data for day {day} already downloaded.")

    cookie = COOKIE_PATH.read_text().strip()
    cookies = {"session": cookie}
    url = ENDPOINT_PATTERN.format(day)
    response = requests.get(url, cookies=cookies)
    if response.status_code == HTTPStatus.OK:
        INPUT_DIR.mkdir(exist_ok=True)
        print(f"Writing '{input_path}'")
        input_path.write_text(response.text)
    else:
        sys.exit(f"Failed to download input for day {day}:\n{response.text}")


def handle_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title="Commands", dest="command")
    subparsers.required = True

    download_parser = subparsers.add_parser("download", help="Download input.")
    download_parser.add_argument("day", type=int)

    return parser.parse_args()


if __name__ == "__main__":
    main()
