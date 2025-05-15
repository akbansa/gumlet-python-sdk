
# Transformations 4

## Structure

`Transformations4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
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
  "format": "hls",
  "thumbnail_format": "png",
  "mp4_access": false,
  "per_title_encoding": true,
  "audio_codec": [
    "audio_codec0",
    "audio_codec1",
    "audio_codec2"
  ],
  "video_codec": [
    "video_codec3",
    "video_codec4"
  ],
  "thumbnail": [
    "thumbnail7",
    "thumbnail8"
  ]
}
```

