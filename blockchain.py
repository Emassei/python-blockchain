from block import Block
from pprint import pprint

class Blockchain:
    '''
    Blockchain is a public ledger of transactions.
    Implimented as a list of blocks - data sets of transactions.
    '''
    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self) -> str:
        return f'Blockchain: {self.chain}'

def main():
    blockchain = Blockchain()
    i = 0
    while(i < 10):
        i+=1
        blockchain.add_block(i)

    pprint(blockchain, width=1, indent=4)

    pprint(f'blockchain.py __name__: {__name__}')

if __name__ == '__main__':
    main()
