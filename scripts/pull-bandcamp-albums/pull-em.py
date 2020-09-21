import requests

output_dir = "../../_data/bandcamp_urls.yml"

url = 'https://bandcamp.com/api/fancollection/1/collection_items'

data = {"fan_id": 149531,
        "older_than_token": "1590788900:576974541:a::",
        "count": 20}

print(data)

r = requests.post("http://bugs.python.org", data={'number': 12524, 'type': 'issue', 'action': 'show'})

print(r.status_code, r.reason)
print(r.text[:300] + '...')
