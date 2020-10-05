# GET /17261/full/max/0/default.jpg. Requests an image with id 17261 with full region, max size, no rotation and default quality in jpg format.

import http.client
import mimetypes
conn = http.client.HTTPSConnection("munch.emuseum.com")
payload = ''
headers = {}
conn.request("GET", "/apis/iiif/image/v2/17261/full/max/0/default.jpg", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /17261/90,0,350,220/max/0/default.jpg. Requests a reqion of an image with ID 17261 with max size, no rotation, default quality and jpg format.

import http.client
import mimetypes
conn = http.client.HTTPSConnection("munch.emuseum.com")
payload = ''
headers = {}
conn.request("GET", "/apis/iiif/image/v2/17261/90,0,350,220/max/0/default.jpg", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /17261/90,0,350,220/max/90/default.jpg. Requests a region of an image with ID 17261 with max size, 90° rotation, default quality and jpg format.

import http.client
import mimetypes
conn = http.client.HTTPSConnection("munch.emuseum.com")
payload = ''
headers = {}
conn.request("GET", "/apis/iiif/image/v2/17261/90,0,350,220/max/90/default.jpg", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /17261/info.json. Requests image information.

import http.client
import mimetypes
conn = http.client.HTTPSConnection("munch.emuseum.com")
payload = ''
headers = {}
conn.request("GET", "/apis/iiif/image/v2/17261/info.json", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
