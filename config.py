import os
import logging
from dotenv import load_dotenv

if os.path.exists('config.env'):
    load_dotenv('config.env', override=True)


class Config:
    def __init__(self) -> None:
        self.SESSION: str = os.environ.get('SESSION', BQCaDhqYP2wA7FfhByPw7vmWiGMHgSwWw_x8vQNud4owJdkKyM8ZBpT1nvZmoZdDO6o-sQcFfBA2Sw-t1kn4lisXYGKh-QqE6V5tii-KxK5ntFqGbx6C9n2_KUuZ9yketxMRunc8yEF9u_CeMvflp5QeygRXJV9IHvkIAB4iNig9UXz2yweyUB2fIkTMd8Y2bzJo3goVP6gv6rpYLfdjtIK7P16EuFcfkDTtYogidULh_ZqtlMVsvfoEp0ZFPpQKVM7naZN5f_Cp0aqDtJ7_rMJuaon7zEwTUlRi0TabkIN_NiNaiT-gkmDKSeuhGdJioSMPOJItW-S8Ten4QZfKMWO4AAAAAUwsSyoA)
        self.API_ID: str = os.environ.get('API_ID', 20244111)
        self.API_HASH: str = os.environ.get('API_HASH', b76d27da2a4220fe109fe9ef0e866530)
        self.SUDO: list = [int(id) for id in os.environ.get(
            'SUDO', ' ').split() if id.isnumeric()]
        if not self.SESSION or not self.API_ID or not self.API_ID:
            print('Error: SESSION, API_ID and API_HASH is required.'
                  'Please check your config.env file.')
            quit(0)
        self.SPOTIFY: bool = False
        self.SPOTIFY_CLIENT_ID: str = os.environ.get('SPOTIFY_CLIENT_ID', None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get(
            'SPOTIFY_CLIENT_SECRET', None)
        _log_level = os.environ.get('LOG_LEVEL', 'error').lower()
        if _log_level == 'error':
            self.LOG_LEVEL = logging.ERROR
        elif _log_level == 'info':
            self.LOG_LEVEL = logging.INFO
        elif _log_level == 'debug':
            self.LOG_LEVEL = logging.DEBUG
        else:
            self.LOG_LEVEL = logging.ERROR
        self.PREFIXES: list = os.environ.get('PREFIX', '!').split()
        self.DEFAULT_LANG: str = os.environ.get('DEFAULT_LANG', 'tr').lower()
        self.DEFAULT_STREAM_MODE: str = 'audio' if (os.environ.get(
            'DEFAULT_STREAM_MODE', 'audio').lower() == 'audio') else 'video'


config = Config()
