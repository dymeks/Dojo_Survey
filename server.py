from flask import Flask, render_template,request,redirect
app = Flask(__name__)

@app.route('/')
def displayLandingPage():
	return render_template('index.html')

@app.route('/result',methods=['POST'])
def displayFormInformation():
	print request.form
	name = request.form['name']
	dojo_location = request.form['location']
	favorite_language = request.form['favorite_language']
	comment = ''
	print 'Location: ' + dojo_location
	print 'Language' + favorite_language
	if(len(request.form['comment']) > 0):
		comment = request.form['comment']
	
	
	print 'comment ' + comment	
	# return render_template('result.html',name=request.form(),dojo_location,favorite_language,comment)
	return render_template('result.html',name=name,dojo_location=dojo_location,favorite_language=favorite_language,comment = comment)	 
app.run(debug=True)
