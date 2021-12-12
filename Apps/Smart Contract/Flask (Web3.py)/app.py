from flask import Flask, render_template
import config
from config import *
from web3 import Web3

app = Flask(__name__)

@app.route("/")
def index():
    return "Ethereum Interface."

@app.route("/transaction/<hash>")
def transaction(hash):
    try:
        transaction = WEB3_HTTP_PROVIDER.eth.get_transaction(hash)
    except:
        transaction = None
    return render_template( "transaction.html", hash=hash, transaction=transaction)
