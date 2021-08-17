import pytest
import requests
from api.settings import DOMAIN, ID_LENGTH


@pytest.mark.parametrize(
    "url, redirected_url",
    [
        ("www.helloworld.com", "http://www.helloworld.com"),
        ("http://www.helloworld.com", "http://www.helloworld.com"),
        ("https://www.helloworld.com", "https://www.helloworld.com"),
    ]
)
def test_url_shortener(api, url, redirected_url):
    response = api.post("/shorten_url", json={"url": url})
    assert requests.codes.ok == response.status_code

    shortened_url = response.json.get("shortened_url")
    assert shortened_url
    assert DOMAIN in shortened_url
    url_id = shortened_url.replace(DOMAIN, "")
    assert ID_LENGTH == len(url_id)

    response = api.get(f"/{url_id}")
    assert requests.codes.found == response.status_code
    assert redirected_url == response.headers.get("location")
