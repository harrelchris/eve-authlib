import sys
import urllib.parse
import webbrowser

from app.auth.client import client
from app.auth.config import AUTHORIZATION_URL, TOKEN_URL
from app.auth.server import capture_callback

uri, state = client.create_authorization_url(AUTHORIZATION_URL)
webbrowser.open(uri)

authorization_response = capture_callback()
authorization_response_state = urllib.parse.parse_qs(urllib.parse.urlparse(authorization_response).query)["state"][0]

if authorization_response_state != state:
    sys.exit("Received invalid state")

token = client.fetch_token(TOKEN_URL, authorization_response=authorization_response)
client.update_token(token)
