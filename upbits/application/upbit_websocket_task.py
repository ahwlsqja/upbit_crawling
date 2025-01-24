import ccxt.pro as ccxtpro
from dependency_injector.wiring import inject, Provide
import pprint
import asyncio


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

    async def watch_ticker(self, symbol: str):
        while True:
            try:
                ticker = await self.upbitWebSocket.watch_ticker(symbol)
                pprint.pprint(ticker)  # 가격 정보를 출력
            except Exception as e:
                print(f"Error fetching ticker: {e}")
                break  # 오류가 발생하면 루프 종료
            await asyncio.sleep(1)  # 1초 간격으로 요청