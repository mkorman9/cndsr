from unittest import TestCase

from sdk.url_processor import process_url, InvalidURLException


class TestUrlProcess(TestCase):
    def test_valid_url_should_pass_through(self):
        # given
        url = 'https://stackoverflow.com/questions/1789945'

        # when
        processed_url = process_url(url)

        # then
        assert url == processed_url, '{} != {}'.format(processed_url, url)

    def test_protocol_prefix_should_be_appended(self):
        # given
        url = 'stackoverflow.com/questions/1789945'

        # when
        processed_url = process_url(url)

        # then
        expected_url = 'http://{}'.format(url)
        assert expected_url == processed_url, '{} != {}'.format(processed_url, expected_url)

    def test_should_fail_if_no_dots_are_present(self):
        # given
        url = 'questions'

        # when then
        with self.assertRaises(InvalidURLException):
            process_url(url)
