
# Additional Track

## Structure

`AdditionalTrack`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Required | URL or web address of a file that Gumlet should download to add a stream. |
| `mtype` | `str` | Required | Type of additional track. Value can be either audio or subtitle. |
| `language_code` | `str` | Required | The language code value represents BCP 47 specification compliant value. For example, en for English. |
| `name` | `str` | Optional | The name of the track containing a human-readable description. |

## Example (as JSON)

```json
{
  "url": "url6",
  "type": "type8",
  "language_code": "language_code0",
  "name": "name2"
}
```

