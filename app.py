from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
        return' Flask Dockerized'

@app.route('/ctof/<c>')
def ctof_func(c):
        return str(float(c) * (9 / 5) + 32)

if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0')
