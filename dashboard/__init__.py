import os
from quart import Quart
from quart_discord import DiscordOAuth2Session
from discord.ext import ipc

app = Quart(__name__)
app.config["SECRET_KEY"] = os.environ["SPARTA_SECRET_KEY"]
app.config["DISCORD_CLIENT_ID"] = int(os.environ["SPARTA_CLIENT_ID"])
app.config["DISCORD_CLIENT_SECRET"] = os.environ["SPARTA_CLIENT_SECRET"]
app.config["DISCORD_REDIRECT_URI"] = "http://127.0.0.1:5000/callback"

discord = DiscordOAuth2Session(app)
ipc_client = ipc.Client(secret_key=os.environ["SPARTA_SECRET_KEY"])


@app.context_processor
def inject_stage_and_region():
    return dict(discord=discord)


from dashboard import routes
