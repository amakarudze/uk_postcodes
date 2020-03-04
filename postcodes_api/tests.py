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

    def test_valid_postcode_A9_format(self):
        pass

    def test_valid_postcode_A99_format(self):
        pass

    def test_valid_postcode_AA9A_format(self):
        pass

    def test_valid_postcode_A9A_format(self):
        pass

    def test_valid_postcode_AA9_format(self):
        pass

    def test_valid_postcode_AA99(self):
        pass

    def test_invalid_postcode(self):
        pass

    def test_invalid_postcode_too_short(self):
        pass

    def test_invalid_postcode_too_long(self):
        pass

    def test_invalid_postcode_A9_format(self):
        pass

    def test_invalid_postcode_A99_format(self):
        pass

    def test_invalid_postcode_AA9A_format(self):
        pass

    def test_invalid_postcode_A9A_format(self):
        pass

    def test_invalid_postcode_AA9_format(self):
        pass

    def test_invalid_postcode_AA99(self):
        pass

    def test_invalid_postcode_AA9_outer(self):
        pass

    def test_invalid_postcode_A9A_outer(self):
        pass

    def test_invalid_postcode_AAA_outer(self):
        pass

    def test_invalid_postcode_999_outer(self):
        pass
