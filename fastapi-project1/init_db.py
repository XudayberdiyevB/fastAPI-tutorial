from app import models, database

from app.models import User, Item  # noqa

models.Base.metadata.create_all(bind=database.engine)
