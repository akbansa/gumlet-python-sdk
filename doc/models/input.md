
# Input

## Structure

`Input`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transformations` | [`Transformations`](../../doc/models/transformations.md) | Optional | - |
| `profile_id` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `metadata` | [`Metadata`](../../doc/models/metadata.md) | Optional | - |
| `source_url` | `str` | Optional | - |
| `call_to_actions` | [`List[CallToAction1]`](../../doc/models/call-to-action-1.md) | Optional | - |

## Example (as JSON)

```json
{
  "profile_id": "646df1c9173a4a2fcac180b7",
  "title": "bipbopall",
  "description": "some description",
  "source_url": "http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8",
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
    "thumbnail": [
      "thumbnail5",
      "thumbnail6",
      "thumbnail7"
    ]
  },
  "metadata": {
    "headermeta": "headermeta0"
  }
}
```

