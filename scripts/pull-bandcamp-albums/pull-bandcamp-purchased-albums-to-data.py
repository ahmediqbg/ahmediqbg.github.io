import html
import json
import time
from pathlib import Path
from pprint import pprint

import requests
import yaml

FAN_ID = 149531
NUM_ALBUMS = 50


def get_output_filepath():
    output_dir = Path("../../_data/bandcamp_urls.yml").resolve()
    file_folder = Path(__file__).parent
    output_dir = Path.joinpath(file_folder, output_dir)
    return output_dir


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


output_dir = get_output_filepath()

print("Outputting to {0}".format(output_dir))

url = 'https://bandcamp.com/api/fancollection/1/collection_items'

data = {"fan_id": FAN_ID,
        "older_than_token": get_older_than_token(),
        "count": NUM_ALBUMS}

print(data)

r = requests.post(url, data=json.dumps(data))

print(r.status_code, r.reason)
responseJSON = (r.json())['items']

# responseJSONsorted = sorted(responseJSON, key=lambda d: d['token'], reverse=True)
# Not necessary as it's already sorted

with open(get_output_filepath(), 'w') as f:
    yaml_data = {'albums': []}

    for albumJSON in responseJSON:
        # html = gen_iframe_html(albumJSON['album_id'], albumJSON['item_url'], albumJSON['album_title'])
        # print(html)
        yaml_data['albums'].append({
            "album": {
                "id": albumJSON['album_id'],
                'item_url': albumJSON['item_url'],
                'title': albumJSON['album_title'],
            }
        })

    yaml.dump(yaml_data, f)
    pprint(yaml_data)

exit(0)
