from flask import Flask, request
from OpenSSL import SSL

global app
global context

app = Flask("github_webhooks")
context = ("/etc/letsencrypt/live/dev.polychromus.com/fullchain.pem", "/etc/letsencrypt/live/dev.polychromus.com/privkey.pem")


@app.route('/github', methods=["POST"])
def github_webhook():
    print(request.get_json())
    return "OK"


def run():
    app.run(host="0.0.0.0", port=8080, ssl_context=context)
