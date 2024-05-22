from flask import Flask

app = Flask(__name__)
count = 0

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/count')
def count_endpoint():
    global count
    count += 1
    return f'<h1 style="font-size: 3em;">Count: {count}</h1>'

@app.route('/count-view')
def count_endpoint():
    global count
    return f'<h1 style="font-size: 3em;">Count: {count}</h1>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)