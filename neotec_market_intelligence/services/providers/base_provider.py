class BaseProvider:
    def get_price(self, symbol):
        raise NotImplementedError

    def get_fx(self, pair):
        raise NotImplementedError
