import argparse
import sys
from binance_bot import place_futurues_order

def main():
    parser = argparse.ArgumentParser(
        description=""
        "CLI TOOL FOR PLACING ORDERS ON BINANCE FUTURE TESTNET"
    )

    parser.add_argument("-s","--symbol",type=str,required=True,help="eg.BTCUSDT")
    parser.add_argument("-d","--side",type=str,required=True,help="Buy Or Sell",choices=["BUY","SELL"])
    parser.add_argument("-t","--type",type=str,required=True,choices=["MARKET","LIMIT"],help="Market(Executes instantly at the best available current market price) or Limit(Executes only at your specified price (or better), waiting in the order book until that price is hit.)")
    parser.add_argument("-q","--quantity",type=float,required=True,help="Trading Volume/Quantity")
    parser.add_argument("-p","--price",type=float,default=None,help="Required strictly For LIMIT Orders")

    args = parser.parse_args()

    if args.type.upper() == "LIMIT" and args.price is None:
        print("CLI ERROR:You must Apply Price for LIMIT orders")
        sys.exit(1)

    print("\n=======================================")
    print("       ORDER REQUEST SUMMARY             ")
    print("=======================================")

    print(f"Target Symbol:{args.symbol.upper()}")
    print(f"Action/Side:{args.side.upper()}")
    print(f"Execution: {args.type.upper()}")
    print(f"Quantity:{args.quantity}")
    if args.price:
        print(f"• Limit Price:   ${args.price} USDT")
    print("=======================================\n")

    print("🛰️ Communicating with Binance Futures Testnet...")

    result = place_futurues_order(
        symbol=args.symbol,
        order_type=args.type,
        side=args.side,
        quantity=args.quantity,
        price=args.price
    )

    if result.get("success"):
        data = result["data"]
        print("\n SUCCESS:Order Processed Cleanly")
        print(f"Order ID:       {data.get('orderId')}")
        print(f"Status:         {data.get('status')}")
        print(f"Executed Qty:   {data.get('executedQty')}")


        avg_price = data.get('avgPrice')
        if avg_price and float(avg_price) > 0:
            print(f"Avg Price:    ${avg_price} USDT")
        else:
            print(f"Avg Price:    N/A (Order added to public book)")
        print("---------------------------------------")
    else:
            # Pull our custom error string or standard dictionary default lookup
        err = result.get("error_msg") or result.get("error_msg:")
        print(f"\n❌ FAILURE: {err}")

if __name__ == "__main__":
    main()