#importing flask
from flask import Flask, render_template
from flask import redirect

import feedparser
import pprint 

d=feedparser.parse("https://news.google.com/?output=rss")
# print(d)
#prettu print
pp=pprint.pformat(d,indent=4)

#writing the feed to file 
#fp.write(pp)
print(pp)

app = Flask(__name__)

#Basic route
@app.route('/')

#default method to show


def index():
	return render_template('hmain.html')

#http://localhost:5000/yourname
# @app.route('/<name>')
# def user(name):
# 	return '<h1>Hello, %s!</h1>' % name

#http://localhost:5000/yourname
@app.route('/user/<name>')
def user(name):
	return redirect('http://www.google.com')




if __name__ == '__main__':
	app.run(debug=True)



