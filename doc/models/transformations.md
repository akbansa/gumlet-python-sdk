
# Transformations

## Structure

`Transformations`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `format` | `str` | Optional | - |
| `resolution` | `List[str]` | Optional | - |
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
  "per_title_encoding": false,
  "resolution": [
    "resolution5"
  ],
  "audio_codec": [
    "audio_codec4",
    "audio_codec3",
    "audio_codec2"
  ],
  "video_codec": [
    "video_codec9",
    "video_codec0"
  ],
  "thumbnail": [
    "thumbnail3",
    "thumbnail4"
  ]
}
```

