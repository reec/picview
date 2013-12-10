from django.shortcuts import render_to_response
from picview.models import Album

def index(request):
    albums = Album.objects.all()
    return render_to_response(
        'index.html',
        {'albums': albums}
    )