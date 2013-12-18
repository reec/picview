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
    image = Album.objects.get(slug).files[int(position)-1]
    return render_to_response(
        'image.html',
        {'image': image}
    )


def output_image(request, slug, position):
    image = Album.objects.get(slug).files[int(position)-1]
    image_data = open(image.get_path(), 'rb').read()
    return HttpResponse(image_data, content_type=mimetypes.guess_type(image.name)[0])


def output_image_thumbnail(request, slug, position):
    image = Album.objects.get(slug).files[int(position)-1]
    if not image.thumbnail_exists():
        image.generate_thumbnail()
    image_data = open(image.get_thumbnail_path(), 'rb').read()
    return HttpResponse(image_data, content_type='image/jpeg')