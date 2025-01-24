import sys
import asyncio
from fastapi import APIRouter
from dependency_injector.wiring import inject, Provide
from upbits.application.upbit_websocket_task import UpbitWebSocket
from containers import Container
from config import get_settings
import concurrent.futures

settings = get_settings()
api_key= settings.accesskey
secret_key = settings.secretkey

router = APIRouter(prefix="/upbitprice")

# upbit_websocket = UpbitWebSocket(api_key, secret_key)

# def start_receive_price_data(symbol: str):
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(upbit_websocket.watch_ticker(symbol))

# @router.on_event("startup")
# def startup_event():
#     executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
#     executor.submit(start_receive_price_data, 'BTC/USDT')  # 원하는 심볼로 변경

# @router.get("/")
# async def get_price():
#     return {"message": "WebSocket 클라이언트가 실행 중입니다."}

# @router.on_event("startup")
# @inject
# async def startup_event(upbit_websocket: UpbitWebSocket = Provide[Container.upbit_websocket]):
#     print(upbit_websocket)  # 인스턴스 확인
#     asyncio.create_task(upbit_websocket.watch_ticker("BTC/KRW"))  # 백그라운드에서 가격 정보 요청
