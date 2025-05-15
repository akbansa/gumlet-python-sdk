
# Video Assets Update Request

## Structure

`VideoAssetsUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_id` | `str` | Required | Asset Id |
| `title` | `str` | Optional | Specify a text string or identifier which can be used for filtering or searching the asset. |
| `description` | `str` | Optional | Attach some textual data with the asset. This field is neither searchable nor filterable. |
| `tag` | `str` | Optional | Specify a text string or identifier which can identify an asset or bunch of assets later. You can pass multiple comma separated values. |
| `call_to_actions` | [`List[CallToAction]`](../../doc/models/call-to-action.md) | Optional | CTA, is an explicit prompt within the video content encouraging viewers to take a particular action. |
| `metadata` | `str` | Optional | Set of key-value pairs that you can attach to this Asset. This can be useful for storing additional information.<br/> Example: <br/> <code>  {  "internal_video_id" : "123Abc"  }  </code> |
| `remove_subtitles` | `List[str]` | Optional | Comma separated string of language codes. |
| `generate_subtitles` | [`GenerateSubtitles3`](../../doc/models/generate-subtitles-3.md) | Optional | Gumlet allowes to generate subtitles from the audio stream (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes) |

## Example (as JSON)

```json
{
  "asset_id": "asset_id6",
  "title": "title6",
  "description": "description2",
  "tag": "tag8",
  "call_to_actions": [
    {
      "text": "text0",
      "url": "url4",
      "start_time": 246,
      "end_time": 226,
      "font_color": "font_color6"
    }
  ],
  "metadata": "metadata8"
}
```

