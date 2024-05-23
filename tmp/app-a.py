from flask import Flask

app = Flask(__name__)
count = 0

@app.route('/')
def hello():
    return 'return f'<h1 style="font-size: 10em;"> A </h1>''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
