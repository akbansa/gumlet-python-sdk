
# Video Sources Request

## Structure

`VideoSourcesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Specify a text string or identifier for the collection. |
| `mtype` | [`TypeEnum`](../../doc/models/type-enum.md) | Required | Video collections are top-level entities in Gumlet. You can use them to organize videos for different teams/departments or use cases.<br><br>**Default**: `'direct-upload'` |
| `default_profile_id` | `str` | Optional | Gumlet provides the functionality of creating multiple video assets using the same set of parameters. |
| `insight_property_id` | `str` | Optional | The five to ten character unique identifier of the Gumlet Insight Property available on the dashboard. |
| `video_protection` | [`VideoProtection1`](../../doc/models/video-protection-1.md) | Optional | Gumlet provides multiple options for securing your video playback. |
| `aws` | [`Aws1`](../../doc/models/aws-1.md) | Optional | This is a required field if collection type is aws. |
| `proxy` | [`Proxy`](../../doc/models/proxy.md) | Optional | This is a required field if collection type is proxy. |
| `gcs` | [`Gcs`](../../doc/models/gcs.md) | Optional | This is a required field if collection type is gcs. |
| `dostorage` | [`Dostorage`](../../doc/models/dostorage.md) | Optional | This is a required field if collection type is dostorage. |
| `wasabi` | [`Wasabi`](../../doc/models/wasabi.md) | Optional | This is a required field if collection type is wasabi. |
| `cloudinary` | [`Cloudinary`](../../doc/models/cloudinary.md) | Optional | This is a required field if collection type is cloudinary. |
| `azure` | [`Azure`](../../doc/models/azure.md) | Optional | This is a required field if collection type is azure. |
| `linode` | [`Linode`](../../doc/models/linode.md) | Optional | This is a required field if collection type is linode. |
| `backblaze` | [`Backblaze`](../../doc/models/backblaze.md) | Optional | This is a required field if collection type is backblaze. |
| `cloudflare` | [`Cloudflare`](../../doc/models/cloudflare.md) | Optional | This is a required field if collection type is cloudflare. |
| `zoom` | [`Zoom`](../../doc/models/zoom.md) | Optional | This is a required field if collection type is zoom. |

## Example (as JSON)

```json
{
  "name": "name4",
  "type": "direct-upload",
  "default_profile_id": "default_profile_id6",
  "insight_property_id": "insight_property_id2",
  "video_protection": {
    "signed_url": false,
    "signed_url_secret": "signed_url_secret0",
    "blacklisted_countries": [
      "blacklisted_countries1"
    ],
    "whitelisted_referrers": "whitelisted_referrers2"
  },
  "aws": {
    "bucket_name": "bucket_name6",
    "bucket_region": "bucket_region6",
    "access_key": "access_key0",
    "secret": "secret8",
    "base_path": "base_path4",
    "endpoint": "endpoint0"
  },
  "proxy": {
    "whitelisted_domains": "whitelisted_domains4"
  }
}
```

