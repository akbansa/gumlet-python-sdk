
# Channel Settings

## Structure

`ChannelSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Optional | - |
| `active` | `bool` | Optional | **Default**: `True` |
| `description` | `str` | Optional | - |
| `privacy_type` | `str` | Optional | - |
| `custom_logo` | `bool` | Optional | **Default**: `True` |
| `logo_url` | `str` | Optional | - |
| `cname` | `List[str]` | Optional | - |
| `temp_cname` | `List[str]` | Optional | - |

## Example (as JSON)

```json
{
  "title": "my channel",
  "active": false,
  "description": "desc",
  "privacy_type": "private",
  "custom_logo": true,
  "logo_url": "https://dev-video.gumlet.io/646df1c9172a4a2fcac180b4/channel/logo.png"
}
```

