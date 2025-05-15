
# Video Sources Response 1

## Structure

`VideoSourcesResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `mtype` | `str` | Optional | - |
| `created_at` | `str` | Optional | - |
| `updated_at` | `str` | Optional | - |
| `video_protection` | `Any` | Optional | - |
| `player_config` | [`PlayerConfig`](../../doc/models/player-config.md) | Optional | - |
| `default_profile_id` | `str` | Optional | - |
| `insight_property_id` | `str` | Optional | - |
| `zoom` | [`Zoom1`](../../doc/models/zoom-1.md) | Optional | - |
| `embed_details` | [`EmbedDetails1`](../../doc/models/embed-details-1.md) | Optional | - |
| `folders` | `List[Any]` | Optional | - |
| `channel_settings` | [`ChannelSettings1`](../../doc/models/channel-settings-1.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "65b01610e99b77f116c0e32b",
  "name": "zoom-collection",
  "type": "zoom",
  "created_at": "01/23/2024 19:40:00",
  "updated_at": "01/23/2024 19:40:00",
  "default_profile_id": "646df1c9173a4a2fcac180b7",
  "insight_property_id": "65b01610e99b77f116c0e329"
}
```

