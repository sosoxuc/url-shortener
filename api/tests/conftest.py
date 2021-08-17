import pytest
import mongomock

import api.settings

api.settings.MONGODB_CLIENT = mongomock.MongoClient()

@pytest.yield_fixture
def api():
    from api import app

    with app.app.test_client() as client:
        yield client
