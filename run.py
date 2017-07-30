#!flask/bin/python
from app import flask_api
import db_create
import db_seed
# This will run the application, change the debug do deliminate the nice error messages (every error would then result in an error 404 message)
if __name__ == "__main__":
    flask_api.run(debug=True, host='0.0.0.0', port=8000)  # Can change back debug
