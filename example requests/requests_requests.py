# GET /17261/full/max/0/default.jpg. Requests an image with id 17261 with full region, max size, no rotation and default quality in jpg format.

import requests

url = "https://munch.emuseum.com/apis/iiif/image/v2/17261/full/max/0/default.jpg"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /17261/90,0,350,220/max/0/default.jpg. Requests a reqion of an image with ID 17261 with max size, no rotation, default quality and jpg format.

import requests

url = "https://munch.emuseum.com/apis/iiif/image/v2/17261/90,0,350,220/max/0/default.jpg"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /17261/90,0,350,220/max/90/default.jpg. Requests a region of an image with ID 17261 with max size, 90° rotation, default quality and jpg format.

import requests

url = "https://munch.emuseum.com/apis/iiif/image/v2/17261/90,0,350,220/max/90/default.jpg"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /17261/info.json. Requests image information.

import requests

url = "https://munch.emuseum.com/apis/iiif/image/v2/17261/info.json"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
