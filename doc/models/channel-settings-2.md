
# Channel Settings 2

Configurations to set various channel settings.

## Structure

`ChannelSettings2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active` | `bool` | Optional | **Default**: `False` |
| `description` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `privacy_type` | [`PrivacyTypeEnum`](../../doc/models/privacy-type-enum.md) | Optional | - |
| `featured_video` | `str` | Optional | Video asset id, the asset should be in the same collection as channel |
| `password` | `str` | Optional | under channel_settings privacy_type must be "password-protected". Password length should be greater than 5 and lesser than 100 characters. |

## Example (as JSON)

```json
{
  "active": false,
  "description": "description2",
  "title": "title6",
  "privacy_type": "\"private\"",
  "featured_video": "featured_video8"
}
```

