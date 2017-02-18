from flask import Flask
app = Flask(__name__) # This is the Flask constructor; aka Flask application object

#A view function which is a decorator and a function
@app.route("/index") # When someone hits the /index url run the functions below. This line is called the decorator
def index():
    return "Hello World!"
# The main application which calls app.run
if __name__ == "__main__":
    app.run()