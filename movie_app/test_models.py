from django.test import TestCase
from .models import Item

# Create your tests here.
class TestModels(TestCase):
    def test_done_defaults_tofalse(self):
        item = Item.objects.create(title='Test Todo Item', director='Test Movie Items', genre='Test Movie Items', summary='', score=5)
        self.assertFalse(item.watched)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(title='Test Todo Item', director='Test Movie Items', genre='Test Movie Items', summary='', score=5)
        self.assertEqual(str(item), 'Test Todo Item')