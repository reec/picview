import os
import logging
from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger(__name__)


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
        return self.get_album_list()

    def _get_model(self):
        from picview.models import Album
        return Album

    def get(self, slug):
        album = cache.get('album-%s' % slug)
        if album:
            logger.debug('got album from cache: %s', album)
            return album
        for album in self.albums:
            if album.slug == slug:
                return album
        raise Exception('Could not find Album with slug %s' % slug)

    def all(self):
        return self.albums

    def get_album_list(self):
        album_list = cache.get('album-list')
        if album_list:
            return album_list

        pic_dir = settings.PICVIEW_DIR
        album_names = os.listdir(pic_dir)
        logger.debug('album names: %s', album_names)
        album_list = []
        for album_name in sorted(album_names, reverse=True):
            if (
                album_name[0] == '.' or
                not os.path.isdir(os.path.join(pic_dir, album_name))
            ):
                continue
            album_list.append(self.model(name=album_name))
        cache.set('album-list', album_list, 30)
        return album_list
