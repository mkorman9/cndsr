
ALLOWED_URL_PREFIXES = ('http://', 'https://')
DEFAULT_URL_PREFIX = 'http://'
URL_LOCAL_IP_REGEX = r'''
    (^localhost$)|(^127\.)|(^192\.168\.)|(^10\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^::1$)|(^[fF][cCdD])
'''


class InvalidURLException(Exception):
    def __init__(self, message):
        self.message = message


def process_url(url):
    """
    Validates given URL against parsing rules. Returns modified URL, ready to store in redis.
    Throws InvalidURLException for critical errors.
    """
    if not url:
        raise InvalidURLException("empty url")
    elif '.' not in url:
        raise InvalidURLException("url must contain at least one dot character")

    url = _force_protocol_prefix(url)

    # TODO: validate domain name

    return url


def _force_protocol_prefix(url):
    url_lower = url.lower()

    for prefix in ALLOWED_URL_PREFIXES:
        if url_lower.startswith(prefix):
            break
    else:
        url = '{}{}'.format(DEFAULT_URL_PREFIX, url)

    return url
