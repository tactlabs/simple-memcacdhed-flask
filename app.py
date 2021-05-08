'''
Source:

Author: Raja CSP


'''
from flask import Flask, jsonify, request
import random
import json

# Local import
import mem_store 

app  = Flask(__name__)
PORT = 3009

    
'''
    http://localhost:3009/
'''
@app.route("/", methods = ["GET", "POST"])
def api_home():

    result = {
        "Greetings" : "Tactlabs welcomes you"
    }

    return jsonify(result)

'''
    http://localhost:3009/add/kevin?word=Toronto
'''
@app.route("/add/<username>", methods = ["GET"])
def api_add_userword(username):

    word = request.values.get('word')

    if(mem_store.is_key_available(username)):
        old_word = mem_store.get_from_local_store(username)

        word = old_word + "," + word

    mem_store.add_in_local_store(username, word)

    result = {
        "error_code" : 0,
        "error_message" : "NA",

        "username" : username,
        "word" : word
    }

    return jsonify(result)

'''
    http://localhost:3009/get/<username>
    http://localhost:3009/get/kevin
'''
@app.route("/get/<username>", methods = ["GET"])
def api_get_userword(username):

    word = mem_store.get_from_local_store(username)

    if(not word):
        result = {
            "error_code" : 8902,
            "error_message" : "Key Not Found",

            "username" : username,
        }

        return jsonify(result)

    result = {
        "error_code" : 0,
        "error_message" : "NA",

        "username" : username,
        "word" : word
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run( debug = True, host = "0.0.0.0", port = PORT)
    