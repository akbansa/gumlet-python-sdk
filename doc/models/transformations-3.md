
# Transformations 3

## Structure

`Transformations3`

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
| `audio_only` | `bool` | Optional | **Default**: `True` |
| `keep_original` | `bool` | Optional | **Default**: `True` |
| `per_title_encoding` | `bool` | Optional | **Default**: `True` |
| `process_low_resolution_input` | `bool` | Optional | **Default**: `True` |

## Example (as JSON)

```json
{
  "resolution": "240p,360p",
  "format": "hls",
  "thumbnail_format": "png",
  "mp4_access": false,
  "audio_only": false,
  "keep_original": true,
  "per_title_encoding": true,
  "process_low_resolution_input": false,
  "audio_codec": [
    "audio_codec4"
  ],
  "video_codec": [
    "video_codec7",
    "video_codec8",
    "video_codec9"
  ],
  "thumbnail": [
    "thumbnail1",
    "thumbnail2",
    "thumbnail3"
  ]
}
```

