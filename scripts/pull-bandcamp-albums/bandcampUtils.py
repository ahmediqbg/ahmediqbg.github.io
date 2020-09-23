import html
import json
import time
from pathlib import Path
from pprint import pprint
from typing import Dict, Union

import requests
import yaml

FAN_ID = 149531  # HenryFBP
COLLECTION_URL = 'https://bandcamp.com/api/fancollection/1/collection_items'
WISHLIST_URL = 'https://bandcamp.com/api/fancollection/1/wishlist_items'


def get_data_folder():
    output_dir = Path("../../_data/").resolve()
    file_folder = Path(__file__).parent
    return Path.joinpath(file_folder, output_dir)


print(get_data_folder())


def gen_iframe_html(albumid, albumurl, albumname):
    albumid = html.escape(str(albumid))
    albumurl = html.escape(albumurl)
    albumname = html.escape(albumname)

    return f'''<iframe style="border: 0; width: 100%; height: 42px;" src="https://bandcamp.com/EmbeddedPlayer/album={albumid}/size=small/bgcol=ffffff/linkcol=0687f5/transparent=true/" seamless><a href="{albumurl}">{albumname}</a></iframe>'''


def get_older_than_token():
    """
    :return: Token representing when to search from. Token will be most recent unix epoch from NOW.
    """
    curr_epoch = str(time.time())
    lpar, rpar = curr_epoch.split('.')
    return "{}:{}:a::".format(lpar, rpar)


def get_top_wishlisted_albums_json(count, fan_id=FAN_ID, older_than_token=get_older_than_token()) -> Dict:
    data = {"fan_id": fan_id,
            "older_than_token": older_than_token,
            "count": count}

    r = requests.post(WISHLIST_URL, data=json.dumps(data))

    return r.json()['items']


def get_top_purchased_albums_json(count, fan_id=FAN_ID, older_than_token=get_older_than_token()) -> Dict:
    data = {"fan_id": fan_id,
            "older_than_token": older_than_token,
            "count": count}

    r = requests.post(COLLECTION_URL, data=json.dumps(data))

    return r.json()['items']


def save_json_object_to_yaml(obj: Union[Dict, list], filepath: str):
    with open(filepath, 'w') as f:
        yaml.dump(obj, f)
