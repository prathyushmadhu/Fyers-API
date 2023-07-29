from fyers_api import fyersModel

client_id = "SPXXXXE7-100"
access_token = "eyJ0eXAiOiJK***.eyJpc3MiOiJhcGkuZnllcnM***.IzcuRxg4tnXiULCx3***"

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, log_path="/home/user/logs")

data = {
    "symbol":"NSE:SBIN-EQ",
    "resolution":"D",
    "date_format":"0",
    "range_from":"1622097600",
    "range_to":"1622097685",
    "cont_flag":"1"
}

response = fyers.history(data=data)
print(response)