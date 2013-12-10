from picview.managers import AlbumManager

class Album(object):
    """
    A fake model
    """

    objects = AlbumManager()

    def __init__(self, name=None):
        self.name = name

    def get_images(self):
        return []