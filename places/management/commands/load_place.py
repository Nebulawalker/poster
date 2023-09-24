import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from pathlib import Path
from urllib.parse import unquote, urlparse
import sys

from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = 'Добавить место на сайт из JSON-файла'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str)

    def handle(self, *args, **options):
        try:
            response = requests.get(options['json_url'])
            response.raise_for_status()
            location = response.json()
            image_urls = location['imgs']

            place, is_created = Place.objects.update_or_create(
                title=location['title'],
                annotation=location['description_short'],
                full_description=location['description_long'],
                longitude=location['coordinates']['lng'],
                latitude=location['coordinates']['lat'],
            )
        except requests.exceptions.HTTPError as error:
            print(error, file=sys.stderr)
            return

        if not is_created:
            place.images.all().delete()

        for index, image_url in enumerate(image_urls):
            try:
                filename = unquote(Path(urlparse(image_url).path).name)
                image_response = requests.get(image_url)
                image_response.raise_for_status()
                image_content = ContentFile(image_response.content)

                place_image = PlaceImage(index=index, place=place)
                place_image.image.save(filename, content=image_content)
            except requests.exceptions.HTTPError as error:
                print(error, file=sys.stderr)