# Binance Futures CLI Trading Client

A robust, production-ready Python Command Line Interface (CLI) application built to execute and track orders on the Binance Futures USDⓈ-M Testnet. This client isolates credentials securely, performs runtime parameter validation, and maintains a persistent transaction ledger.
##  Features
* **Order Execution:** Fully supports automated `MARKET` and `LIMIT` risk-execution orders.
* **Security First:** Strict `.env` isolation ensures private API credentials never touch version control.
* **Transaction Ledger:** Automatic, millisecond-precision tracking of all outgoing order payloads and corresponding exchange response IDs.
---
## Prerequisites & System Requirements
* **Python Engine:** Python 3.8 or higher installed on your local system.
* **Binance Account:** An active Binance Futures Testnet account with generated API keys.
---
## Setup & Installation Steps

### 1. Structure the Project
Ensure your local project directory structure matches the clean layout below:
```text
binance_future_bot/
│
├── binance_bot.py      # Core API connection logic & transaction handling
├── cli.py              # Command-line interface orchestration
├── requirements.txt    # Application dependencies
├── .gitignore          # Version control protection shield
└── README.md           # Documentation (This file)
----------------------------------------------------------------------------
##---Create a private environment file named exactly .env in the root directory. Populate it with your testnet keys:
BINANCE_API_KEY=your_actual_testnet_api_key_here
BINANCE_API_SECRET=your_actual_testnet_secret_key_here

##---Install Dipendencies:
pip install -r requirements.txt
----------------------------------------------------------------------------
##---How to Run Examples
Launch the application by executing the CLI controller script via your terminal:
------>python cli.py

Executing a MARKET Order
------->python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Persistent Logging Structure
2026-05-21 18:30:31,041 - INFO - Sending Order Request Payload: {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'LIMIT', 'quantity': 0.02, 'price': 7000.0, 'timeInForce': 'GTC'}
2026-05-21 18:30:31,624 - INFO - Order Placement Success. Order ID: 13172298857
-----------------------------------------------------------------------------
