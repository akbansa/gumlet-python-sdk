
# Video Playlist Response

## Structure

`VideoPlaylistResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `collection_id` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `player_config` | [`PlayerConfig`](../../doc/models/player-config.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": "659693cadc46251d898930f2",
  "collection_id": "646df1c9173a4a2fcac180b4",
  "title": "Playlist-Title",
  "description": "This is description for playlist.",
  "player_config": {
    "preload": false,
    "autoplay": false,
    "disable_seek": false,
    "disable_player_controls": false,
    "powered_by_gumlet_overlay": false
  }
}
```

