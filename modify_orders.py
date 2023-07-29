from fyers_api import fyersModel

client_id = "SPXXXXE7-100"
access_token = "eyJ0eXAiOiJK***.eyJpc3MiOiJhcGkuZnllcnM***.IzcuRxg4tnXiULCx3***"

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, log_path="/home/user/logs")

orderId = "8102710298291"
data = {
    "id":orderId, 
    "type":1, 
    "limitPrice": 61049, 
    "qty":1
}

response = fyers.modify_order(data=data)
print(response)