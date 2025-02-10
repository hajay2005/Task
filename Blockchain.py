import hashlib
import time

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}"
        return hashlib.sha256(block_data.encode()).hexdigest()
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), transactions, previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False
            
        return True
class Block:
    def __init__(self, index, transactions, previous_hash, difficulty=2):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.mine_block(difficulty)

    def mine_block(self, difficulty):
        while True:
            self.nonce += 1
            new_hash = self.calculate_hash()
            if new_hash[:difficulty] == "0" * difficulty:
                return new_hash

    def calculate_hash(self):
        block_data = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_data.encode()).hexdigest()
def tamper_block(blockchain, block_index, new_data):
    blockchain.chain[block_index].transactions = new_data

blockchain = Blockchain()
blockchain.add_block("Transaction 1")
blockchain.add_block("Transaction 2")

print("Blockchain valid before tampering:", blockchain.is_chain_valid())

tamper_block(blockchain, 1, "Hacked Transaction")
print("Blockchain valid after tampering:", blockchain.is_chain_valid())

def print_blockchain(blockchain):
    for block in blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}, Prev: {block.previous_hash}, Transactions: {block.transactions}")

print_blockchain(blockchain)
