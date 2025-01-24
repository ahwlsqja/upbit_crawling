import ccxt.pro as ccxtpro
import asyncio
import pprint
import sys

if sys.platform == 'win32':
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
     
async def main():
    exchange = ccxtpro.upbit()
    while True:
        ticker = await exchange.watch_ticker(symbol="BTC/KRW")
        pprint.pprint(ticker)

asyncio.run(main())