import os

from pymongo import MongoClient

# Sentry
# SENTRY_DSN = os.environ.get("SENTRY_DSN", "")

SECRET_KEY = "SecretNoneShouldKnow"

# MongoDB
MONGODB_CONNECTION_STRING = os.environ.get("MONGODB_CONNECTION_STRING", "mongodb://localhost:27017/")
MONGODB_CLIENT = MongoClient(MONGODB_CONNECTION_STRING)
ID_LENGTH = 8
DOMAIN = os.environ.get("DOMAIN", "http://localhost:5000/")