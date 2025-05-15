
# Input 1

## Structure

`Input1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transformations` | [`Transformations1`](../../doc/models/transformations-1.md) | Optional | - |
| `profile_id` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `metadata` | [`Metadata`](../../doc/models/metadata.md) | Optional | - |
| `source_url` | `str` | Optional | - |
| `call_to_actions` | [`List[CallToAction3]`](../../doc/models/call-to-action-3.md) | Optional | - |

## Example (as JSON)

```json
{
  "profile_id": "646df1c9173a4a2fcac180b7",
  "title": "Sports.",
  "description": "This video provides information about various sports.",
  "source_url": "646df1c9173a4a2fcac180b4/65b169dfe99b77f116c0e4aa/origin-65b169dfe99b77f116c0e4aa",
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

