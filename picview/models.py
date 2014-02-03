import os
import logging
from PIL import Image as PILImage
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.cache import cache
from django.template.defaultfilters import slugify

from picview.managers import AlbumManager

logger = logging.getLogger(__name__)


class Album(object):
    """
    A fake model
    """

    objects = AlbumManager()

    def __init__(self, name=None):
        self.name = name
        self.slug = slugify(self.name)
        self._files = None
        self.cache()

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)

    @property
    def files(self):
        if not self._files is None:
            return self._files
        album_path = os.path.join(settings.PICVIEW_DIR, self.name)
        file_names = os.listdir(album_path)
        object_list = []
        for file_name in file_names:
            ext = os.path.splitext(file_name)[-1].lstrip('.').lower()
            if ext in settings.IMAGE_EXTS:
                obj = Image(name=file_name, album=self)
            elif ext in settings.VIDEO_EXTS:
                obj = Video(name=file_name, album=self)
            else:
                continue
            object_list.append(obj)
        self._files = object_list

        # Update cache now that we have the files too
        self.cache()
        return self._files

    def cache(self):
        logging.debug('caching %s with %d files', self.slug,
                      len(self._files or []))
        cache.set('album-%s' % self.slug, self)

    def get_images(self):
        return [obj for obj in self.files if isinstance(obj, Image)]

    def get_videos(self):
        return [obj for obj in self.files if isinstance(obj, Video)]

    def get_path(self):
        return os.path.join(settings.PICVIEW_DIR, self.name)


class File(object):
    def __init__(self, name=None, album=None):
        self.name = name
        self.slug = slugify(self.name)
        self.album = album
        self._position = None
        self._meta = {}

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)

    @property
    def position(self):
        if self._position is None:  # can be 0
            self._position = self.album.files.index(self)
        return self._position

    @property
    def meta(self):
        if not self._meta:
            self._meta = self._get_meta()
        return self._meta

    @property
    def resolution(self):
        return self.get_resolution()

    def is_first(self):
        return self.position is 0

    def is_last(self):
        return self.position is len(self.album.files)-1

    def _get_meta(self):
        raise NotImplementedError

    def get_view_url(self):
        raise NotImplementedError

    def get_url(self):
        raise NotImplementedError

    def get_thumbnail_url(self):
        raise NotImplementedError

    def get_resolution(self):
        return self.meta.get('resolution')

    def get_path(self):
        return os.path.join(self.album.get_path(), self.name)


class Image(File):
    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)

    def _get_meta(self):
        image = PILImage.open(self.get_path())
        # TODO: moar exif
        return {'resolution': '%sx%s' % image.size}

    def get_view_url(self):
        return reverse('image', args=[self.album.slug, self.position+1])

    def get_url(self):
        return reverse('output_image', args=[self.album.slug, self.position+1])

    def get_thumbnail_url(self):
        return reverse('output_image_thumbnail',
                       args=[self.album.slug, self.position+1])

    def get_thumbnail_path(self):
        return os.path.join(self.album.get_path(), 'thumbnails', self.name)

    def thumbnail_exists(self):
        return os.path.exists(self.get_thumbnail_path())

    def generate_thumbnail(self):
        image = PILImage.open(self.get_path())
        image.thumbnail((128, 128), PILImage.ANTIALIAS)

        # Create the subdir 'thumbnails' if it doesn't exist
        thumbnail_dir_path = os.path.join(self.album.get_path(), 'thumbnails')
        if not os.path.exists(thumbnail_dir_path):
            os.mkdir(thumbnail_dir_path)

        image.save(self.get_thumbnail_path())


class Video(File):
    def __init__(self, *args, **kwargs):
        super(Video, self).__init__(*args, **kwargs)

    def _get_meta(self):
        # TODO: look at the file and stuff
        return {'resolution': '1920x1080'}

    def get_view_url(self):
        return reverse('video', args=[self.album.slug, self.position+1])