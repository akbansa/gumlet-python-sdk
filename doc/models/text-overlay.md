
# Text Overlay

Text overlay can be used to brand a video or add a label in the form of text.

## Structure

`TextOverlay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Required | Text to be overlayed on video. |
| `horizontal_align` | `str` | Optional | This parameter specifies the horizontal alignment of the overlayed image and can be either `left` or `right`. **Default: `right`** |
| `vertical_align` | `str` | Optional | This parameter specifies the vertical alignment of the overlayed image and can be either `top` or `bottom`. **Default: `bottom`** |
| `horizontal_margin` | `str` | Optional | This parameter defines the horizontal coordinate value of the corner (determined by `horizontal_align`) of the overlay area. Values can be an absolute number of pixels relative to the video width. **Default: `0`** |
| `vertical_margin` | `str` | Optional | This parameter defines the vertical coordinate value of the corner (determined by vertical_align) of the overlay area. Values can be an absolute number of pixels relative to the video height. **Default: `0`** |
| `color` | `str` | Optional | Font color for text. **Default: `black`** |
| `font` | `str` | Optional | Font family type for text. **Default: `sans`** |
| `font_size` | `str` | Optional | Font size in pixels. **Default: `16`** |
| `opacity` | `str` | Optional | Overlay text opacity can be specified with opacity parameter where value can be between `0` and `100` where `0` is considered completely transparent and `100` is considered completely opaque. **Default: `100`** |
| `box` | `bool` | Optional | This parameter allows rectangular drawing a box over the overlayed text. **Default: `false`** |
| `box_color` | `str` | Optional | Box color can be specified with this parameter. **Default: `white`** |
| `box_opacity` | `str` | Optional | Box opacity can be specified with this parameter. **Default: `100`** |
| `box_border` | `str` | Optional | Padding between the box border and the text can be specified with this parameter in pixels. **Default: `0`** |

## Example (as JSON)

```json
{
  "text": "text2",
  "horizontal_align": "horizontal_align2",
  "vertical_align": "vertical_align0",
  "horizontal_margin": "horizontal_margin0",
  "vertical_margin": "vertical_margin0",
  "color": "color6"
}
```

