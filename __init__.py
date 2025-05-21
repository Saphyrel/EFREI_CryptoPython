from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3

app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')

#key = Fernet.generate_key()
#f = Fernet(key)

@app.route('/encrypt/<string:valeur>/<string:key>')
def encryptage(valeur, key):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = key.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt/<string:valeur>/<string:key>')
def decryptage(valeur, key):
    valeur_bytes = valeur.encode()
    token = key.decrypt(valeur_bytes)
    return f"Valeur décryptée : {token.decode()}"
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
