from flask import Flask
from flask import render_template, request
import textblob
import google.generativeai as genai
import os

api = os.getenv("makersuite")
genai.configure(api_key = api)
model = genai.GenerativeModel("gemini-1.5-flash")

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

@app.route("/sentimentanalysis", methods = ["GET", "POST"])
def sentimentanalysis():
    satext = request.form.get("analysetext")
    return(render_template('sentimentanalysis.html'))
    
@app.route("/SA_results", methods = ["GET", "POST"])
def SA_results():
    satext = request.form.get("analysetext")
    if satext:
        results = textblob.TextBlob(satext).sentiment.polarity

        if results > 0:
            textresult = "Positive"
        elif results == 0:
            textresult = "Neutral"
        else:
            textresult = "Negative"

        return(render_template('SA_results.html', results = results, textresult = textresult))
    else:
        return(render_template('sentimentanalysis.html'))
    
@app.route("/genai", methods = ["GET", "POST"])
def genai():
    gentext = request.form.get("genaitext")
    if gentext:
        genairesponse = model.generate_content(gentext)

        return(render_template('genai.html', genairesponse = genairesponse.text))
    else:
        return(render_template('genai.html'))

if __name__ == "__main__":
    app.run()