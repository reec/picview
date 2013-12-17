import mimetypes
from django.http import HttpResponse
from django.shortcuts import render_to_response
from picview.models import Album, Image


def index(request):
    albums = Album.objects.all()
    return render_to_response(
        'index.html',
        {'albums': albums}
    )


def album(request, slug):
    album = Album.objects.get(slug)
    return render_to_response(
        'album.html',
        {'album': album}
    )


def image(request, slug, position):
    image = Album.objects.get(slug).files[int(position)]
    return render_to_response(
        'image.html',
        {'image': image}
    )


def output_image(request, slug, position):
    image = Album.objects.get(slug).files[int(position)]
    image_data = open(image.get_full_path(), 'rb').read()
    return HttpResponse(image_data, content_type=mimetypes.guess_type(image.name)[0])