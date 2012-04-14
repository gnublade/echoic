from django.test import TestCase
from django.test.utils import override_settings
from django.core.urlresolvers import reverse

from .models import Recording

@override_settings(DEBUG=True)
class RecordTest(TestCase):

    def test_record_request(self):
        response = self.client.get(reverse('tw:record'))
        self.assertContains(response, "<Record")

    def test_store_record(self):
        tel = '+012345678'
        url = 'http://example.com/recording.wav'
        response = self.client.post(reverse('tw:record'), {
            'RecordingUrl': url,
            'RecordingDuration': 10,
            'From': tel,
        })
        self.assertContains(response, "Thankyou")
        record = Recording.objects.get()
        self.assertEqual(record.url, url)
        self.assertEqual(record.duration, 10.0)
        self.assertEqual(record.recorded_by.username, tel)
        self.assertEqual(record.recorded_by.userprofile.phone_number, tel)
