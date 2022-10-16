from flask import Flask, render_template, request, flash
from googletrans import Translator

app = Flask(__name__)
app.secret_key = "ajkndh182uedcanq29_d92hj3"

@app.route("/translate")
def index():
    # this function is associated with the above route - the content that is accessed 
    flash("Ingresa una frase para traducir en ingles: ")
    return render_template("index.html")

@app.route("/convert", methods=["POST", "GET"])
def convert():
    translator = Translator()
    out = translator.translate(str(request.form['phrase_input']), dest="en")
    flash("La frase '"+ str(request.form['phrase_input']) + "' se traduce a: "+ out.text )
    
    return render_template("index.html")