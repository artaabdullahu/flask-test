from flask import Flask, render_template
# from flask_bootstrap import Bootstrap

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")



if __name__ == '__main__':
    app.run(debug=True,port=5001)
