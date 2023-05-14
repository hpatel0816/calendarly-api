from api import app


@app.route("/")
def home():
    return "Hello World!"


@app.route("/test", methods=["GET"])
def test():
    return "This is the db page!"