
# Image Overlay

Image overlay can be used to brand a video or add a visual label in the form of an image.

## Structure

`ImageOverlay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Required | This is the required parameter for image overlay, it can be a URL to an image that needs to be overlayed. |
| `horizontal_margin` | `str` | Optional | This parameter defines the horizontal coordinate value of the corner (determined by `horizontal_align`) of the overlay area. Values can be an absolute number of pixels or a percentage value relative to the video width. **Default: `0`** |
| `vertical_margin` | `str` | Optional | This parameter defines the vertical coordinate value of the corner (determined by `vertical_align`) of the overlay area. Values can be an absolute number of pixels or a percentage value relative to the video height. **Default: `0`** |
| `horizontal_align` | `str` | Optional | This parameter specifies the horizontal alignment of the overlayed image and can be either `left` or `right`. **Default: `right`** |
| `vertical_align` | `str` | Optional | This parameter specifies the vertical alignment of the overlayed image and can be either `top` or `bottom`. **Default: `bottom`** |
| `width` | `str` | Optional | Width of the overlayed image. **Default: `image width`** |
| `height` | `str` | Optional | Height of the overlayed image. **Default: `image height`** |

## Example (as JSON)

```json
{
  "url": "url8",
  "horizontal_margin": "horizontal_margin8",
  "vertical_margin": "vertical_margin2",
  "horizontal_align": "horizontal_align4",
  "vertical_align": "vertical_align8",
  "width": "width2"
}
```

