import json
from eth_account import Account

from web3 import Web3

node_url = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(Web3.HTTPProvider(node_url))

link_token_contract = "0x84b9B910527Ad5C03A9Ca831909E21e236EA7b06"
pv_key = "0x4e9c990a047cfacd755f21b7f14423f524383e93fa4ade4e111c56caee5893f5"
ali_shams_address_wallet = "0xA437f0F7e43b22C6501ec90c5b4a7a0ad36be0C7"
recipient = "0x152B91011Fa3F3488D5b6d0619dcE317533685DB"
amount = web3.to_wei(1, "ether")

with open("/Users/mac/Desktop/pingi_task/user_authentication/wallet/link_abi.json") as abi_file:
    contract_abi = json.load(abi_file)


transaction = {
    "gas": 100000,
    "gasPrice": web3.eth.gas_price,  # Current GasPrice
    "nonce": web3.eth.get_transaction_count(ali_shams_address_wallet),
    "chainId": 97,
}
token_contract = web3.eth.contract(address=link_token_contract, abi=contract_abi)
build_transaction = token_contract.functions.transfer(recipient, amount).build_transaction(transaction)
signed_transaction = web3.eth.account.sign_transaction(build_transaction, pv_key)
web3.eth.send_raw_transaction(signed_transaction.raw_transaction)
