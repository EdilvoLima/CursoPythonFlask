from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/<username>')
def hello_user_profile(username):
    #da um 'hello' ao user
    return 'Hello %s!' % username

if __name__ == '__main__':
    app.run(debug=True)
