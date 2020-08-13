from flask import Flask

app = Flask(__name__)

@app.route("/") # / represent default page
def index(): # this function call decorator
    return "Hello, world!" # return string in 