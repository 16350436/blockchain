from web3 import Web3

GANACHE_URL = "http://127.0.0.1:7545"
FLASK_DEBUG = False
WEB3_HTTP_PROVIDER = Web3(Web3.HTTPProvider(GANACHE_URL))
