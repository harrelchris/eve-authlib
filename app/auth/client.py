import json
import pathlib

from authlib.integrations.requests_client import OAuth2Session

from app.auth.config import CALLBACK_URL, CLIENT_ID, JWT_FILE_PATH, SCOPES, SECRET_KEY, TOKEN_URL


def fetch_token(*a, **k) -> dict:
    if not pathlib.Path(JWT_FILE_PATH).exists():
        return {}

    with open(JWT_FILE_PATH, "r") as file:
        return json.load(file)


def update_token(token, *a, **k) -> None:
    with open(JWT_FILE_PATH, "w") as file:
        json.dump(token, file)


client = OAuth2Session(
    client_id=CLIENT_ID,
    client_secret=SECRET_KEY,
    scope=SCOPES,
    redirect_uri=CALLBACK_URL,
    fetch_token=fetch_token,
    update_token=update_token,
    token=fetch_token(),
    token_endpoint=TOKEN_URL,
)
