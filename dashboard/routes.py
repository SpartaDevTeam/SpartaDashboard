from quart import render_template, url_for, redirect
from quart_discord.exceptions import AccessDenied, HttpException

from dashboard import app, discord_oauth, ipc_client
from dashboard.forms import ServerSettingsForm


async def get_common_bot_guilds(user):
    user_guilds = await user.fetch_guilds()
    bot_guild_ids = await ipc_client.request("get_guild_ids")
    common_guilds = [
        guild for guild in user_guilds if guild.id in bot_guild_ids
    ]
    return common_guilds


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
    return await discord_oauth.create_session()


@app.route("/logout")
async def logout():
    discord_oauth.revoke()
    return redirect(url_for("home"))


@app.route("/callback")
async def callback():
    try:
        await discord_oauth.callback()
    except AccessDenied or HttpException:
        return redirect(url_for("login"))

    return redirect(url_for("guild_list"))


@app.route("/serverlist")
async def guild_list():
    user = await discord_oauth.fetch_user()
    common_guilds = await get_common_bot_guilds(user)

    return await render_template(
        "guild_list.html", title="Servers", guilds=common_guilds
    )


@app.route("/server/<int:guild_id>")
async def guild_page(guild_id):
    user = await discord_oauth.fetch_user()
    common_guild_ids = [
        guild.id for guild in await get_common_bot_guilds(user)
    ]

    if guild_id not in common_guild_ids:
        return redirect(url_for("guild_list"))

    guild_info = await ipc_client.request("get_guild_info", guild_id=guild_id)
    return await render_template(
        "guild.html",
        title=guild_info["name"],
        guild_id=guild_id,
        guild_info=guild_info,
    )


@app.route("/server/<int:guild_id>/settings", methods=["GET", "POST"])
async def guild_settings(guild_id):
    return "<h1>Coming soon...</h1>"
