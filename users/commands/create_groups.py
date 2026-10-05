from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        groups = {
            'moderator_of_products': ['add_product', 'change_product', 'delete_product', 'view_product'],
            'viewers': ['view_product'],
        }

        for group_name, codenames in groups.items():
            group, _ = Group.objects.get_or_create(name=group_name)
            group.permissions.set(
                Permission.objects.filter(codename__in=codenames)
            )
            self.stdout.write(self.style.SUCCESS(f'Группа "{group_name}" готова'))
