from url_shortener import create_app
from url_shortener.extensions import db
from url_shortener.models import Link

db.create_all(app=create_app())
