#importing flask
from flask import Flask, render_template
from flask import redirect
#importing feedparser for parsing rss feed
import feedparser
import pprint 
#importing regex module
import re

#initializing empty lists 
dlm = [] 
slm = []
tlm = []
mlm = []

fp=open("parsedfeed.py","w")
d=feedparser.parse("https://news.google.com/?output=rss")
# print(d)
#prettu print
pp=pprint.pformat(d,indent=4)

#writing the feed to file 
fp.write(pp)
#print(pp)
list = d['entries']
i=0
#loop for taking out all the links
pattern = "(?<=src=\").*?(?=\")"
pattern1 = "(?<=&url=\").*?(?=\")"
regex = re.compile(pattern)

m=len(list)
# matrix = [[0 for x in xrange(2)] for x in xrange(m)]
while(i<m):
	dict_of_list = list[i]

	#printing the list recovered from entries:
	# print(list)

	#formatting the list generated:
	rr=pprint.pformat(list,indent=4)

	#storing the formatted list into file:
	

	#printing the formated list
	# print(rr)

	#formatting dict_of_list:
	dl = pprint.pformat(dict_of_list['links'],indent=4)
	dlm.append(dl)
	sl = pprint.pformat(dict_of_list['summary'],indent=4)
	slm.append(sl)
	match = regex.search(sl)
	mlm.append(match.group(0))
	# matrix[i][1] = match.group(0)
	tl = pprint.pformat(dict_of_list['title'],indent=4)
	tlm.append(tl)
	# matrix[i][0] = tl
	#for extracting the 
	#printing the formatted links value inside dict_of_list:
	print("Article No {}".format(i))
	# print(i)
	print(dl)
	print(sl)
	i=i+1
	pass
print('printing dlm')
print(dlm)
app = Flask(__name__)

#Basic route
@app.route('/')

#default method to show
def index():
	return render_template('hmain.html', TLM = tlm, MLM = mlm)

#http://localhost:5000/yourname
# @app.route('/<name>')
# def user(name):
# 	return '<h1>Hello, %s!</h1>' % name

#http://localhost:5000/yourname
@app.route('/user/<name>')
def user(name):
	return redirect('http://www.google.com')

#route to login page
@app.route('/login')
def login():
	return render_template('login.html')


if __name__ == '__main__':
	app.run(debug=True)



