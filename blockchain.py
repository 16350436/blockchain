import datetime
import hashlib
import json
from flask inport Flask, jsonify


class Blockchain:
    
    def __init___(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
    
    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
            'date': ''
            }
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
