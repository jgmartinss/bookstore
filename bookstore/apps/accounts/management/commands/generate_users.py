from django.core.management.base import BaseCommand, CommandError

from bookstore.apps.accounts import factories, models


class Command(BaseCommand):
    help = "Generates random user"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int)

        parser.add_argument(
            "--clear",
            action="store_true",
            dest="clear",
            default=False,
            help="Clear all existing coupons first",
        )

    def handle(self, *args, **options):
        count = options["count"]
        if options["clear"]:
            models.User.objects.all().delete()
        factories.UserFactory.create_batch(size=count)
        self.stdout.write(self.style.SUCCESS(f"Generated {count} user(s)!"))
