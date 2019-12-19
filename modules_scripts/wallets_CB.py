import traceback

from coinbase.wallet.client import Client


# Get your primary coinbase account
class CoinBase():
    client = Client('1XdFWSCd0nwzXR1C', 'x0EHD2GbO3t2zmYTZJb6z0tQYh3X1MpN', api_version='2019-12-16')
    eth_id = "a5e426fd-e64d-50ac-ac7e-809e9c3a0fe8"
    ltc_id = "e1286da1-4770-537a-b4ca-980d4be5600f"
    btc_id = "850f7602-744f-5450-b208-95b64572620b"

    def create_address(self, coin_id):
        address = self.client.create_address(coin_id)["address"]
        print(address)
        return address

    def send_coin(self, address, coin, coin_amount,account_id):
        try:
            primary_account = self.client.get_account(account_id)

            tx = primary_account.send_money(to=address,
                                            amount=coin_amount,
                                            currency=coin)
            return True
        except Exception as e:
            print(traceback.format_exc())
