from django.test import TestCase
from django.shortcuts import resolve_url as r


class DetailTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('detail-video', 4))

    def test_template(self):
        self.assertTrue(self.resp, 'core/detail-video.html')

