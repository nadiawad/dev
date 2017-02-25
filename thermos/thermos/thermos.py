from datetime import datetime
import os
from flask import Flask, render_template, url_for,request,redirect, flash
from flask_sqlalchemy import SQLAlchemy

#from logging import DEBUG

from forms import BookmarkForm
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '.*\x99L2\x83\x08\xfc\x12\x06\xc5\xaa\xba\xdd5w\x03\xca\x180*\x90\x04E' #This was generated by running import os then os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'theroms.db')
db = SQLAlchemy(app)

#app.logger.setLevel(DEBUG)
bookmarks = []



#from models import Bookmark

def store_bookmark(url, description):
    bookmarks.append(dict(
        url = url,
        description = description,
        user = "Nadi",
        date = datetime.utcnow()
    ))

def new_bookmarks(num):
    return sorted(bookmarks, key = lambda bm: bm['date'], reverse=True)[:num]

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{}.{}.".format(self.firstname[0], self.lastname[0])

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="I am a title passed from view to template", text=["a", "b", "c"],
                           user=User("Nadi", "Awad"), new_bookmarks = new_bookmarks(5))

@app.route('/add',methods=['GET','POST'])
def add():
#    if request.method == "POST":
#        url=request.form['url']
#        store_bookmark(url)
#        app.logger.debug('stored url: '+url)
#        flash("Stored Bookmark: '{}'".format(url))
#        return redirect(url_for('index'))
#    return render_template('add.html')
    form= BookmarkForm()
    if form.validate_on_submit():
        url=form.url.data
        description=form.description.data
        store_bookmark(url, description)
        flash("Stored: '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500

if __name__ == '__main__':
    app.run(debug=True)

