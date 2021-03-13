from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
  
  def test_create_user(self):
    User = get_user_model()
    user = User.objects.create_user(
      username='will',
      email='admin@admin.com',
      password='Ecirtaeb2'
    )
    
    self.assertEqual(user.username, 'will')
    self.assertEqual(user.email, 'admin@admin.com')
    self.assertTrue(user.is_active)
    self.assertFalse(user.is_staff)
    self.assertFalse(user.is_superuser)
