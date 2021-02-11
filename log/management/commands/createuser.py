from django.core.management.base import BaseCommand, CommandError
from log.models import User

class Command(BaseCommand):
    help = 'Create new user'

    # def add_arguments(self, parser):
    #     parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        username = input('Enter usename: ')
        if not username:
            raise CommandError('Username is required')
        email = input('Enter email: ')
        if not email:
            raise CommandError('Email is required')
        password = input('Enter password: ')
        if not password:
            raise CommandError('Password is required')
        confirm_password = input('Confirm password: ')
        if password != confirm_password:
            raise CommandError('Confirm password don\'t match to password')
        permission = input('Enter permission(AD, CA, CS): ')
        if permission not in ['AD', 'CA', 'CS']:
            raise CommandError('Please choose right permission.')

        try:
            User.objects.create_user(username, email, password, permission)
            self.stdout.write(self.style.SUCCESS('Successfully create new user: %s' % username))
        except ValueError:
            raise CommandError(ValueError)