from flask import Flask, send_from_directory
from OpenSSL import SSL

global app
global context

app = Flask("web_server")
context = ("/etc/letsencrypt/live/dev.polychromus.com/fullchain.pem", "/etc/letsencrypt/live/dev.polychromus.com/privkey.pem")


@app.route("/<path:path>")
def index(path):
    if path == "":
        return send_from_directory("../frontend/public", "index.html")
    return send_from_directory("../frontend/public", path)


def run():
    app.run(host="0.0.0.0", port=443, ssl_context=context)
