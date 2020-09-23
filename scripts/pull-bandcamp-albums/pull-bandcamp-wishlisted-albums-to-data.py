from pathlib import Path
from pprint import pprint

import bandcampUtils


def get_output_filepath():
    return Path.joinpath(bandcampUtils.get_data_folder(), "bandcamp_wishlisted_albums.yml")


if __name__ == '__main__':
    print("Outputting to {0}".format(get_output_filepath()))

    responseJSON = bandcampUtils.get_top_wishlisted_albums_json()

    yaml_list = []

    for albumJSON in responseJSON:
        # html = gen_iframe_html(albumJSON['album_id'], albumJSON['item_url'], albumJSON['album_title'])
        # print(html)
        yaml_list.append({
            "id": albumJSON['album_id'],
            'item_url': albumJSON['item_url'],
            'title': albumJSON['album_title'],
        })

    pprint(yaml_list[0:5])

    bandcampUtils.save_json_object_to_yaml(yaml_list, get_output_filepath())
