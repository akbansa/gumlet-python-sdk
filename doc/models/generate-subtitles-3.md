
# Generate Subtitles 3

Gumlet allowes to generate subtitles from the audio stream (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes)

## Structure

`GenerateSubtitles3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `audio_language` | `str` | Optional | Language code for native language of the audio. |
| `subtitle_languages` | `str` | Optional | Comma separated string of language codes for which subtitle needs to be generated. Maximum four language codes are allowed. |

## Example (as JSON)

```json
{
  "audio_language": "audio_language4",
  "subtitle_languages": "subtitle_languages6"
}
```

