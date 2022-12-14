from django.core.management.base import BaseCommand

from ...models import Agency, Zone

Agency.objects.all().delete()

ZONE_ONE_AGENCIES = [
    "Audit",
    "Contact Centre",
    "Housing",
    "Inland Revenue",
    "Land Registry",
    "Parastatal & Monitoring",
    "Planning",
    "PM Office",
    "Public Service",
    "Equity",
]

ZONE_TWO_AGENCIES = [
    "AG Chambers",
    "Agriculture",
    "Education",
    "FRSA",
    "Health",
    "Service & Teaching Commission",
    "Tourism",
    "Legislative Drafting",
    "Energy",
    "Commerce",
]

ZONE_THREE_AGENCIES = [
    "Civil Status",
    "Customs",
    "Electoral",
    "Fire",
    "Justice",
    "Parliament",
    "Parliamentary Commission",
    "Police",
    "Post Office",
    "Printery",
    "Probation and Parole",
    "Treasury",
    "Home Affairs",
    "Human Services",
    "Youth & Sports",
    "Substance Abuse",
    "Welfare",
]

ZONE_FOUR_AGENCIES = [
    "GIS",
    "ROCIP",
    "Labour",
    "Finance",
    "Sustainable",
    "Crown Lands",
    "Leader of the Opposition",
    "GOV GEN",
    "ICT",
    "Integrity Commission",
    "Economic Affairs",
    "Budget",
    "NCA",
    "SSDF",
]

ZONE_FIVE_AGENCIES = [
    "Bordelais",
    "Human Services (South)",
    "Infrastructure (North & South)",
    "Probation (South)",
    "Second District Court",
    "Treasury Sub Offices",
    "Youth and Sports (Anse La Raye)",
    "Boys Training Centre",
    "NEMO",
    "OKEU",
    "External Affairs",
    "Public Service Training",
    "Infrastructure (Bexon)",
    "Equity External Locations",
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        for agency in ZONE_ONE_AGENCIES:
            zone = Zone.objects.get(zone_name__icontains="zone One")
            agency_name = agency.replace("\n", "")
            Agency.objects.get_or_create(
                zone=zone,
                agency_name=agency_name,
            )
            self.stdout.write(self.style.SUCCESS(f"{agency_name} added to {zone}"))

        for agency in ZONE_TWO_AGENCIES:
            zone = Zone.objects.get(zone_name__icontains="zone Two")
            agency_name = agency.replace("\n", "")
            Agency.objects.get_or_create(
                zone=zone,
                agency_name=agency_name,
            )
            self.stdout.write(self.style.SUCCESS(f"{agency_name} added to {zone}"))

        for agency in ZONE_THREE_AGENCIES:
            zone = Zone.objects.get(zone_name__icontains="zone Three")
            agency_name = agency.replace("\n", "")
            Agency.objects.get_or_create(
                zone=zone,
                agency_name=agency_name,
            )
            self.stdout.write(self.style.SUCCESS(f"{agency_name} added to {zone}"))

        for agency in ZONE_FOUR_AGENCIES:
            zone = Zone.objects.get(zone_name__icontains="zone Four")
            agency_name = agency.replace("\n", "")
            Agency.objects.get_or_create(
                zone=zone,
                agency_name=agency_name,
            )
            self.stdout.write(self.style.SUCCESS(f"{agency_name} added to {zone}"))

        for agency in ZONE_FIVE_AGENCIES:
            zone = Zone.objects.get(zone_name__icontains="zone Five")
            agency_name = agency.replace("\n", "")
            Agency.objects.get_or_create(
                zone=zone,
                agency_name=agency_name,
            )
            self.stdout.write(self.style.SUCCESS(f"{agency_name} added to {zone}"))
