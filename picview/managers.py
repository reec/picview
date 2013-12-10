import os
from django.conf import settings

class BaseManager(object):
    def __init__(self, model):
        self.model = model

class AlbumManager(BaseManager):
    """
    A fake manager
    """

    def get(self, name):
        return None # An Album

    def all(self):
        return self.get_album_list()

    def get_album_list(self):

        pic_dir = settings.PICVIEW_DIR
        album_names = os.listdir(pic_dir)
        album_list = []
        for album_name in album_names:
            album_list.append(self.model(name=album_name))
        return album_list