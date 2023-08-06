from django.shortcuts import render
from places.models import Place
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse


def place_detail_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_detail = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.order_by('index')],
        "description_short": place.annotation,
        "description_long": place.full_description,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        },
    }
    return JsonResponse(
        place_detail,
        json_dumps_params={
            'indent': 2,
            'ensure_ascii': False,
        }
    )


def get_features():
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        place.longitude,
                        place.latitude
                    ]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse(place_detail_view, args=[place.id])
                }
            }
        )
    return features


def index(request):
    geo_json = {
        "type": "FeatureCollection",
        "features": get_features()
    }
    print(geo_json)
    context = {'places': geo_json}
    
    return render(request, 'index.html', context=context)
