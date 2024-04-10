# imports
from flask import Flask 
from extensions.extension import api, db
from flask_security import Security
from configs.config import DevelopmentConfig
from models.user_model import user_datastore

# import resources
from api.auth_resource import ns_auth


# initialize app
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# initialize extensions
db.init_app(app)

security = Security(app, user_datastore)
api.init_app(app)



# register namespaces
api.add_namespace(ns_auth)


if __name__ == '__main__':
    app.run(debug=True)