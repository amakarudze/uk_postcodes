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
        response = self.client.get('/M1 1AE/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), 'M1 1AE is a valid UK postcode.')

    def test_valid_postcode_A99_format(self):
        response = self.client.get('/B33 8TH/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), 'B33 8TH is a valid UK postcode.')

    def test_valid_postcode_AA9A_format(self):
        response = self.client.get('/EC1A 1BB/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), 'EC1A 1BB is a valid UK postcode.')

    def test_valid_postcode_A9A_format(self):
        response = self.client.get('/W1A 0AX/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), 'W1A 0AX is a valid UK postcode.')

    def test_valid_postcode_AA9_format(self):
        response = self.client.get('/CR2 6XH/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), 'CR2 6XH is a valid UK postcode.')

    def test_valid_postcode_AA99(self):
        response = self.client.get('/GU16 7HF/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), 'GU16 7HF is a valid UK postcode.')

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

    def test_invalid_first_position(self):
        pass

    def test_invalid_second_position(self):
        pass

    def test_invalid_final_letters(self):
        pass
