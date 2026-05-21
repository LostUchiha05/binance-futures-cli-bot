from binance.client import Client
from binance.exceptions import BinanceAPIException
import logging
import os
from dotenv import load_dotenv
import time


logging.basicConfig(
    filename="Trading.log",
    level=logging.INFO,
    filemode='a',
    format = "%(asctime)s - %(levelname)s - %(message)s"
)
load_dotenv()
API_KEY = os.environ.get("API_Key")
SECRET_KEY = os.environ.get("Secret_Key")

if not API_KEY or not SECRET_KEY:
    logging.error("Initialization Failed Binance API Key missing from .env file")
    raise ValueError("Crirtical Error: Binance API keys missing from environment.Check yiour .env file")

def get_binance_client():
    bot_client = Client(API_KEY,SECRET_KEY,testnet=True)
    bot_client.API_URL = 'https://testnet.binance.vision/api'
    bot_client.FUTURES_URL = 'https://testnet.binancefuture.com'
    return bot_client
client = get_binance_client() 

def place_futurues_order(symbol:str,side:str,order_type:str,quantity:float,price:float = None):
        order_payload = {
            "symbol": symbol.upper(),
            "side":side.upper(),
            "type":order_type.upper(),
            "quantity":quantity
        }
        if order_type.upper() =="LIMIT":
            if price is None:
                error_msg = "Validation Error : 'price' parameter is missing but mandatory for LIMIT Orders"
                logging.warning(error_msg)
                return {"success":False,"error_msg": error_msg}
            
            order_payload["price"] = price
            order_payload["timeInForce"] = "GTC"

        
        logging.info(f"Sending Order Request Payload: {order_payload}")

        try:
            response = client.futures_create_order(**order_payload)
            order_ID = response.get('orderId')
            logging.info(f"Order Placement Success.Order ID:{order_ID}")

            return {
            "success": True,
            "data": response
            }
        
        except BinanceAPIException as e:
            error_msg = f"Binance Exchanage Error:{e.message}(Code {e.code})"
            logging.error(f"API Exception encounterd:{error_msg}")
            return {
                "success": False,
                "error_msg":f"Binance Exchange Error: {e.message} Code: {e.code}"
            }
        
        except Exception as e:
            error_msg = f"System/Network Error:{str(e)}"
            logging.error(f"Unexpected network or runtime failure:{error_msg}")
            return {
                "success":False,
                "error_msg":f"System/Network Error {str(e)}"
        }
