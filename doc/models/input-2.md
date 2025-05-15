
# Input 2

## Structure

`Input2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transformations` | [`Transformations2`](../../doc/models/transformations-2.md) | Optional | - |
| `profile_id` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `chapters` | [`List[Chapter]`](../../doc/models/chapter.md) | Optional | - |
| `source_url` | `str` | Optional | - |
| `size` | `int` | Optional | **Default**: `0` |
| `duration` | `float` | Optional | **Default**: `0` |
| `aspect_ratio` | `str` | Optional | - |
| `fps` | `float` | Optional | **Default**: `0` |
| `width` | `int` | Optional | **Default**: `0` |
| `height` | `int` | Optional | **Default**: `0` |

## Example (as JSON)

```json
{
  "profile_id": "67e4ece9403562dbea65425c",
  "title": " Sample Video",
  "description": "This is a sample video to help you experience Gumlet platform and player.",
  "source_url": "5f462c1561cf8a766464ffc4/647eb18cc90c6c6c35370979/origin-647eb18cc90c6c6c35370979",
  "size": 364735178,
  "duration": 183.088,
  "aspect_ratio": "16:9",
  "fps": 23.98,
  "width": 3840,
  "height": 2160,
  "transformations": {
    "format": "format2",
    "resolution": [
      "resolution7",
      "resolution8"
    ],
    "audio_codec": [
      "audio_codec2"
    ],
    "video_codec": [
      "video_codec1",
      "video_codec2",
      "video_codec3"
    ],
    "image_overlay": {
      "url": "url8",
      "vertical_align": "vertical_align8",
      "horizontal_align": "horizontal_align6",
      "vertical_margin": "vertical_margin2",
      "horizontal_margin": "horizontal_margin8"
    }
  },
  "chapters": [
    {
      "endTime": 28,
      "label": "label2"
    },
    {
      "endTime": 28,
      "label": "label2"
    },
    {
      "endTime": 28,
      "label": "label2"
    }
  ]
}
```

