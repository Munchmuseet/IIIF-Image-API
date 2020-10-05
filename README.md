# Introduction
This documents how to retrieve images from https://emunch.emuseum.no using the IIIF Image and Presentation APIs. The base URI (`{scheme}://{server}{/prefix}/{identifier}`) for the API is `https://munch.emuseum.com/apis/iiif/image/v2/{identifier}`. The identifier is the media ID. The media ID can be found in an image's URL. This URL can be requested from the eMuseum API using something like this: `GET https://munch.emuseum.com/objects/json?mediaExistence=True&key={key}`. In the response look for `primaryMedia`:

```
"primaryMedia": {
	"value": "/internal/media/dispatcher/7483/resize%25253Aformat%25253Dthumbnail;jsessionid=54EDD47D73197613988875184D91DAC7"
}
```
The media ID is the number after ```dispatcher/```.

See also: https://documenter.getpostman.com/view/2789837/S1ZucW54

# Image request URI syntax
The syntax for requesting an image is ```{scheme}://{server}{/prefix}/{identifier}/{region}/{size}/{rotation}/{quality}.{format}```.

# Image information request URI syntax
The syntax for requesting information about an image is ```{scheme}://{server}{/prefix}/{identifier}/info.json```.

# Image request parameters
## Region
The region parameter defines the rectangular portion of the full image to be returned. Region can be specified by pixel coordinates, percentage or by the value “full”, which specifies that the entire image should be returned.

| Form | Description |
| --- | --- |
| full | The complete image is returned, without any cropping. |
| square | The region is defined as an area where the width and height are both equal to the length of the shorter dimension of the complete image. The region may be positioned anywhere in the longer dimension of the image content at the server’s discretion, and centered is often a reasonable default. |
| x,y,w,h | The region of the full image to be returned is specified in terms of absolute pixel values. The value of x represents the number of pixels from the 0 position on the horizontal axis. The value of y represents the number of pixels from the 0 position on the vertical axis. Thus the x,y position 0,0 is the upper left-most pixel of the image. w represents the width of the region and h represents the height of the region in pixels.
| pct:x,y,w,h | The region to be returned is specified as a sequence of percentages of the full image’s dimensions, as reported in the image information document. Thus, x represents the number of pixels from the 0 position on the horizontal axis, calculated as a percentage of the reported width. w represents the width of the region, also calculated as a percentage of the reported width. The same applies to y and h respectively. These may be floating point numbers. |

The ```square``` form is not implemented in this API.

## Size
The size parameter determines the dimensions to which the extracted region is to be scaled.

| Form | Description |
| --- | --- |
| full | The image or region is not scaled, and is returned at its full size. Note [deprecation warning][1] |
| max | The image or region is returned at the maximum size available, as indicated by maxWidth, maxHeight, maxArea in the profile description. This is the same as full if none of these properties are provided. |
| w, | The image or region should be scaled so that its width is exactly equal to w, and the height will be a calculated value that maintains the aspect ratio of the extracted region. |
| ,h | The image or region should be scaled so that its height is exactly equal to h, and the width will be a calculated value that maintains the aspect ratio of the extracted region. |
| pct:n | The width and height of the returned image is scaled to n% of the width and height of the extracted region. The aspect ratio of the returned image is the same as that of the extracted region. |
| w,h | The width and height of the returned image are exactly w and h. The aspect ratio of the returned image may be different than the extracted region, resulting in a distorted image. |
| !w,h | The image content is scaled for the best fit such that the resulting width and height are less than or equal to the requested width and height. The exact scaling may be determined by the service provider, based on characteristics including image quality and system performance. The dimensions of the returned image content are calculated to maintain the aspect ratio of the extracted region. |

## Rotation
The rotation parameter specifies mirroring and rotation. A leading exclamation mark (“!”) indicates that the image should be mirrored by reflection on the vertical axis before any rotation is applied. The numerical value represents the number of degrees of clockwise rotation, and may be any floating point number from 0 to 360.

| Form | Description |
| --- | --- |
| n | The degrees of clockwise rotation from 0 up to 360. |
| !n | The image should be mirrored and then rotated as above. |

This API only allows the values ```0```, ```90```, ```180```, ```270``` and ```360```. Mirroring is not implemented.

## Quality
The quality parameter determines whether the image is delivered in color, grayscale or black and white.

| Quality | Parameter Returned |
| --- | --- |
| color | The image is returned in full color. |
| gray | The image is returned in grayscale, where each pixel is black, white or any shade of gray in between. |
| bitonal | The image returned is bitonal, where each pixel is either black or white. |
| default | The image is returned using the server’s default quality (e.g. color, gray or bitonal) for the image. |

## Format
The format of the returned image is expressed as an extension at the end of the URI.

| Extension | MIME Type |
| --- | --- |
| jpg | image/jpeg |
| tif | image/tiff |
| png | image/png |
| gif | image/gif |
| jp2 | image/jp2 |
| pdf | application/pdf |
| webp | image/webp |

Only ```jpg```and ```png```are implemented. All other values are invalid.

# Full documentation
See [IIIF Image API 2.1.1][2] and [IIIF Presentation API 2.1.1][3] for full documentation.

[1]: https://iiif.io/api/image/2.1/#full-dep "Deprecation Warning"
[2]: https://iiif.io/api/image/2.1/ "IIIF Image API"
[3]: https://iiif.io/api/presentation/2.1/ "IIIF Presentation API"
