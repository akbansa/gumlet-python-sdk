
# Video Assets Upload Request

## Structure

`VideoAssetsUploadRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `collection_id` | `str` | Required | Gumlet video collection id. |
| `format` | [`Format1Enum`](../../doc/models/format-1-enum.md) | Required | Transcode and deliver the asset in the requested format. The options can be one of `ABR` (HLS + DASH) and `MP4`. |
| `profile_id` | `str` | Optional | Provide `profile_id` of the previously created video profile. This parameter will override all the parameters (except `input` and `collection_id`) from the video profile. |
| `tag` | `List[str]` | Optional | Specify a text string or identifier which can identify an asset or bunch of assets later. |
| `title` | `str` | Optional | Specify a text string or identifier which can be used for filtering or searching the asset. |
| `description` | `str` | Optional | Attach some textual data with the asset. This field is neither searchable nor filterable. |
| `playlist_id` | `str` | Optional | Add this asset to a playlist. |
| `metadata` | `str` | Optional | Set of key-value pairs that you can attach to this Asset. This can be useful for storing additional information.<br/> Example: <br/> <code>  {  "internal_video_id" : "123Abc"  }  </code> |
| `call_to_actions` | [`List[CallToAction]`](../../doc/models/call-to-action.md) | Optional | CTA, is an explicit prompt within the video content encouraging viewers to take a particular action. |
| `width` | `str` | Optional | Resize video with the given width. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset width will be ignored. Applicable only when specified format is `MP4`. |
| `height` | `str` | Optional | Resize video with the given height. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset height will be ignored. Applicable only when specified format is `MP4`. |
| `enable_drm` | `bool` | Optional | Enable DRM encryption for transcoded videos. Gumlet supports Widevine and Fairplay DRMs. |
| `pad` | [`Pad`](../../doc/models/pad.md) | Optional | This transformation can be used to add padding to the video. |
| `crop` | [`Crop`](../../doc/models/crop.md) | Optional | This transformation can be used to crop the video by defining a rectangular area within the dimensions of the output video. |
| `image_overlay` | [`ImageOverlay`](../../doc/models/image-overlay.md) | Optional | Image overlay can be used to brand a video or add a visual label in the form of an image. |
| `text_overlay` | [`TextOverlay`](../../doc/models/text-overlay.md) | Optional | Text overlay can be used to brand a video or add a label in the form of text. |
| `trim` | [`Trim`](../../doc/models/trim.md) | Optional | Trim transformation can be used to trim videos based on time duration. |
| `animated_gif` | [`AnimatedGif`](../../doc/models/animated-gif.md) | Optional | Create an animated GIF from the video. |
| `resolution` | `str` | Optional | Required resolutions of the transformed asset in case of HLS or MPEG-DASH delivery format. Can be a comma separated string out of the following values: `240p`, `360p`, `480p`, `540p`, `720p`, and `1080p`. Re-sized rendition will retain the input aspect ratio. |
| `generate_subtitles` | [`GenerateSubtitles`](../../doc/models/generate-subtitles.md) | Optional | Gumlet allows to generate subtitles from the audio stream (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes) |
| `mp_4_access` | `bool` | Optional | Creates `MP4` version for download purpose in case of `MPEG-DASH` or `HLS` delivery format. **Default: `false`** |
| `per_title_encoding` | `bool` | Optional | Gumlet analyzes each input video on a wide range of visual aspects. Based on the analysis, it chooses a unique set of transcoding options for processing the video. This ensures that the output video is of optimal size and best quality. **Default: `true`** |
| `process_low_resolution_input` | `bool` | Optional | Currently, the minimum supported frame size is `57600` (`240x240`) pixels for `HLS/DASH` and `21025` (`145x145`) pixels for `MP4` format. However, enabling this flag will allow Gumlet to simply put your video asset into the specified delivery format without transcoding and optimization. Enabling this flag will cause any kind of specified video transformation to be ignored if you input video asset frame size is lower than the minimum supported frame size for the specified format. **Default: `false`** |
| `audio_only` | `bool` | Optional | This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case, video transformation and thumbnails/animated GIFs would not be created. **Default: `false`** |
| `keep_original` | `bool` | Optional | Gumlet by default saves the original file uploaded, if you don't want Gumlet to save your original files then you set this flag false. |
| `thumbnail` | `str` | Optional | Specify second or percentage value of video duration to capture thumbnail image from. |
| `enable_preview_thumbnails` | `bool` | Optional | Enable video preview thumbnails. Default: true |

## Example (as JSON)

```json
{
  "collection_id": "collection_id6",
  "format": "ABR",
  "profile_id": "profile_id6",
  "tag": [
    "tag0",
    "tag1",
    "tag2"
  ],
  "title": "title0",
  "description": "description4",
  "playlist_id": "playlist_id6"
}
```

