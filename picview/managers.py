import os
from django.conf import settings

class AlbumManager(object):
    """
    A fake manager
    """

    def __init__(self):
        self._model = None

    @property
    def model(self):
        # defer importing
        if not self._model:
            self._model = self._get_model()
        return self._model

    def _get_model(self):
        from picview.models import Album
        return Album

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