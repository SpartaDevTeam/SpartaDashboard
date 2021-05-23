import os
import dotenv
from quart import Quart, flask_patch
from quart_discord import DiscordOAuth2Session
from discord.ext import ipc

dotenv.load_dotenv()

app = Quart(__name__)
app.config["SECRET_KEY"] = os.environ["SPARTA_SECRET_KEY"]
app.config["DISCORD_CLIENT_ID"] = int(os.environ["SPARTA_CLIENT_ID"])
app.config["DISCORD_CLIENT_SECRET"] = os.environ["SPARTA_CLIENT_SECRET"]
app.config["DISCORD_REDIRECT_URI"] = os.environ["SPARTA_CALLBACK_URI"]

discord_oauth = DiscordOAuth2Session(app)
ipc_client = ipc.Client(
    host=os.environ["SPARTA_IPC_HOST"],
    secret_key=os.environ["SPARTA_SECRET_KEY"],
)


@app.context_processor
def inject_discord_session():
    return dict(discord_oauth=discord_oauth)


from dashboard import routes
