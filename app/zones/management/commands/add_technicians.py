from django.core.management.base import BaseCommand

from ...models import Technician

TECHNICIAN_LIST = [
    "Swelan Auguste",
    "Brandon Volney",
    "David St. Romain",
    "Nain Wells",
    "Samuel Edmund",
]

# Technician.objects.all().delete()



class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        for technician in TECHNICIAN_LIST:
            technician_name = technician.replace("\n", "")
            Technician.objects.get_or_create(
                technician_name=technician_name,
            )
            self.stdout.write(self.style.SUCCESS(f"{technician_name} added"))
