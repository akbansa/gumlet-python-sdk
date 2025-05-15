
# Error 28

## Structure

`Error28`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | - |
| `message` | `str` | Optional | - |
| `extra` | `Any` | Optional | - |
| `param` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "code": "parameter_missing",
  "message": "One or more required values are missing.",
  "param": "metrics",
  "extra": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

