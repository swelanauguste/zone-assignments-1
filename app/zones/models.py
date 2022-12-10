from django.db import models
from django.urls import reverse


class Technician(models.Model):
    technician_name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("technician_name",)

    def get_absolute_url(self):
        return reverse("zones:technician-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f"({self.id}) - {self.technician_name}"


class Zone(models.Model):
    zone_name = models.CharField(max_length=100, unique=True)
    technician = models.OneToOneField(Technician, on_delete=models.CASCADE, null=True)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ("order",)

    def get_absolute_url(self):
        return reverse("zones:zone-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"({self.id}) {self.zone_name}"


class Agency(models.Model):
    zone = models.ForeignKey(
        Zone, on_delete=models.CASCADE, related_name="agencies", null=True
    )
    agency_name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "agencies"
        ordering = ("agency_name",)

    def get_absolute_url(self):
        return reverse("zones:agency-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"(({self.id}) {self.agency_name}) - ({self.zone})"
