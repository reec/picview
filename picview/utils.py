import logging
import subprocess
import os

from PIL import Image
from io import BytesIO
from django.conf import settings

logger = logging.getLogger(__name__)

def get_video_frame(source, frame='00:00:01', binary=None):
    """
    Get video frame as PIL.Image.Image. Requires ffmpeg installed.

    .. warning::

        Using `-ss` argument for position will cause ffmpeg to bork if the
        frame is "outside" video. There's surely an argument for getting the
        nearest frame.

    :param source: Filepath to video
    :param frame: Seek expressed as `HH:MM:SS` or frame number
    :param binary: Path to `ffmpeg` binary. Defaults to django settings.
    :return: :py:class:`PIL.Image.Image`
    """
    if not binary:
        binary = settings.FFMPEG_BINARY

    # Tighten belt
    if not os.path.isfile(source):
        raise IOError('File %s not found' % source)

    # Run ffmpeg with our video as input. Output to stdout for python to
    # collect raw image as jpeg (image2)
    command_args = [binary, '-an', '-ss', frame, '-i', source, '-f', 'image2',
                    '-vframes', '1', '-y', '-']
    logger.debug('running command: %s', command_args)
    command = subprocess.Popen(command_args, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = command.communicate()

    if not stdout:
        logger.error('Error generating thumbnail for %s: %s', source, stderr)
        return None

    # Read binary data into PIL
    image = Image.open(BytesIO(stdout))
    image.load()
    return image