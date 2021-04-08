import os
from quart import Quart, url_for
from quart_discord import DiscordOAuth2Session

app = Quart(__name__)
app.config["SECRET_KEY"] = os.environ["SPARTA_SECRET_KEY"]
app.config["DISCORD_CLIENT_ID"] = int(os.environ["SPARTA_CLIENT_ID"])
app.config["DISCORD_CLIENT_SECRET"] = os.environ["SPARTA_CLIENT_SECRET"]
app.config["DISCORD_REDIRECT_URI"] = "https://127.0.0.1:5000/callback"

discord = DiscordOAuth2Session(app)

from dashboard import routes
