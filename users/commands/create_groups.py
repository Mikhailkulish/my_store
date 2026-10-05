from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        groups = {
            'admin': ['add_product', 'change_product', 'delete_product', 'view_product'],
            'moderator_of_products': ['can_unpublish_product', 'can_delete_any_product'],
            'viewers': ['view_product'],
        }

        for group_name, codenames in groups.items():
            group, _ = Group.objects.get_or_create(name=group_name)
            group.permissions.set(
                Permission.objects.filter(codename__in=codenames)
            )
            self.stdout.write(self.style.SUCCESS(f'Группа "{group_name}" готова'))
