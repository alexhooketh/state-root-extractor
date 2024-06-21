# PoC of the logic in python

from web3 import Web3
import rlp
from eth_utils import decode_hex

web3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

def fetch_block_header(block):

    header = [
        block.parentHash,
        block.sha3Uncles,
        decode_hex(block.miner),
        block.stateRoot,
        block.transactionsRoot,
        block.receiptsRoot,
        block.logsBloom,
        block.difficulty,
        block.number,
        block.gasLimit,
        block.gasUsed,
        block.timestamp,
        block.extraData,
        block.mixHash,
        block.nonce,
        block.baseFeePerGas,
        block.withdrawalsRoot
    ]

    return rlp.encode(header)

def extract_state_root(block_hash, header):
    assert web3.keccak(header) == block_hash
    return header[91:123]

block = web3.eth.get_block(20134772)
header = fetch_block_header(block)

state_root = extract_state_root(block.hash, header)
assert state_root == block.stateRoot