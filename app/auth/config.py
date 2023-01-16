import os
import pathlib

import dotenv

BASE_DIR = pathlib.Path(__file__).parent.parent

dotenv.load_dotenv()

AUTHORIZATION_URL = "https://login.eveonline.com/v2/oauth/authorize/"
TOKEN_URL = "https://login.eveonline.com/v2/oauth/token"

CLIENT_ID = os.environ["CLIENT_ID"]
SECRET_KEY = os.environ["SECRET_KEY"]
SCOPES = os.environ["SCOPES"]
CALLBACK_URL = os.environ["CALLBACK_URL"]

JWT_FILE_PATH = os.environ.get("JWT_FILE_PATH", BASE_DIR.parent / "jwt.json")
