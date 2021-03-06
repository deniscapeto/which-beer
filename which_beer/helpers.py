# Standard Library
import csv
import json
import os

import requests


def url_base() -> str:
    url = "https://api.punkapi.com/v2/beers"
    return url


def get_file_path() -> str:
    root_dir = os.getcwd()
    file_dir = root_dir + "/files/"
    return file_dir


def format_json(response: requests.models.Response) -> str:
    parsed = json.loads(response.text)
    beer = json.dumps(parsed, indent=2)
    return beer


def create_json_file(
    file_name: str, response: requests.models.Response
) -> None:  # noqa
    with open(file_name, "w") as outfile:
        json.dump(response.json(), outfile, indent=2)


def create_csv_file(
    file_name: str, response: requests.models.Response
) -> None:  # noqa
    with open(file_name, "w") as outfile:
        csv_writer = csv.writer(outfile)
        count = 0

        for beer in response.json():
            if count == 0:
                header = beer.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(beer.values())
