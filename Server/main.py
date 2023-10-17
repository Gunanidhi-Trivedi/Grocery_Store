from flask import Flask

app = Flask(__name__)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('success.html')
    else:
        return render_template('failure.html')

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run()
