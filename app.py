from flask import Flask, request

app = Flask(__name__)

@app.route('/home')
def index():
    return 'Hello Flask1'

@app.route('/users/<user_id>',methods = ['GET','POST',
                                         'PUT','DELETE'])
def parameter(user_id):
    if request.method =='GET':
        return 'GET method'

    elif request.method =='POST':
        data = request.form
        return data

    elif request.method =='PUT':
        return 'PUT method'
    elif request.method == 'DELETE':
        return 'DELETE method'
    else:
        return "Not an allowed method"



app.run(host='0.0.0.0',
        port=81) #0.0.0.0 is local host.