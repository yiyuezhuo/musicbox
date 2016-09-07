# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:27:14 2016

@author: yiyuezhuo
"""

import NEMbox.api
from utils import Downloader

import os
import requests

ne = NEMbox.api.NetEase()

def music_id_to_url(music_id):
    return NEMbox.api.geturl_new_api(ne.songs_detail([music_id])[0])[0]
    
def album_id_to_music_list(album_id):
    return ne.album(album_id)
    
        
class MusicBox(Downloader):
    def download(self,record):
        url = music_id_to_url(record['id'])
        return requests.get(url).content
    def get_path(self,record):
        name = record['name']
        path = os.path.join(self.bind_path, '{}.mp3'.format(name))
        return path
    def print_map(self,record):
        return record['name']
            
def download_album(album_id):
    mb = Downloader(str(album_id),records = album_id_to_music_list(album_id))
    mb.run()
    
if __name__ == '__main__':
    album_id = '3190532'
    bind_path = album_id
    
    music_list = album_id_to_music_list(album_id)
    mb = MusicBox(bind_path, records = music_list)
    mb.run()