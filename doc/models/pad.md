
# Pad

This transformation can be used to add padding to the video.

## Structure

`Pad`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `top` | `str` | Optional | Width of padding on the top side. Values can be an absolute number of pixels or a percentage value relative to the video height. **Default: `%5`** |
| `left` | `str` | Optional | Width of padding on the left side. Values can be an absolute number of pixels or a percentage value relative to the video width. **Default: `0`** |
| `bottom` | `str` | Optional | Width of padding on the bottom side. Values can be an absolute number of pixels or a percentage value relative to the video height. **Default: `%5`** |
| `right` | `str` | Optional | Width of padding on the right side. Values can be an absolute number of pixels or a percentage value relative to the video width. **Default: `0`** |
| `color` | `str` | Optional | Color of padding area. **Default: `black`** |

## Example (as JSON)

```json
{
  "top": "top6",
  "left": "left4",
  "bottom": "bottom6",
  "right": "right4",
  "color": "color2"
}
```

