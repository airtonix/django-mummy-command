from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from model_mommy import mommy


class Command(BaseCommand):
    args = '<modelpath modelpath:count ...>'
    help = 'Generate model instances using model-mommy'

    def handle(self, *args, **options):
        for modelpath in args:
            count = 1
            if ":" in modelpath:
                modelpath, count = modelpath.split(":")

            self.stdout.write("Processing: {}".format(modelpath))
            mommy.make(modelpath, _quantity=count)
