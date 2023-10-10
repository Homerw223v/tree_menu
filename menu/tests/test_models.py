from django.test import TestCase

from menu.models import Menu


class TestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Menu.objects.create(name='Python')
        menu = Menu.objects.get(name='Python')

    def test_menu_name_verbose_name(self):
        menu = Menu.objects.get(name='Python')
        field_label = menu._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'URL')

    def test_menu_url_verbose_name(self):
        menu = Menu.objects.get(name='Python')
        field_label = menu._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Name')

    def test_parent_verbose_name(self):
        menu = Menu.objects.get(name='Python')
        field_label = menu._meta.get_field('parent').verbose_name
        self.assertEquals(field_label, 'Parent to this element')

    def test_str_method(self):
        menu = Menu.objects.get(name='Python')
        self.assertEqual(menu.__str__(), 'Python')

    def test_menu_check_parent(self):
        menu = Menu.objects.get(name='Python')
        field = menu.parent
        self.assertEquals(field, None)

    def test_max_length(self):
        menu = Menu.objects.get(name='Python')
        m_l_name = menu._meta.get_field('name').max_length
        m_l_slug = menu._meta.get_field('slug').max_length
        m_l_url = menu._meta.get_field('url').max_length
        self.assertEquals(m_l_name, 200)
        self.assertEquals(m_l_slug, 200)
        self.assertEquals(m_l_url, 1000)


class MenuParentTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        parent = Menu.objects.create(name='Python', slug='python', url='python')
        Menu.objects.create(name='manage.py', slug='managepy', url='python-managepy', parent=parent)

    def test_have_parent(self):
        child = Menu.objects.get(name='manage.py')
        self.assertEquals(child.parent.__str__(), 'Python')
