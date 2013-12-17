import os
from django.conf import settings
from django.core.cache import cache


class AlbumManager(object):
    """
    A fake manager
    """

    def __init__(self):
        self._model = None
        self._albums = None

    @property
    def model(self):
        # defer importing
        if not self._model:
            self._model = self._get_model()
        return self._model

    @property
    def albums(self):
        if not self._albums:
            self._albums = self.get_album_list()
        return self._albums

    def _get_model(self):
        from picview.models import Album
        return Album

    def get(self, slug):
        album = cache.get('album-%s' % slug)
        if album:
            print('got album from cache')
            return album
        for album in self.albums:
            if album.slug == slug:
                return album
        raise Exception('Could not find Album with slug %s' % slug)

    def all(self):
        return self.albums

    def get_album_list(self):
        pic_dir = settings.PICVIEW_DIR
        album_names = os.listdir(pic_dir)
        album_list = []
        for album_name in album_names:
            album_list.append(self.model(name=album_name))
        return album_list