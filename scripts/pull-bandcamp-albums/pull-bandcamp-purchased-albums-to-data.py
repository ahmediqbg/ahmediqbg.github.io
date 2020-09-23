from pathlib import Path
from pprint import pprint

import yaml

import bandcampUtils


def get_output_filepath():
    output_dir = Path("../../_data/bandcamp_purchased_albums.yml").resolve()
    file_folder = Path(__file__).parent
    return Path.joinpath(file_folder, output_dir)


output_dir = get_output_filepath()

print("Outputting to {0}".format(output_dir))

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
