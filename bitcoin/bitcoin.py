import requests
import sys
import json

if len(sys.argv)<2:
    print("Missing command-line argument")
    sys.exit(1)
else:
    try:
        number = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
    response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o=response.json()
    usd_rate=o["bpi"]["USD"]["rate_float"]
    total_number = float(number*float(usd_rate))
    final_num="{:,.4f}".format(total_number)
    print(f"${final_num}")