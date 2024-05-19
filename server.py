from flask import Flask, url_for, request, redirect, abort 

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from PythonAnywhere"

if __name__ == "__main__": 
    app.run(debug=True)