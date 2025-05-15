
# Transformations 1

## Structure

`Transformations1`

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
| `original_deleted` | `bool` | Optional | **Default**: `True` |

## Example (as JSON)

```json
{
  "format": "hls",
  "thumbnail_format": "png",
  "mp4_access": false,
  "per_title_encoding": false,
  "original_deleted": true,
  "resolution": [
    "resolution9",
    "resolution0"
  ],
  "audio_codec": [
    "audio_codec0"
  ],
  "video_codec": [
    "video_codec3",
    "video_codec4",
    "video_codec5"
  ],
  "thumbnail": [
    "thumbnail7",
    "thumbnail8",
    "thumbnail9"
  ]
}
```

