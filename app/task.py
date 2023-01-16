"""Example task accessing a protected endpoint

Execute with:

    python -m app.task
"""

from app.auth.client import client

character_id = ""

response = client.get(f"https://esi.evetech.net/latest/characters/{character_id}/location/?datasource=tranquility")
response.raise_for_status()
print(response.json())
