from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import connections


class Command(BaseCommand):

    def handle(self, *args, **options):
        conn = connections['default']
        conn.connect()
        User = get_user_model()
        if not User.objects.all():
            for user in settings.ADMINS:
                username = user[0].replace(' ', '')
                email = user[1]
                password = user[2]
                print('Creating account for %s (%s)' % (username, email))
                admin = User.objects.create_superuser(email=email, username=username, password=password)
                admin.is_active = True
                admin.is_admin = True
                admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
