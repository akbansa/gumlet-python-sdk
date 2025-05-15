
# Transformations 6

## Structure

`Transformations6`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `resolution` | `str` | Optional | - |
| `format` | `str` | Optional | - |
| `audio_codec` | `List[str]` | Optional | - |
| `video_codec` | `List[str]` | Optional | - |
| `thumbnail` | `List[str]` | Optional | - |
| `thumbnail_format` | `str` | Optional | - |
| `mp_4_access` | `bool` | Optional | **Default**: `True` |
| `per_title_encoding` | `bool` | Optional | **Default**: `True` |

## Example (as JSON)

```json
{
  "resolution": "240p,360p",
  "format": "hls",
  "thumbnail_format": "png",
  "mp4_access": false,
  "per_title_encoding": true,
  "audio_codec": [
    "audio_codec0",
    "audio_codec1"
  ],
  "video_codec": [
    "video_codec3"
  ],
  "thumbnail": [
    "thumbnail7"
  ]
}
```

