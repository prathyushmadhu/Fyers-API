from fyers_api import fyersModel

client_id = "SPXXXXE7-100"
access_token = "eyJ0eXAiOiJK***.eyJpc3MiOiJhcGkuZnllcnM***.IzcuRxg4tnXiULCx3***"

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, log_path="/home/user/logs")

data = {
     "symbol":"NSE:SBIN-EQ",
     "qty":1,
     "type":2,
     "side":1,
     "productType":"INTRADAY",
     "limitPrice":0,
     "stopPrice":0,
     "validity":"DAY",
     "disclosedQty":0,
     "offlineOrder":"False",
 }

response = fyers.place_order(data=data)
print(response)