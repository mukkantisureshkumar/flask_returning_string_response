from flask import Flask

Flask_Application_Instance=Flask(__name__)

@Flask_Application_Instance.route('/suresh') #here inside suffix is written first provide slash the name of the fun in django fun name the slash 
def suresh():
    return '''<enter><h1>the all type of operations are take care by flask application instance
              like views,url(in flask we call url as rootings),models,forms,running the server and in flask 
              all type of code are written in one file only we dont have here views urls models forms 
              httpresponse also handled by flask application instance</h1></center>'''

Flask_Application_Instance.run(debug=True) #is used for running server
