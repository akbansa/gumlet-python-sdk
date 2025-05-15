
# Transformations 2

## Structure

`Transformations2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `format` | `str` | Optional | - |
| `resolution` | `List[str]` | Optional | - |
| `audio_codec` | `List[str]` | Optional | - |
| `video_codec` | `List[str]` | Optional | - |
| `image_overlay` | [`ImageOverlay2`](../../doc/models/image-overlay-2.md) | Optional | - |
| `thumbnail` | `List[str]` | Optional | - |
| `thumbnail_format` | `str` | Optional | - |
| `mp_4_access` | `bool` | Optional | **Default**: `True` |
| `audio_only` | `bool` | Optional | **Default**: `True` |
| `original_deleted` | `bool` | Optional | **Default**: `True` |
| `per_title_encoding` | `bool` | Optional | **Default**: `True` |
| `generate_subtitles` | [`GenerateSubtitles2`](../../doc/models/generate-subtitles-2.md) | Optional | - |
| `preview_thumbnails` | [`PreviewThumbnails`](../../doc/models/preview-thumbnails.md) | Optional | - |

## Example (as JSON)

```json
{
  "format": "abr",
  "thumbnail_format": "png",
  "mp4_access": false,
  "audio_only": false,
  "original_deleted": true,
  "per_title_encoding": false,
  "resolution": [
    "resolution3",
    "resolution4"
  ],
  "audio_codec": [
    "audio_codec4"
  ],
  "video_codec": [
    "video_codec7",
    "video_codec8",
    "video_codec9"
  ],
  "image_overlay": {
    "url": "url8",
    "vertical_align": "vertical_align8",
    "horizontal_align": "horizontal_align6",
    "vertical_margin": "vertical_margin2",
    "horizontal_margin": "horizontal_margin8"
  }
}
```

