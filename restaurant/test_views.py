from django.test import TestCase
from restaurant.models import Menu

# Create your tests here.
class MenuViewTest(TestCase):
    def setup():
        Menu.objects.create(title='IceCream',price=80,inventory=38)
        Menu.objects.create(title='Baklava',price=60,inventory=65)
        Menu.objects.create(title='Sobiyet',price=45,inventory=92)
    def test_getall(self):
        pass