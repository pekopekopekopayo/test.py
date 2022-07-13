from datetime import datetime
from os import access
from django.core.management.base import BaseCommand
from item.models import Item

from user.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('실행')
        for i in range(1, 100):
            user = User.objects.create(account=f'user{i}', password=i)
            for j in range(1, 100):
                Item.objects.create(price=i*j, name=f'item{j}', user=user)
        print('종료')