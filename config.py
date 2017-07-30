import os

DB_USER = os.getenv("FLASK_DB_USER") or "stuy_spec"
DB_PASSWORD = os.getenv("FLASK_DB_PASSWORD") or "stuyspecflaskdb"
DB_HOST = os.getenv("FLASK_DB_HOST") or "localhost"
DB_PORT = os.getenv("FLASK_DB_PORT") or "5432"
DB_NAME = os.getenv("FLASK_DB_NAME") or "stuy-spec-dev"

# The base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# The base directory for the database
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME
)


# More sql setup, reference previous comment
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# WTForms Config
# Enable the security on the forms
WTF_CSRF_ENABLED = True
# Secret key for the hashes
SECRET_KEY = os.getenv("FLASK_SECRET_KEY") or \
             '045fe0b3a26310e780f545ccb056742535e2adcbf2b2d89' \
             'f075355e727957f0d13a2a8d258179c3a2f0e89f508f76' \
             '2bdd487c8a70d58a674cbae15a73f6abbed'
