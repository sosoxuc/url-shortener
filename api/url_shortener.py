import random
import string

from flask import redirect, abort, request
from flask_restx import Namespace, Resource, fields

from api.settings import MONGODB_CLIENT, DOMAIN, ID_LENGTH

db = MONGODB_CLIENT.url_shortener
api = Namespace("", description="URL shortener endpoints")

url_shortener_request_model = api.model(
    "UrlShortenerRequestModel",
    {
        "url": fields.String(description="Url to shorten", required=True),
    }
)

url_shortener_response_model = api.model(
    "UrlShortenerResponseModel",
    {
        "shortened_url": fields.String(description="Shortened URL"),
    }
)


@api.route("/shorten_url")
class Shorten(Resource):
    @api.expect(url_shortener_request_model)
    @api.marshal_with(url_shortener_response_model)
    def post(self):
        data = request.json
        url = data.get("url")
        assert url
        _id = ''.join(random.choices(string.ascii_letters + string.digits, k=ID_LENGTH))
        db.urls.insert_one({"_id": _id, "url": url})
        return {"shortened_url": f"{DOMAIN}{_id}"}


@api.route("/<string:url_id>")
class Redirect(Resource):
    def get(self, url_id):
        data = db.urls.find_one({"_id": url_id})
        print(data)
        if not data:
            abort(404)
        url = data.get("url")
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        return redirect(url)
