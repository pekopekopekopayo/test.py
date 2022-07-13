from datetime import datetime
from os import access
from django.core.management.base import BaseCommand
from item.models import Item

from user.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        start = datetime.now()
        user = User.objects.prefetch_related('items').first()
        items = user.items.all()
        for _ in items:
            pass
        print('1.역참조',datetime.now() - start)
        start = datetime.now()
        for _ in items:
            pass
        print('2.역참조',datetime.now() - start)
        
        start = datetime.now()
        items = Item.objects.filter(user=user)
        for _ in items:
            pass
        print('1.필터링',datetime.now() - start)
        
        start = datetime.now()
        for _ in items:
            pass
        print('2.필터링',datetime.now() - start)