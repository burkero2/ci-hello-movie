from django.test import TestCase
from .forms import MovieForm

# Create your tests here.
class TestMovieForm(TestCase):
    def test_movie_title_is_required(self):
        form = MovieForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    # Extra Test: Check the Summary Field is Not required
    def test_summary_field_is_not_required(self):
        form = MovieForm({'title': 'Test Movie Items', 'director': 'Test Movie Items', 'genre': 'Test Movie Items', 'summary': '', 'score': 5})
        self.assertTrue(form.is_valid())


    def test_watched_field_is_not_required(self):
        form = MovieForm({'title': 'Test Movie Items', 'director': 'Test Movie Items', 'genre': 'Test Movie Items', 'summary': 'Test Movie Items', 'score': 5})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = MovieForm()
        self.assertEqual(form.Meta.fields, ['title', 'director', 'genre', 'summary', 'score', 'watched'])


