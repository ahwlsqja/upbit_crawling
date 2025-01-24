from dependency_injector import containers, providers
from config import get_settings
from upbits.application.upbit_obj_service import ExchangeService
from upbits.application.upbit_websocket_task import UpbitWebSocket

class Container(containers.DeclarativeContainer):
    settings = get_settings()
    
    exchange_service = providers.Factory(
        ExchangeService,
        api_key=settings.accesskey,
        secret_key=settings.secretkey
    )
    
    upbit_websocket = providers.Factory(
        UpbitWebSocket,
        api_key=settings.accesskey,
        secret_key=settings.secretkey
    )



    