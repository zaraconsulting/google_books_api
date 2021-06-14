from . import bp as main
from flask import render_template, redirect, url_for, jsonify, request
import requests

@main.route('/')
def index():
    context = dict()
    return render_template('main/index.html', **context)

@main.route('/google_books_api', methods=['GET'])
def google_books_api():
    data = requests.get('https://www.googleapis.com/books/v1/volumes?q=quilting').json()
    # print(data)
    return jsonify(data)
    # return jsonify( data )