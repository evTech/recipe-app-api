from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='testuser@mitco.com', password='testpass'):
    """ Create a smaple user """
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successul(self):
        """Test creating a new user with an email is successful """
        email = 'test@vaughen.com'
        password = 'TestPaswword123!'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email for a new user is normalized"""
        email = 'test@VAUGHEN.com'
        user = get_user_model().objects.create_user(
                email=email,
                password='test123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating a user with no email error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                    email=None,
                    password='test123'
            )

    def test_create_new_superuser(self):
        """Test creating a new super user """
        email = 'test@vaughen.com'
        password = 'TestPaswword123!'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """ Test the tag string representation """
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """ Test the ingredient string representation """
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """ test the recipe string repersentation """
        recipe = models.Recipe.objects.create(
            user=sample_user(),

            title= 'Steak and mushroom sauce',
            time_minutes= 5,
            price= 5.00
        )

        self.assertEqual(str(recipe), recipe.title)
