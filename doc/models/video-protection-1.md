
# Video Protection 1

Gumlet provides multiple options for securing your video playback.

## Structure

`VideoProtection1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `signed_url` | `bool` | Optional | **Default**: `False` |
| `signed_url_secret` | `str` | Optional | - |
| `blacklisted_countries` | `List[str]` | Optional | Example: ["IN","USA"] |
| `whitelisted_referrers` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "signed_url": false,
  "signed_url_secret": "signed_url_secret0",
  "blacklisted_countries": [
    "blacklisted_countries1"
  ],
  "whitelisted_referrers": "whitelisted_referrers8"
}
```

