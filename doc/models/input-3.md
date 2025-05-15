
# Input 3

## Structure

`Input3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transformations` | [`Transformations3`](../../doc/models/transformations-3.md) | Optional | - |
| `source_url` | `str` | Optional | - |
| `size` | `int` | Optional | **Default**: `0` |
| `duration` | `float` | Optional | **Default**: `0` |
| `aspect_ratio` | `str` | Optional | - |
| `fps` | `int` | Optional | **Default**: `0` |
| `width` | `int` | Optional | **Default**: `0` |
| `height` | `int` | Optional | **Default**: `0` |
| `additional_tracks` | [`List[AdditionalTrack1]`](../../doc/models/additional-track-1.md) | Optional | - |

## Example (as JSON)

```json
{
  "source_url": "https://gumlet.sgp1.digitaloceanspaces.com/video/BigBuckBunny.mp4",
  "size": 158008374,
  "duration": 596.473333,
  "aspect_ratio": "16:9",
  "fps": 24,
  "width": 1280,
  "height": 720,
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

