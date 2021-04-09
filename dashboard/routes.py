from quart import render_template, url_for, redirect
from quart_discord.exceptions import AccessDenied, HttpException

from dashboard import app, discord, ipc_client


@app.route("/")
@app.route("/home")
async def home():
    return await render_template("home.html")


@app.route("/about")
async def about():
    return "<h1>Coming soon...</h1>"


@app.route("/features")
async def features():
    return "<h1>Coming soon...</h1>"


@app.route("/login")
async def login():
    return await discord.create_session()


@app.route("/logout")
async def logout():
    discord.revoke()
    return redirect(url_for("home"))


@app.route("/callback")
async def callback():
    try:
        await discord.callback()
    except AccessDenied or HttpException:
        return redirect(url_for("login"))

    return redirect(url_for("guild_list"))


@app.route("/serverlist")
async def guild_list():
    user = await discord.fetch_user()
    user_guilds = await user.fetch_guilds()
    bot_guild_ids = await ipc_client.request("get_guild_ids")
    common_guilds = [
        guild for guild in user_guilds if guild.id in bot_guild_ids
    ]

    return await render_template(
        "guild_list.html", title="Servers", guilds=common_guilds
    )
