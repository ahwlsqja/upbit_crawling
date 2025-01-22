from config import get_settings
import ccxt



class ExchangeService:
    def __init__(self, api_key, secret_key):
        self.exchange = ccxt.upbit(config={
            'apiKey': api_key,
            'secret': secret_key,
            'enableRateLimit': True
        })
        
    def fetch_ticker(self, symbol):
        return self.exchange.fetch_ticker(symbol)
    
    
        