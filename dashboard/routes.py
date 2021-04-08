from quart import render_template, url_for, redirect

from dashboard import app, discord


@app.route("/")
@app.route("/home")
async def home():
    return await render_template("home.html")


@app.route("/login")
async def login():
    return await discord.create_session()


@app.route("/callback")
async def callback():
    try:
        await discord.callback()
    except:
        return redirect(url_for("login"))

    user = await discord.fetch_user()
    return f"Hello {user}"
