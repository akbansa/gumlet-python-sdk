
# Storage Details

## Structure

`StorageDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `video` | [`List[Video]`](../../doc/models/video.md) | Optional | - |
| `audio` | [`List[Audio]`](../../doc/models/audio.md) | Optional | - |
| `playlist` | [`List[Playlist]`](../../doc/models/playlist.md) | Optional | - |
| `thumbnail` | [`List[Thumbnail]`](../../doc/models/thumbnail.md) | Optional | - |
| `subtitle` | [`List[Subtitle]`](../../doc/models/subtitle.md) | Optional | - |
| `preview_thumbnail` | [`List[PreviewThumbnail]`](../../doc/models/preview-thumbnail.md) | Optional | - |

## Example (as JSON)

```json
{
  "video": [
    {
      "fileName": "fileName0",
      "size": 142,
      "resolution": "resolution0",
      "duration": 244
    }
  ],
  "audio": [
    {
      "fileName": "fileName2",
      "size": 92,
      "duration": 38
    }
  ],
  "playlist": [
    {
      "fileName": "fileName0",
      "size": 182
    },
    {
      "fileName": "fileName0",
      "size": 182
    },
    {
      "fileName": "fileName0",
      "size": 182
    }
  ],
  "thumbnail": [
    {
      "fileName": "fileName0",
      "size": 232,
      "resolution": "resolution0"
    },
    {
      "fileName": "fileName0",
      "size": 232,
      "resolution": "resolution0"
    },
    {
      "fileName": "fileName0",
      "size": 232,
      "resolution": "resolution0"
    }
  ],
  "subtitle": [
    {
      "fileName": "fileName0",
      "size": 40
    },
    {
      "fileName": "fileName0",
      "size": 40
    }
  ]
}
```

