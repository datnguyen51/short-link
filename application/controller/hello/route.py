from .hello import HelloWorld


def controller_hello(api):
    api.add_resource(HelloWorld, '/')
