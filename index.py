from flask import Flask
from flask.ext.admin import Admin
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    admin = Admin(app)
    app.run()
