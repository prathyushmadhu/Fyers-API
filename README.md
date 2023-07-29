# Fyers-API
**Fyers API** provide integration with our in-house trading platform with which you can build your own cutomized trading applications. The API helps to place multiple orders (10  limit per day). This documentation is inspired from the original documentation of **FYERS-API**.

## 🔗 Links
[![Fyers API]()](https://api-docs.fyers.in/)

## Authorisation.py
This file extracts the authorisation key `auth_key` that is essential for getting an access key `access_token`.
- `client_id` : This is the  app_id which is received after app creation.
- `redirect_url` : User will be redirected to this page after successful login.
- `response_type` : (Default : "code") Gives the type of response in accordance with login status.
- `state` : Random value that will be returned in output console after successful login.

## access_token.py
This file returns `access_token` and `refresh_token`. `refresh_token` will expire in 15 days and can be used to generate a new `access_token`.
- `grant_type` : The value always and by default is "authorization_code"
- `appIdHash` : SHA-256 of api_id + app_secret
- `code` : auth_code from `authorisation.py`
