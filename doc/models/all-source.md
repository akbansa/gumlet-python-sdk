
# All Source

## Structure

`AllSource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `mtype` | `str` | Optional | - |
| `created_at` | `str` | Optional | - |
| `updated_at` | `str` | Optional | - |
| `video_protection` | [`VideoProtection`](../../doc/models/video-protection.md) | Optional | - |
| `player_config` | [`PlayerConfig`](../../doc/models/player-config.md) | Optional | - |
| `default_profile_id` | `str` | Optional | - |
| `insight_property_id` | `str` | Optional | - |
| `aws` | [`Aws`](../../doc/models/aws.md) | Optional | - |
| `embed_details` | [`EmbedDetails`](../../doc/models/embed-details.md) | Optional | - |
| `folders` | `List[str]` | Optional | - |
| `channel_settings` | [`ChannelSettings`](../../doc/models/channel-settings.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "646df1c9173a4a2fcac180b4",
  "name": "collection_name",
  "type": "aws",
  "created_at": "05/24/2023 11:15:21",
  "updated_at": "01/24/2024 11:57:48",
  "default_profile_id": "646df1c9173a4a2fcac180b7",
  "insight_property_id": "646df0aa173a4a2fcac18009"
}
```

