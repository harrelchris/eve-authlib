# Eve Authlib

Authlib example for Eve Online

## Dependencies

```shell
pip install -r requirements.txt
```

## `.env` File

Create a file called `.env` in the same directory as the `README.md` and `requirements.txt` files. Paste the following into that file. Update the 

```dotenv
# Update with your application values from 
# https://developers.eveonline.com/applications
CLIENT_ID=YourClientId
SECRET_KEY=YourSecretKey
SCOPES="your scopes as an space-delimited string"
CALLBACK_URL=http://localhost/callback

# optional
JWT_FILE_PATH=path\to\jwt.json
```

## Authorize

You must first authorize the application. A file `jwt.json` containing your auth token will be created. You do not need to reauthorize the application after the file is created. It will automatically manage refreshing and updating the token. 

```shell
python -m app.auth.authorize
```

## Example Task

Included is an example task. Run it with:

```shell
python -m app.task
```
