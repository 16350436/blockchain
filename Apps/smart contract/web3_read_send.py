from web3 import Web3

ganache_url ="http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0xB48447F753a2fc50D6edc05f5a318abCA1aa9791"
private_key = "16369b50abb1e462bebef52b5fb4593422b47cf9532f0793999399614ead64dc"

account_2 = "0x8F044aE2C83FB5b19cDC4F23fd207d2613334817"

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
