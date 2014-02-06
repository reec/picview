Installation
============

Requirements
------------

Ubuntu packages:
~~~~~~~~~~~~~~~~

- libreadline
- memcached
- libjpeg-dev (for PIL/Pillow)
- ffmpeg (for video thumbnail hack)

Python 3.3 virtual env (if you don't have python 3.3):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    git clone git://github.com/yyuu/pyenv.git ~/.pyenv

Add ~/.pyenv/shims:~/.pyenv/bin to PATH

::

    pyenv install 3.3.0
    pyenv shell 3.3.0
    virtualenv -p ~/.pyenv/versions/3.3.0/bin/python env


If you do have python 3.3:
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    virtualenv env

Stuff from pip:
~~~~~~~~~~~~~~~

::

    pip install -r requirements.pip

