from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from django_extensions.management.shells import import_objects

from test.factories import UserFactory

User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "-admin",
            type=bool,
            help="Create Admin",
        )

    def handle(self, *args, **kwargs):
        self.stdout.write("Start loading dummy")

        if kwargs.get("admin"):
            # Local admin account
            UserFactory(
                username="admin",
                email="admin@test.com",
                password="1234",
                is_staff=True,
            )

        # populates globals() with django models, so no need to worry about importing them
        # https://stackoverflow.com/questions/59267620/how-to-import-all-django-models-and-more-in-a-script
        options = {"quiet_load": True}
        style = BaseCommand().style

        imported_objects = import_objects(options, style)
        globals().update(imported_objects)

        UserFactory.create_batch(size=10)

        self.stdout.write("Finish load dummy")
