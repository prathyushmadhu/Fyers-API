from fyers_api import fyersModel

client_id = "SPXXXXE7-100"
access_token = "eyJ0eXAiOiJK***.eyJpc3MiOiJhcGkuZnllcnM***.IzcuRxg4tnXiULCx3***"

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, log_path="/home/user/logs")

data = {
    "symbol":"MCX:SILVERMIC20NOVFUT",
    "positionSide":1,
    "convertQty":1,
    "convertFrom":"INTRADAY",
    "convertTo":"CNC"
}

response = fyers.convert_position(data=data)
print(response)