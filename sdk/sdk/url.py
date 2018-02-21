import re
from abc import abstractmethod, ABCMeta
from urllib.parse import urlparse

ALLOWED_URL_PREFIXES = ('http://', 'https://')
DEFAULT_URL_PREFIX = 'http://'
URL_LOCAL_IP_REGEX = re.compile(r'''
(localhost)|(127\.)|(192\.168\.)|(10\.)|(172\.1[6-9]\.)|(172\.2[0-9]\.)|(172\.3[0-1]\.)|(::1$)|([fF][cCdD])
''')


class Model(metaclass=ABCMeta):
    @abstractmethod
    def parse(self, *args, **kwargs) -> 'Model':
        pass


class ModelValidationException(Exception):
    def __init__(self, message: str):
        self.message = message


class URL(Model):
    def __init__(self, address: str=""):
        self._address = address

    @property
    def address(self):
        return self._address

    @classmethod
    def parse(cls, raw_address: str) -> 'URL':
        if not raw_address:
            raise ModelValidationException("empty url")
        elif '.' not in raw_address:
            raise ModelValidationException("url must contain at least one dot character")

        address = cls._force_protocol_prefix(raw_address)

        parsed_url = urlparse(address)
        if URL_LOCAL_IP_REGEX.findall(parsed_url.netloc):
            raise ModelValidationException("url represents invalid network location")

        return URL(address)

    @classmethod
    def _force_protocol_prefix(cls, address: str):
        url_lower = address.lower()

        for prefix in ALLOWED_URL_PREFIXES:
            if url_lower.startswith(prefix):
                break
        else:
            address = '{}{}'.format(DEFAULT_URL_PREFIX, address)

        return address
