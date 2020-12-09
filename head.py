from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_
@app.route('/')

def index():
    return " Hello World"

if __name__ == '__main__':
    app.run(port = 5000 , debug = True)