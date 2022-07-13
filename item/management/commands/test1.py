from datetime import datetime
from os import access
from django.core.management.base import BaseCommand
from item.models import Item

from user.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        user = User.objects.first()
        start = datetime.now()
        for _ in user.items.all():
            pass
        print('역참조',datetime.now() - start)
        
        start = datetime.now()
        for data in Item.objects.filter(user=user):
            pass
        print('필터링',datetime.now() - start)