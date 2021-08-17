from flask import Blueprint
from flask import Flask
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from api import settings
from api.url_shortener import api as url_shortener_api

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

app.config["JSON_AS_ASCII"] = False
app.config["SWAGGER_UI_DOC_EXPANSION"] = "list"
app.config["RESTPLUS_MASK_SWAGGER"] = False
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

blueprint = Blueprint("url-shortener-api", __name__, url_prefix="/")

api = Api(
    blueprint,
    version="1.0",
    title="URL shortener API",
    description="The API provides ability to shorten your URLs.",
    doc="/docs",
)

api.add_namespace(url_shortener_api)

app.register_blueprint(blueprint, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
