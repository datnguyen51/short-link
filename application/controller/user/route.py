from .register import Registration


def controller_user(api):
    api.add_resource(Registration, '/user_registration')
