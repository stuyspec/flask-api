import os
# The base directory (DO NOT CHANGE, unless you know EXACTLY what you are doing)
basedir = os.path.abspath(os.path.dirname(__file__))

# The base directory for the database (DO NOT CHANGE, unless you know EXACTLY what you are doing)

SQLALCHEMY_DATABASE_URI = 'postgresql://test:test@localhost:5432/spec'

# More sql setup, reference previous comment
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# WTForms Config
# Enable the security on the forms
WTF_CSRF_ENABLED = True
# Secret key for the hashes
SECRET_KEY = 'THIS IS A SECRET KEY'
