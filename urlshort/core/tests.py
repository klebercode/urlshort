from datetime import datetime

from django.test import TestCase
from urlshort.core.models import Link


class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_html(self):
        """Html must contain input tags"""
        tags = (('<input', 3),
                ('<span', 1),
                ('<button', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')


class LinkModelTest(TestCase):
    def setUp(self):
        self.obj = Link(
            slug_key='qF3gR4',
            my_url='http://mywebsite.com/',
            count='1'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Link.objects.exists())

    def test_last_access(self):
        """Link must have on auto last_access attr."""
        self.assertIsInstance(self.obj.last_access, datetime)
