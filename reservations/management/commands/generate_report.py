from django.core.management.base import BaseCommand
from datetime import date
from reservations.models import Reservations


class Command(BaseCommand):
    help = " Generate a report of upcoming reservations"

    def handle(self,*args,**options):
        upcoming_reservations = Reservations.objects.filter(date__gte=date.today())
        self.stdout.write(self.style.SUCCESS(F"Upcoming reservations: {upcoming_reservations.count()}"))
        for reservation in upcoming_reservations:
            self.stdout.write(self.style.SUCCESS(str(reservation)))
