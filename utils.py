# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:03:02 2016

@author: yiyuezhuo
"""

import os

class Downloader(object):
    def __init__(self, bind_path, records = None, verbose = True):
        if not os.path.isdir(bind_path):
            os.makedirs(bind_path)
            print("make dirs",bind_path)
        self.bind_path = bind_path
        self.verbose = verbose
        self.records = records
    def run(self):
        self.start()
        for record in self.records:
            path = self.get_path(record)
            if os.path.isfile(path):
                self.print_skip(record)
            else:
                self.print_downloading(record)
                con = self.download(record)
                with open(path,'wb') as f:
                    f.write(con)
                self.print_downloaded(record)
        self.end()
    def start(self):
        pass
    def end(self):
        pass
    def print_map(self,record):
        return record
    def print_skip(self,record):
        if self.verbose:
            print("skip",self.print_map(record))
    def print_downloading(self, record):
        if self.verbose:
            print("start download",self.print_map(record))
    def print_downloaded(self, record):
        if self.verbose:
            print("downloaded",self.print_map(record))
    def download(self,record):
        raise NotImplementedError
    def get_path(self,record):
        raise NotImplementedError
