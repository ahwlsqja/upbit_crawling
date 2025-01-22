import ccxt.pro as ccxtpro



class UpbitWebSocket:
    def __init__(self, api_key, secret_key):
        self.upbitWebSocket = ccxtpro.upbit(config={
            'apiKey': api_key,
            'secret': secret_key,
            'enableRateLimit': True,
            'options' : {
                'defaultType': 'future',
            }
        })