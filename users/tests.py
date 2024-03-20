from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.test import TestCase
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

    # Username o'lchamini tekshiradi
    def test_username_filed(self):

        response = self.client.post(
            reverse('users:register'),
            data={
                'username': 'g',
                'first_name': 'Asadbek',
                'last_name': 'Sotvoldiyev',
                'email': 'asadbeffffk@gmail.com',
                'password': '1234',
                'password2': '1234'
            }
        )

        user_count = User.objects.count()
        form = response.context['form']
        self.assertEqual(user_count, 0)
        self.assertTrue(form.errors)
        self.assertIn("username", form.errors.keys())
        self.assertEqual(form.errors['username'], ["Username 5 va 30 orasida bo'lishi kerak"])

    # Passwordlar bir xilligini tekshiradi
    def test_password_filed(self):
        response = self.client.post(
            reverse('users:register'),
            data={
                'username': 'asadbek',
                'first_name': 'Asadbek',
                'last_name': 'Sotvoldiyev',
                'email': 'asadbeffffk@gmail.com',
                'password': '12343434',
                'password2': '1234'
            }
        )

        user_count = User.objects.count()
        form = response.context['form']
        self.assertEqual(user_count, 0)
        self.assertTrue(form.errors)
        self.assertIn("password2", form.errors.keys())
        self.assertEqual(form.errors['password2'], ["Passwords don't match"])

    # email formaga to'g'ri kiritilishini tekshiradi
    def test_email_filed(self):

        response = self.client.post(
            reverse('users:register'),
            data={
                'username': 'asadbek',
                'first_name': 'Asadbek',
                'last_name': 'Sotvoldiyev',
                'email': 'asadbeffffk',
                'password': '1234',
                'password2': '1234'
            }
        )

        user_count = User.objects.count()
        form = response.context['form']
        self.assertEqual(user_count, 0)
        self.assertTrue(form.errors)
        self.assertIn("email", form.errors.keys())
        self.assertEqual(form.errors['email'], ["Enter a valid email address."])


    # Email bazada mavjudligini tekshiradi
    def test_email_exists(self):
        user = User.objects.create(username="alijon", first_name='Alijon',
                                   last_name='Boymirzayev', email='ali@gmail.com')
        user.set_password('1111')
        user.save()

        response = self.client.post(
            reverse('users:register'),
            data={
                'username': 'asadbek',
                'first_name': 'Asadbek',
                'last_name': 'Sotvoldiyev',
                'email': 'ali@gmail.com',
                'password': '1234',
                'password2': '1234'
            }
        )
        user_count = User.objects.count()
        form = response.context['form']
        self.assertEqual(user_count, 1)
        self.assertTrue(form.errors)
        self.assertIn("email", form.errors.keys())
        self.assertEqual(form.errors['email'], ["Bunday email bazada mavjud"])

    # Username bazada mavjud ekanligini tekshiradi
    def test_username_exists(self):
        user = User.objects.create(username="alijon", first_name='Alijon',
                                   last_name='Boymirzayev', email='ali@gmail.com')
        user.set_password('1111')
        user.save()

        response = self.client.post(
            reverse('users:register'),
            data={
                'username': 'alijon',
                'first_name': 'Asadbek',
                'last_name': 'Sotvoldiyev',
                'email': 'alijonsdjfhjdsf@gmail.com',
                'password': '1234',
                'password2': '1234'
            }
        )
        user_count = User.objects.count()
        form = response.context['form']
        self.assertEqual(user_count, 1)
        self.assertTrue(form.errors)
        self.assertIn("username", form.errors.keys())
        self.assertEqual(form.errors['username'], ["A user with that username already exists."])

class LoginTest(TestCase):

    def test_login_success(self):
        user = User.objects.create(username="alijon", first_name='Alijon',
                                   last_name='Boymirzayev', email='ali@gmail.com')
        user.set_password('1111')
        user.save()

        response = self.client.post(
            reverse('users:login'),
            data={
                'username': 'alijon',
                'password': '1111'
            }
        )

        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_username_len(self):
        user = User.objects.create(username="ali", first_name='Alijon',
                                   last_name='Boymirzayev', email='ali@gmail.com')
        user.set_password('1111')
        user.save()

        response = self.client.post(
            reverse('users:login'),
            data={
                'username': 'ali',
                'password': '1111'
            }
        )

        user_count = User.objects.count()
        form = response.context['form']
        self.assertEqual(user_count, 1)
        self.assertTrue(form.errors)
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'], ["Username 5 va 30 orasida bo'lishi kerak"])


    # Logout uchun test
    def test_logout_user(self):
        user = User.objects.create(username="alijon", first_name='Alijon',
                                   last_name='Boymirzayev', email='ali@gmail.com')
        user.set_password('1111')
        user.save()

        self.client.post(
            reverse('users:logout'),
            data={
                'username': 'alijon',
                'password': '1111'
            }
        )

        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

