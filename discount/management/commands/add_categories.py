from django.core.management.base import BaseCommand
from discount.models import Category


class Command(BaseCommand):
    help = "Add Multiple Category"

    def handle(self, *args, **options):
        cont = True
        while cont:
            category_name = input("Enter category name: ")
            category = Category.objects.create(name=category_name)
            category.save()

            cont = input("Enter Y to continue other key to end: ")
            if cont.lower() != "y":
                cont = False
