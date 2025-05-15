
# Video Profiles Request

## Structure

`VideoProfilesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Profile name or identifier.<br><br>**Default**: `'Gumlet-Profile-1'` |
| `format` | [`Format1Enum`](../../doc/models/format-1-enum.md) | Required | Transcode and deliver the asset in the requested format. The options can be one of `ABR` (HLS + DASH) and `MP4`.<br><br>**Default**: `'ABR'` |
| `width` | `str` | Optional | Resize video with the given width. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset width will be ignored. Only applicable when specified `format` is `MP4`. |
| `height` | `str` | Optional | Resize video with the given height. Can be an absolute value in pixels or a percentage value with the `%` suffix. Specified values greater than the original asset height will be ignored. Only applicable when specified `format` is `MP4`. |
| `resolution` | `str` | Optional | Required resolutions of the transformed asset in case of HLS or MPEG-DASH delivery format. Can be a comma separated string out of the following values:  `240p`, `360p`, `480p`, `540p`, `720p`,  and `1080p`. Re-sized rendition will retain the input aspect ratio. |
| `crop` | [`Crop`](../../doc/models/crop.md) | Optional | This transformation can be used to crop the video by defining a rectangular area within the dimensions of the output video. |
| `pad` | [`Pad`](../../doc/models/pad.md) | Optional | This transformation can be used to add padding to the video. |
| `trim` | [`Trim`](../../doc/models/trim.md) | Optional | Trim transformation can be used to trim videos based on time duration. |
| `image_overlay` | [`ImageOverlay`](../../doc/models/image-overlay.md) | Optional | Image overlay can be used to brand a video or add a visual label in the form of an image. |
| `text_overlay` | [`TextOverlay`](../../doc/models/text-overlay.md) | Optional | Text overlay can be used to brand a video or add a label in the form of text. |
| `animated_gif` | [`AnimatedGif2`](../../doc/models/animated-gif-2.md) | Optional | Create an animated GIF from a video. |
| `generate_subtitles` | [`GenerateSubtitles`](../../doc/models/generate-subtitles.md) | Optional | Gumlet allows to generate subtitles from the audio stream (use <a href='https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes'> ISO 639-1 </a> Language Codes) |
| `mp_4_access` | `bool` | Optional | Creates `mp4` version for download purpose in case of `MPEG-DASH` or `HLS` delivery format. **Default: `false`** |
| `per_title_encoding` | `bool` | Optional | Gumlet analyzes each input video on a wide range of visual aspects. Based on the analysis, it chooses a unique set of transcoding options for processing the video. This ensures that the output video is of optimal size and best quality. **Default: `true`** |
| `process_low_resolution_input` | `bool` | Optional | Currently, the minimum supported frame size is `57600` (`240x240`) pixels for `HLS/DASH` and `21025` (`145x145`) pixels for `MP4` format. However, enabling this flag will allow Gumlet to simply put your video asset into the specified delivery format without transcoding and optimization. Enabling this flag will cause any kind of specified video transformation to be ignored if you input video asset frame size is lower than the minimum supported frame size for the specified format. **Default: `false`** |
| `audio_only` | `bool` | Optional | This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case,This flag allows Gumlet to transcode and deliver audio-only in the specified format. In this case, video transformation and thumbnails/animated GIFs would not be created. **Default: `false`** |
| `enable_drm` | `bool` | Optional | Enable DRM encryption for transcoded videos. Gumlet supports Widevine and Fairplay DRMs. |

## Example (as JSON)

```json
{
  "name": "Gumlet-Profile-1",
  "format": "ABR",
  "width": "width4",
  "height": "height6",
  "resolution": "resolution4",
  "crop": {
    "horizontal_margin": "horizontal_margin6",
    "vertical_margin": "vertical_margin4",
    "width": "width0",
    "height": "height2"
  },
  "pad": {
    "top": "top0",
    "left": "left0",
    "bottom": "bottom2",
    "right": "right0",
    "color": "color8"
  }
}
```

