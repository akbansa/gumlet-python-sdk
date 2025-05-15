
# Image Sources Request 1

## Structure

`ImageSourcesRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type3Enum`](../../doc/models/type-3-enum.md) | Optional | - |
| `webfolder` | [`Webfolder1`](../../doc/models/webfolder-1.md) | Optional | This is a required field if source type is webfolder. |
| `aws` | [`Aws4`](../../doc/models/aws-4.md) | Optional | This is a required field if source type is aws. |
| `proxy` | [`Proxy2`](../../doc/models/proxy-2.md) | Optional | This is a required field if source type is proxy. |
| `gcs` | [`Gcs2`](../../doc/models/gcs-2.md) | Optional | This is a required field if source type is gcs. |
| `dostorage` | [`Dostorage2`](../../doc/models/dostorage-2.md) | Optional | This is a required field if source type is dostorage. |
| `wasabi` | [`Wasabi2`](../../doc/models/wasabi-2.md) | Optional | This is a required field if source type is wasabi. |
| `linode` | [`Linode2`](../../doc/models/linode-2.md) | Optional | This is a required field if source type is linode. |
| `backblaze` | [`Backblaze2`](../../doc/models/backblaze-2.md) | Optional | This is a required field if source type is backblaze. |
| `cloudflare` | [`Cloudflare2`](../../doc/models/cloudflare-2.md) | Optional | This is a required field if source type is cloudflare. |
| `cloudinary` | [`Cloudinary2`](../../doc/models/cloudinary-2.md) | Optional | This is a required field if source type is cloudinary. |
| `azure` | [`Azure2`](../../doc/models/azure-2.md) | Optional | This is a required field if source type is azure. |

## Example (as JSON)

```json
{
  "type": "azure",
  "webfolder": {
    "base_url": "base_url0"
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
  },
  "gcs": {
    "bucket_name": "bucket_name4",
    "service_account_key": "service_account_key6"
  }
}
```

