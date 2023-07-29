from fyers_api import fyersModel

client_id = "SPXXXXE7-100"
access_token = "eyJ0eXAiOiJK***.eyJpc3MiOiJhcGkuZnllcnM***.IzcuRxg4tnXiULCx3***"

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, log_path="/home/user/logs")

data = {
    "symbols":"NSE:SBIN-EQ,NSE:HDFC-EQ"
}

response = fyers.quotes(data=data)
print(response)