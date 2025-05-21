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

@app.route('/keygen')
def keygen():
    key = Fernet.generate_key()
    return f"Voici votre clé : {key.decode()}"

@app.route('/encrypt/<string:valeur>/<string:key>')
def encryptage(valeur, key):
    key_bytes = key.encode()
    valeur_bytes = valeur.encode()
    f = Fernet(key_bytes)
    token = f.encrypt(valeur_bytes)
    return f"Valeur encryptée : {token.decode()}"

@app.route('/decrypt/<string:valeur>/<string:key>')
def decryptage(valeur, key):
    key_bytes = key.encode()
    valeur_bytes = valeur.encode()
    f = Fernet(key_bytes)
    token = f.decrypt(valeur_bytes)
    return f"Valeur decryptée : {token.decode()}"
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)

# test
