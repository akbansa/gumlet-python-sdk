
# Trim

Trim transformation can be used to trim videos based on time duration.

## Structure

`Trim`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_offset` | `float` | Required | Start offset in number of seconds or in `HH:MM:SS` format. |
| `end_offset` | `float` | Required | End offset in number of seconds or in `HH:MM:SS` format. |
| `duration` | `float` | Optional | Duration can be used in conjunction with `start_offset` parameter, can be specified in number of seconds. |

## Example (as JSON)

```json
{
  "start_offset": 173.86,
  "end_offset": 136.36,
  "duration": 18.42
}
```

