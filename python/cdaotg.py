#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import webapp2
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

def sort(a,b):
	c=''
	i=0
	while i<len(a) or i<len(b):
		if i<len(a):
			c=c+a[i]
		if i<len(b):	
			c=c+b[i]
		i+=1
	return c

class BaseHandler(webapp2.RequestHandler):
	def render(self,html,values={}):
		template=JINJA_ENVIRONMENT.get_template(html)
		self.response.write(template.render(values))

class MainPage(BaseHandler):
	def get(self):
		self.response.headers['Content-Type']='text/html; charset=UTF-8'
		self.response.write('<html>\
		 		<head>\
		 			<meta charset="UTF-8">\
		 			<title>パタトクカシーー</title>\
		 		</head>\
		 		<body>\
		 			<form action="/" method="GET">\
		 			<p> <input type="text" name="a"/> </p>\
		 			<p> <input type="text" name="b"/> </p>\
		 			<p> <button type="submit">submit</button> </p>\
		 			</form>\
		 		</body>\
		 		</html>')
		c=''
		a=self.request.get('a')
		b=self.request.get('b')
		c=sort(a,b)
		value={
			'data':c
		}
		if c!='':
			self.response.headers['Content-Type']='text/html;; charset=UTF-8'
			self.render('result.html',value);

app=webapp2.WSGIApplication([
	('/',MainPage),
], debug=True)

