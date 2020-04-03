from django.test import Client, TestCase


class TestPostcodes(TestCase):
    """Tests for validate_postcode function."""
    def setUp(self):
        self.client = Client()

    def test_valid_postcode_with_space(self):
        response = self.client.get('/DN55 1PT/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), 'DN55 1PT is a valid UK postcode.')

    def test_valid_postcode_with_no_space(self):
        response = self.client.get('/DN551PT/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), 'DN55 1PT is a valid UK postcode.')

    def test_invalid_postcode(self):
        response = self.client.get('/Q33 8TH/')
        self.assertRaises(ValueError)
        self.assertEqual(response.content.decode("utf-8"), 'Invalid postcode - Q33 8TH.')
