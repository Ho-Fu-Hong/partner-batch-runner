import json
from pathlib import Path

import requests

CONFIG = json.loads((Path(__file__).resolve().parents[1] / "config" / "runner.json").read_text())


def post_settlement(files):
    api = CONFIG["Settlement"]
    response = requests.post(api["BaseUrl"] + "/settlements", json={"files": files},
                             auth=(api["ClientId"], api["ClientSecret"]), timeout=30)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(post_settlement([]))
