from application import app, api
from application.controller import init_controller

init_controller(api)

if __name__ == '__main__':
    app.run(debug=True)
