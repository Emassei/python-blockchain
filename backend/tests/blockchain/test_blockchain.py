from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA
import pytest

def test_blockchain_instance():
    blockchain = Blockchain()
    assert blockchain.chain[0].hash == GENESIS_DATA['hash']


def test_add_block():
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.add_block(data)

    assert blockchain.chain[-1].data == data

@pytest.fixture
def blockchain_five_blocks():
    blockchain = Blockchain()

    for i in range(5):
        blockchain.add_block(i)
    return blockchain

def test_is_valid_chain(blockchain_five_blocks):
    Blockchain.is_valid_chain(blockchain_five_blocks.chain)

def test_is_valid_chain_bad_genesis(blockchain_five_blocks):
    blockchain_five_blocks.chain[0].hash = 'evil'

    with pytest.raises(Exception, match='genesis block must be valid'):
        Blockchain.is_valid_chain(blockchain_five_blocks.chain)


def test_replace_chain(blockchain_five_blocks):
    blockchain = Blockchain()
    blockchain.replace_chain(blockchain_five_blocks.chain)

    assert blockchain.chain == blockchain_five_blocks.chain


def test_replace_chain_not_longer(blockchain_five_blocks):
    blockchain = Blockchain()

    with pytest.raises(Exception, match='The incoming chain must be longer'):
        blockchain_five_blocks.replace_chain(blockchain.chain)

def test_replace_chain_bad_chain(blockchain_five_blocks):
    blockchain = Blockchain()
    blockchain_five_blocks.chain[1].hash = 'evil_hash'

    with pytest.raises(Exception, match='The incoming chain is invalid'):
        blockchain.replace_chain(blockchain_five_blocks.chain)
