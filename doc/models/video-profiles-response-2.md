
# Video Profiles Response 2

## Structure

`VideoProfilesResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `profile_id` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `transformations` | [`Transformations6`](../../doc/models/transformations-6.md) | Optional | - |
| `created_at` | `int` | Optional | **Default**: `0` |
| `updated_at` | `int` | Optional | **Default**: `0` |

## Example (as JSON)

```json
{
  "profile_id": "61921fb10822a81d955d1730",
  "name": "Gumlet-Profile-2",
  "created_at": 1636966321742,
  "updated_at": 1636975593082,
  "transformations": {
    "resolution": "resolution0",
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
    ]
  }
}
```

