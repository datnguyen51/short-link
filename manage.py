from application import app, api
from application.controller import init_controller
from application.database import init_database


init_controller(api)
init_database(app)

if __name__ == '__main__':
    app.run(debug=True)
