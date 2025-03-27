from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello, World!'

@app.route('/about')
def aboutUs():
    return aboutUs
if __name__ == '_main_':
    app.run(debug=True)