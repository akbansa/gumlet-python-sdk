
# Video Playlist Request 1

## Structure

`VideoPlaylistRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `position` | `int` | Optional | Playlists have order in which they will be shown on the channel page. |
| `player_config` | [`PlayerConfig2`](../../doc/models/player-config-2.md) | Optional | Configure player settings for this playlist, it overrides the setting set on collection. |
| `channel_visibility` | `bool` | Optional | If true then playlist will be visible on channel page.<br><br>**Default**: `False` |

## Example (as JSON)

```json
{
  "channel_visibility": false,
  "title": "title8",
  "description": "description2",
  "position": 70,
  "player_config": {
    "preload": false,
    "autoplay": false,
    "disable_seek": false,
    "disable_player_controls": false,
    "powered_by_gumlet_overlay": false
  }
}
```

