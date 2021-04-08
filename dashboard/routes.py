from quart import render_template, url_for

from dashboard import app


@app.route("/")
@app.route("/home")
async def home():
    return "Hello"


@app.route("/callback")
async def callback():
    return "Coming soon..."
