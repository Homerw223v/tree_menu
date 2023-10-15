from django.test import TestCase
from django.urls import reverse

from menu.models import Menu


class MenuViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        parent = Menu.objects.create(name='Python', slug='python', url='python')
        Menu.objects.create(name='manage.py', slug='managepy', url='python-managepy', parent=parent)

    def test_view_url_exists(self):
        response1 = self.client.get('')
        response2 = self.client.get('/python')
        response3 = self.client.get('/python-managepy')
        self.assertEquals(response1.status_code, 200)
        self.assertEquals(response2.status_code, 200)
        self.assertEquals(response3.status_code, 200)

    def test_url_access_via_name(self):
        parent = Menu.objects.get(name='Python')
        child = Menu.objects.get(name='manage.py')
        response1 = self.client.get(reverse('tree_menu:menu', args=(parent.url,)))
        response2 = self.client.get(reverse('tree_menu:menu', args=(child.url,)))
        response3 = self.client.get((reverse('tree_menu:start_page')))
        self.assertEquals(response1.status_code, 200)
        self.assertEquals(response2.status_code, 200)
        self.assertEquals(response3.status_code, 200)

    def test_template_used(self):
        parent = Menu.objects.get(name='Python')
        child = Menu.objects.get(name='manage.py')
        response1 = self.client.get(reverse('tree_menu:menu', args=(parent.url,)))
        response2 = self.client.get(reverse('tree_menu:menu', args=(child.url,)))
        self.assertTemplateUsed(response1, 'menu/home.html')
        self.assertTemplateUsed(response2, 'menu/home.html')

