#!/usr/bin/env python3
"""
Flask app for user authentication service
"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()

@app.route("/")
def welcome():
    """Welcome message
    """
    return jsonify({"message": "Bienvenue"})

