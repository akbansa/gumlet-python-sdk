
# All Profile

## Structure

`AllProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `profile_id` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `transformations` | [`Transformations4`](../../doc/models/transformations-4.md) | Optional | - |
| `created_at` | `int` | Optional | **Default**: `0` |
| `updated_at` | `int` | Optional | **Default**: `0` |

## Example (as JSON)

```json
{
  "profile_id": "61921fb10822a81d955d1730",
  "name": "Gumlet-Profile-1",
  "created_at": 1636966321742,
  "updated_at": 1636966321742,
  "transformations": {
    "format": "format2",
    "audio_codec": [
      "audio_codec2"
    ],
    "video_codec": [
      "video_codec1",
      "video_codec2",
      "video_codec3"
    ],
    "thumbnail": [
      "thumbnail5",
      "thumbnail6",
      "thumbnail7"
    ],
    "thumbnail_format": "thumbnail_format8"
  }
}
```

