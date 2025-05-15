
# Video Sources Request 1

## Structure

`VideoSourcesRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | video collection name |
| `default_profile_id` | `str` | Optional | Gumlet provides the functionality of creating multiple video assets using the same set of parameters. |
| `temp_cname` | `List[str]` | Optional | cname for channel |
| `insight_property_id` | `str` | Optional | The five to ten character unique identifier of the Gumlet Insight Property available on the dashboard. |
| `player_config` | [`PlayerConfig2`](../../doc/models/player-config-2.md) | Optional | Configure player settings for this playlist, it overrides the setting set on collection. |
| `video_protection` | [`VideoProtection1`](../../doc/models/video-protection-1.md) | Optional | Gumlet provides multiple options for securing your video playback. |
| `channel_settings` | [`ChannelSettings2`](../../doc/models/channel-settings-2.md) | Optional | Configurations to set various channel settings. |
| `mtype` | [`TypeEnum`](../../doc/models/type-enum.md) | Optional | Video collections are top-level entities in Gumlet. You can use them to organize videos for different teams/departments or use cases. |
| `webfolder` | [`Webfolder`](../../doc/models/webfolder.md) | Optional | This is a required field if collection type is webfolder. |
| `aws` | [`Aws1`](../../doc/models/aws-1.md) | Optional | This is a required field if collection type is aws. |
| `proxy` | [`Proxy`](../../doc/models/proxy.md) | Optional | This is a required field if collection type is proxy. |
| `gcs` | [`Gcs`](../../doc/models/gcs.md) | Optional | This is a required field if collection type is gcs. |
| `dostorage` | [`Dostorage`](../../doc/models/dostorage.md) | Optional | This is a required field if collection type is dostorage. |
| `wasabi` | [`Wasabi`](../../doc/models/wasabi.md) | Optional | This is a required field if collection type is wasabi. |
| `linode` | [`Linode`](../../doc/models/linode.md) | Optional | This is a required field if collection type is linode. |
| `backblaze` | [`Backblaze`](../../doc/models/backblaze.md) | Optional | This is a required field if collection type is backblaze. |
| `cloudflare` | [`Cloudflare`](../../doc/models/cloudflare.md) | Optional | This is a required field if collection type is cloudflare. |
| `cloudinary` | [`Cloudinary`](../../doc/models/cloudinary.md) | Optional | This is a required field if collection type is cloudinary. |
| `azure` | [`Azure`](../../doc/models/azure.md) | Optional | This is a required field if collection type is azure. |
| `zoom` | [`Zoom`](../../doc/models/zoom.md) | Optional | This is a required field if collection type is zoom. |

## Example (as JSON)

```json
{
  "name": "name8",
  "default_profile_id": "default_profile_id0",
  "temp_cname": [
    "temp_cname7",
    "temp_cname8"
  ],
  "insight_property_id": "insight_property_id6",
  "player_config": {
    "preload": false,
    "autoplay": false,
    "disable_seek": false,
    "disable_player_controls": false,
    "powered_by_gumlet_overlay": false
  }
}
```

