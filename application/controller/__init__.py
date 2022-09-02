from application.controller.hello.route import controller_hello
from application.controller.user.route import controller_user


def init_controller(api):
    controller_hello(api)
    controller_user(api)
