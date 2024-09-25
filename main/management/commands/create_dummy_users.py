from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Product

class Command(BaseCommand):
    help = 'Create 2 dummy users and 3 data'

    def handle(self, *args, **kwargs):
    
        cookiecat, created1 = User.objects.get_or_create(username='CookieCat')
        if created1:
            cookiecat.set_password('cookiecat123')
            cookiecat.save()

        chocodog, created2 = User.objects.get_or_create(username='ChocoDog')
        if created2:
            chocodog.set_password('chocodog123')
            chocodog.save()

        Product.objects.create(user=cookiecat, name='Pink cookie', price=5000, description='Baked with strawberry.')
        Product.objects.create(user=cookiecat, name='Purple cookie', price=4000, description='Baked with grapes.')
        Product.objects.create(user=cookiecat, name='Blue cookie', price=3000, description='Baked with blueberries.')

        Product.objects.create(user=chocodog, name='Choco cookie', price=6000, description='Baked with chocolate chips.')
        Product.objects.create(user=chocodog, name='Vanilla cookie', price=7000, description='Baked with vanilla.')
        Product.objects.create(user=chocodog, name='Orange Cookies', price=5000, description='Baked with oranges.')

        self.stdout.write(self.style.SUCCESS('Dummy users and cookie data created successfully'))