from api import create_app


@create_app.route("/")
def home():
    return "Hello World!"


@create_app.route("/test", methods=["GET"])
def test():
    return "This is the db page!"