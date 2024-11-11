from flask import Flask
from flask import render_template, request

app = Flask(__name__)

# Decorator
# The / meanas that as long as you call a function from flask, it will go here first
@app.route("/", methods = ["GET", "POST"])
def index():
    return(render_template('index.html'))

if __name__ == "__main__":
    app.run()