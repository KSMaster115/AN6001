from flask import Flask
from flask import render_template, request

app = Flask(__name__)

# Decorator
# The / meanas that as long as you call a function from flask, it will go here first
@app.route("/", methods = ["GET", "POST"])
def index():
    return(render_template('index.html'))

@app.route("/main", methods = ["GET", "POST"])
def main():
    name = request.form.get("q") # Thus is from the <form> in index
    return(render_template('main.html'))

if __name__ == "__main__":
    app.run()