#from urllib import request
from flask import Flask   # Imported Flask library

#from flasgger import Swagger

app = Flask(__name__)     # Created constructor of the Flask



@app.route("/<name>")
def print_name(name):
    return f"Welcome {name} "


if __name__ == "__main__":
    
    app.run(host = "0.0.0.0", port = 8080, debug = True)