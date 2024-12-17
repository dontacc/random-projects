from eth_account import Account
import django
import os
import sys

sys.path.append("/Users/mac/Desktop/pingi_task/user_authentication")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_authentication.settings')
django.setup()

from wallet.models import Wallet
from authentication.models import User
from web3 import Web3

node_url = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(Web3.HTTPProvider(node_url))

pv_key = "0x4e9c990a047cfacd755f21b7f14423f524383e93fa4ade4e111c56caee5893f5"
ali_shams_address_wallet = "0xA437f0F7e43b22C6501ec90c5b4a7a0ad36be0C7"


class SendTransaction:

    @staticmethod
    def create_wallet():
        gas_price = web3.eth.gas_price

        account = Account.create()
        wallet_address = account.address
        pv_key = account.key.hex()
        Wallet.objects.get_or_create(
            user_id=User.objects.get(id=2).id,
            defaults={
                "wallet_address": wallet_address
            }
        )

    @staticmethod
    def sign_transaction():
        transaction_details = {
            "gas": 21000,
            "gasPrice": web3.eth.gas_price,  # Current GasPrice
            "to": "0x152B91011Fa3F3488D5b6d0619dcE317533685DB",
            "nonce": web3.eth.get_transaction_count(ali_shams_address_wallet),
            "value": web3.to_wei(0.001, 'ether'),
        }
        pv_key = "0x4e9c990a047cfacd755f21b7f14423f524383e93fa4ade4e111c56caee5893f5"  # sender
        signed_data = Account.sign_transaction(transaction_details, pv_key)
        return signed_data.raw_transaction

    @staticmethod
    def send_transaction():
        import urllib.parse
        signed_transaction = SendTransaction.sign_transaction()
        # json_data = {
        #     "module": "proxy",
        #     "action": "eth_sendRawTransaction",
        #     "hex": hex_signed,
        #     "apikey": "I7FXMT87NTR8E2S5J2N6X7CRJ7HFK1J32J",
        #     "chainId": 97,  # for testnet
        #     "gasPrice": Web3.to_wei(5, "gwei"),
        # }
        # params = urllib.parse.urlencode(json_data)
        # url = f"https://api.bscscan.com/api/?{params}"
        url = "https://data-seed-prebsc-1-s1.binance.org:8545/"
        web3 = Web3(Web3.HTTPProvider(url))
        web3.eth.send_raw_transaction(signed_transaction)


# SendTransaction.send_transaction()

SendTransaction.create_wallet()
