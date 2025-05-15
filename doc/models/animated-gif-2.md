
# Animated Gif 2

Create an animated GIF from a video.

## Structure

`AnimatedGif2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_offset` | `str` | Optional | The time (in seconds or `HH:MM:SS` format) of the video timeline where the animated gif should begin. **Default: `0`** |
| `end_offset` | `str` | Optional | The time (in seconds or `HH:MM:SS` format) of the video timeline where the GIF ends. Defaults to `10` seconds after the start_offset. Maximum duration of GIF is limited to `10` seconds. |
| `width` | `str` | Optional | The width in pixels (or in percentage value of asset width) of the animated GIF. Max width is `640px`. |
| `height` | `str` | Optional | The height in pixels (or in percentage value of asset height) of the animated GIF. Max height is `640px`. |
| `fps` | `str` | Optional | The frame rate of the generated GIF. Defaults to `15` fps. Max `30` fps. |

## Example (as JSON)

```json
{
  "start_offset": "start_offset8",
  "end_offset": "end_offset8",
  "width": "width2",
  "height": "height4",
  "fps": "fps0"
}
```

