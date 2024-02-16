from products.models import Artist


def access_all_artists(request):
    artists = Artist.objects.all()
    return {
        'all_artists': artists,
    }
