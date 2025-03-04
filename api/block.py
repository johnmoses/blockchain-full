""" 
Block
"""
import time
from hashable import crypto_hash
from util import hex_to_binary
from config import MINE_RATE

GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonce'
}

class Block:
    """ 
    A unit of storage for transactions
    """
    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}, '
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce})'
        )

    def to_json(self):
        """ 
        Serialize block
        """
        return self.__dict__

    @staticmethod
    def from_json(block_json):
        """ 
        Deserialize block
        """
        return Block(**block_json)

    @staticmethod
    def genesis():
        """ 
        Generate genesis or start block
        """
        return Block(**GENESIS_DATA)

    @staticmethod
    def adjust_difficulty(last_block, new_timestamp):
        """ 
        Calculate adjusted difficulty
        """
        if (new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty + 1
        if (last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1
        return 1

    @staticmethod
    def mine(last_block, data):
        """ 
        Mine a block 
        """

    @staticmethod
    def is_valid(last_block, block):
        """
        Validate a block
        """

def main():
    pass

if __name__ == '__main__':
    main()