# Python3 wangyi musicbox

modified by https://github.com/darknessomi/musicbox

provide a little python3 support.

## usage

```python
# In api.py file
album_id = '3190532'
bind_path = album_id

music_list = album_id_to_music_list(album_id)
mb = MusicBox(bind_path, records = music_list)
mb.run()
```

