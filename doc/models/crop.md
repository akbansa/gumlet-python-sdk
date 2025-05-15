
# Crop

This transformation can be used to crop the video by defining a rectangular area within the dimensions of the output video.

## Structure

`Crop`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `horizontal_margin` | `str` | Optional | This parameter defines the horizontal coordinate value of the upper-left corner of the cropping area. Values can be an absolute number of pixels or a percentage value relative to the video width. **Default: `0`** |
| `vertical_margin` | `str` | Optional | This parameter defines the vertical coordinate value of the upper-left corner of the cropping area. Values can be an absolute number of pixels or a percentage value relative to the video height. **Default: `0`** |
| `width` | `str` | Required | Width of the cropping area in pixels. |
| `height` | `str` | Required | Height of the cropping area in pixels. |

## Example (as JSON)

```json
{
  "horizontal_margin": "horizontal_margin6",
  "vertical_margin": "vertical_margin6",
  "width": "width2",
  "height": "height4"
}
```

