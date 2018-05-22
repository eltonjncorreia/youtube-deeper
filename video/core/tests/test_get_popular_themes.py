from django.test import TestCase
from django.shortcuts import resolve_url as r


class GetPopularTheme(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('popular-themes'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTrue(self.resp, 'core/popular-themes.html')

