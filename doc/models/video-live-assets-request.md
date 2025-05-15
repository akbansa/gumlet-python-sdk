
# Video Live Assets Request

## Structure

`VideoLiveAssetsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `live_source_id` | `str` | Required | Gumlet live video source/collection id. |
| `resolution` | `str` | Required | Required resolutions in HLS delivery format for live stream. Can be an array of string out of the following values:  `240p`, `360p`, `480p`, `540p`, `720p`, and `1080p`. Re-sized rendition will retain the input aspect ratio. |
| `title` | `str` | Optional | Your live stream asset title |
| `mp_4_access` | `bool` | Optional | Creates <code>MP4</code> version for download purpose. |

## Example (as JSON)

```json
{
  "live_source_id": "live_source_id2",
  "resolution": "resolution6",
  "title": "title8",
  "mp4_access": false
}
```

