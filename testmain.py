#importing flask
from flask import Flask, render_template
from flask import redirect

import feedparser
import pprint 
dlm = [] 
slm = []

fp=open("parsedfeed.py","w")
d=feedparser.parse("http://timesofindia.indiatimes.com/rssfeedstopstories.cms")
# print(d)
#prettu print
pp=pprint.pformat(d,indent=4)

#writing the feed to file 
fp.write(pp)
#print(pp)
list = d['entries']
i=0
#loop for taking out all the links
m=len(list)
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
	
	return render_template('hmain.html', SLM = slm)

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



