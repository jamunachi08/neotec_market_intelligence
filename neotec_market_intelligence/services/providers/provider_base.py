class ProviderBase:
    def search_instruments(self, query: str):
        raise NotImplementedError

    def get_quote(self, symbol: str):
        raise NotImplementedError

    def get_history(self, symbol: str, period: str = "1M"):
        raise NotImplementedError

    def get_fx_rate(self, base_currency: str, quote_currency: str):
        raise NotImplementedError

    def get_indicator(self, indicator_code: str):
        raise NotImplementedError
