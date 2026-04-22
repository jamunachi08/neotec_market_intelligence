from neotec_market_intelligence.services.providers.base_provider import BaseProvider

class DemoProvider(BaseProvider):
    def get_price(self, symbol):
        return {'symbol': symbol, 'price': 100.0, 'currency': 'USD'}

    def get_fx(self, pair):
        return {'pair': pair, 'rate': 3.75}
