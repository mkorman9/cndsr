from unittest import TestCase

from sdk.url import URL, ModelValidationError


class TestUrl(TestCase):
    def test_valid_url_should_pass_through(self):
        # given
        url = 'https://stackoverflow.com/questions/1789945'

        # when
        processed_url = URL.parse(url)

        # then
        assert url == processed_url.address, '{} != {}'.format(processed_url, url)

    def test_protocol_prefix_should_be_appended(self):
        # given
        url = 'stackoverflow.com/questions/1789945'

        # when
        processed_url = URL.parse(url)

        # then
        expected_url = 'http://{}'.format(url)
        assert expected_url == processed_url.address, '{} != {}'.format(processed_url, expected_url)

    def test_should_fail_if_no_dots_are_present(self):
        # given
        url = 'questions'

        # when then
        with self.assertRaises(ModelValidationError):
            URL.parse(url)

    def test_should_fail_for_local_addresses(self):
        # given
        banned_urls = (
            'http://localhost:8080/asd',
            '127.0.0.1/?p=123',
            'http://user:pass@192.168.1.1'
        )

        # when then
        for banned_url in banned_urls:
            with self.assertRaises(ModelValidationError):
                URL.parse(banned_url)
