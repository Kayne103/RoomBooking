# By Kayne
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

"""
Root endpoint.
It doesnt matter in the API design.
"""
@app.route('/')
def index():
    """
    This is the root endpoint.
    :return: The landing page 🛬 of the platform.
    """
    return render_template('index.html')

if __name__ == '__main__':

    app.run(threaded=True, port=5000)