# bookshelf/management/commands/setup_groups.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Create default groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Define groups
        groups_permissions = {
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
            "Editors": ["can_create", "can_edit"],
            "Viewers": ["can_view"],
        }

        for group_name, perms in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_codename in perms:
                permission = Permission.objects.get(codename=perm_codename)
                group.permissions.add(permission)
            group.save()

        self.stdout.write(self.style.SUCCESS("Groups and permissions created successfully."))
