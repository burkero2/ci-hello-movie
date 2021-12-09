from django.test import TestCase
from .models import Item

# Create your tests here.
class TestViews(TestCase):
    def test_get_movie_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_app/movie_app_home.html')

    def test_movie_app_add_page(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_app/movie_app_add.html')

    def test_movie_app_edit_page(self):
        item = Item.objects.create(title='Test Todo Item', director='Test Movie Items', genre='Test Movie Items', summary='', score=5)
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_app/movie_app_edit.html')

    def test_can_add_movie(self):
        response = self.client.post('/add/', {'title': 'Test Movie Items', 'director': 'Test Movie Items', 'genre': 'Test Movie Items', 'summary': '', 'score': 5})
        self.assertRedirects(response, '/')

    def test_can_delete_movie(self):
        item = Item.objects.create(title='Test Todo Item', director='Test Movie Items', genre='Test Movie Items', summary='', score=5)
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_movie(self):
        item = Item.objects.create(title='Test Todo Item', director='Test Movie Items', genre='Test Movie Items', summary='', score=5, watched=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.watched)

    def test_can_edit_item(self):
        item = Item.objects.create(title='Test Todo Item', director='Test Movie Items', genre='Test Movie Items', summary='', score=5)
        response = self.client.post(f'/edit/{item.id}', {'title': 'Updated Name', 'director': 'Test Movie Items', 'genre': 'Test Movie Items', 'summary': '', 'score': 5})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.title, 'Updated Name')
