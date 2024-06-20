import hashlib
import json
from time import time


class Block(object):
    def __init__(self):
        self.chain = []
        self.new_transactions = []
        self.count = 0
        self.new_block(previous_hash="No previous Hash. Since this is the first block.")

    def new_block(self, previous_hash=None):

        block = {
            'Block No': self.count,
            'timestamp': time(),
            'transactions': self.new_transactions or 'No Transactions First Genesis Block',
            'gasfee': 0.1,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
            
        }
        self.new_transactions = []
        self.count = self.count + 1
        self.chain.append(block)
        


        return block

    def last_block(self):
        return self.chain[-1]

    def transaction(self, sender, recipient, amount):
        sender_encoder = hashlib.sha256(sender.encode())
        sender_hash = sender_encoder.hexdigest()
        recipient_encoder = hashlib.sha256(recipient.encode())
        recipient_hash = recipient_encoder.hexdigest()

        transaction_data = {
            'sender': sender_hash,
            'recipient': recipient_hash,
            'amount': amount
        }
        self.new_transactions.append(transaction_data)
        return self.last_block

    def hash(self, block):
        string_object = json.dumps(block)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        # self.chain.append(("Current Hash: ", hex_hash))
        block['Current_hash'] = hex_hash
        return hex_hash


blockchain = Block()

transaction4 = blockchain.transaction("Omkar", "Mike", '5 ETH')
transaction5 = blockchain.transaction("Mike", "Satoshi", '1 ETH')
blockchain.new_block()

# Write Task 01 code from below
Blockchain_data = blockchain.chain
number_of_blocks = len(Blockchain_data)
print("Number of blocks in blockchain: ", Blockchain_data)

# Write Task 02 code from below
print("Previous hash code of Genesis Block: ", blockchain.chain[0]['previous_hash'])
print("Current hash code of Genesis Block: ", blockchain.chain[1]['current_hash'])
print("Previous hash code of 1st block: ", blockchain.chain[1]['current_hash'])

# Write Task 03 code from below
if(blockchain.chain[0]['previous_hash'] == blockchain.chain[1]['current_hash']) :
    print("The Hash of Current Block matches with Previous Block... Hence Transaction Verified...")
else: 
    print("Oh...No...The Hash of Current Block does not match with Previous Block")




