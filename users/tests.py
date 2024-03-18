from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

class RegisterTest(TestCase):

    def test_register_success(self):
        self.client.post(
            reverse('users:register'),
            data={
                'username': 'asadbekjon',
                'first_name': 'Asadbek',
                'last_name': 'Sotvoldiyev',
                'email': 'asadbeffffk@gmail.com',
                'password': '1234',
                'password2': '1234'
            }
        )

        user = User.objects.get(username="asadbekjon")

        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        self.assertEqual(user.first_name, "Asadbek")
        self.assertEqual(user.last_name, "Sotvoldiyev")
        self.assertEqual(user.email, "asadbeffffk@gmail.com")
        self.assertNotEqual(user.password, '1234')
        self.assertTrue(user.check_password('1234'))

    def test_register_page_url(self):
        response = self.client.get("/users/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/register.html')

    def test_login_success(self):
        self.client.post(
            reverse('users:login'),
            data = {
                'username': 'alijon',
                'password': '13221'
            }
        )
        c = Client()
        c.login(username="alijon", password="13221")