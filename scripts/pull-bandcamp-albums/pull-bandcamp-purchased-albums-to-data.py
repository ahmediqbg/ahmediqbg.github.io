from pathlib import Path
from pprint import pprint

import yaml

import bandcampUtils


def get_output_filepath():
    return Path.joinpath(bandcampUtils.get_data_folder(), "bandcamp_purchased_albums.yml")

print("Outputting to {0}".format(get_output_filepath()))

responseJSON = bandcampUtils.get_top_purchased_albums_json(50)

with open(get_output_filepath(), 'w') as f:
    yaml_list = []

    for albumJSON in responseJSON:
        # html = gen_iframe_html(albumJSON['album_id'], albumJSON['item_url'], albumJSON['album_title'])
        # print(html)
        yaml_list.append({
            "id": albumJSON['album_id'],
            'item_url': albumJSON['item_url'],
            'title': albumJSON['album_title'],
        })

    yaml.dump(yaml_list, f)
    pprint(yaml_list[0:5])
