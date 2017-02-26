from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    if request.method == "GET":
        _text = "Hi Nadi"
        return render_template("view.html", text=_text)
    elif request.method == "POST":
        text = request.form['text']
        _processed_text = text.upper()
        return render_template("secondPage.html", processed_text=_processed_text)

@app.route('/hello/<username>')
def hello_username(username):
    return 'Welcome %s' %username

if __name__ == '__main__':
    app.run()