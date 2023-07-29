from fyers_api import accessToken

client_id = "SPXXXXE7-100"
secret_key = "N********B"
redirect_uri = "https://trade.fyers.in/api-login/redirect-uri/index.html"
response_type = "code"
state = "sample_state"

session=accessToken.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri, 
    response_type=response_type
)

response = session.generate_authcode()
print(response)