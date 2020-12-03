# import flask dependencies
from flask import Flask, request, make_response, jsonify
import pandas as pd

# initialize the flask app
app = Flask(__name__)

#df = pd.read_csv('https://github.com/koshalnirwan/flask/blob/main/New.csv')

# default route
@app.route('/')
def index():
    return """<iframe width="350" height="430" allow="microphone;" src="https://console.dialogflow.com/api-client/demo/embedded/9e85e733-ec1c-461f-aaba-2e4d7ed71fd2"></iframe>"""
    #return 'Hello World!'

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')
    
    if action == 'get_results':
        return {'fulfillmentText':'This is a response from webhook for color.'}
    elif action == 'put_results':
        return {'fulfillmentText':'This is a response from webhook for name.'}
    elif action == 'set_results':
        #res = fetch_name(req)
        return {'fulfillmentText': 'Hello'}
  
#def fetch_name(req):
#  element = req.get('queryResult').get('parameters').get('medicine').get('name')
#  result  = list(df["Caution"][df['Name']==element].values)
#  return(result)
    
# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
   app.run()

'''# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
  return 'hello world'

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)'''
