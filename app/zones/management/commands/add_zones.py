from django.core.management.base import BaseCommand

from ...models import Zone

ZONES_LIST = [
    "Zone One",
    "Zone Two",
    "Zone Three",
    "Zone Four",
    "Zone Five",
]

# Zone.objects.all().delete()



class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        for zone in ZONES_LIST:
            zone_name = zone.replace("\n", "")
            Zone.objects.get_or_create(
                zone_name=zone_name,
            )
            self.stdout.write(self.style.SUCCESS(f"{zone_name} added"))
