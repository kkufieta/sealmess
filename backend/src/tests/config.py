import os
import http.client
import json

# Using the manually copied access tokens
# customer_access_token = os.environ.get('CUSTOMER_ACCESS_TOKEN')
# provider_access_token = os.environ.get('PROVIDER_ACCESS_TOKEN')
# owner_access_token = os.environ.get('OWNER_ACCESS_TOKEN')

# --- 
#   Attempted to grab access tokens automatically but
#   is out of scope for now.
# --- 
domain = os.environ.get('DOMAIN')
audience = os.environ.get('AUDIENCE')

payload = "{{\"client_id\":\"{}\",\"client_secret\":\"{}\",\"audience\":\"{}\",\"grant_type\":\"client_credentials\"}}"

headers = { 'content-type': "application/json" }

# Get the customer bearer token
customer_client_id = os.environ.get('CUSTOMER_CLIENT_ID')
customer_client_secret = os.environ.get('CUSTOMER_CLIENT_SECRET')
customer_payload = payload.format(customer_client_id,
                                  customer_client_secret,
                                  audience)

conn = http.client.HTTPSConnection(domain)
conn.request("POST", "/oauth/token", customer_payload, headers)
res = conn.getresponse()
data = res.read().decode("utf-8")
data = json.loads(data)
customer_access_token = data['access_token']
conn.close()

# Get the provider bearer token
provider_client_id = os.environ.get('PROVIDER_CLIENT_ID')
provider_client_secret = os.environ.get('PROVIDER_CLIENT_SECRET')
provider_payload = payload.format(provider_client_id,
                                  provider_client_secret,
                                  audience)
conn = http.client.HTTPSConnection(domain)
conn.request("POST", "/oauth/token", provider_payload, headers)
res = conn.getresponse()
data = res.read().decode("utf-8")
data = json.loads(data)
provider_access_token = data['access_token']
conn.close()

# Get the owner bearer token
owner_client_id = os.environ.get('OWNER_CLIENT_ID')
owner_client_secret = os.environ.get('OWNER_CLIENT_SECRET')
owner_payload = payload.format(owner_client_id,
                               owner_client_secret,
                               audience)


conn = http.client.HTTPSConnection(domain)
conn.request("POST", "/oauth/token", owner_payload, headers)
res = conn.getresponse()
data = res.read().decode("utf-8")
data = json.loads(data)
owner_access_token = data['access_token']
conn.close()

# Create the headers
customer_header = {"Authorization": "Bearer {}".format(customer_access_token)}
provider_header = {"Authorization": "Bearer {}".format(provider_access_token)}
owner_header = {"Authorization": "Bearer {}".format(owner_access_token)}