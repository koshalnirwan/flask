# import flask dependencies
from flask import Flask, request, make_response, jsonify
import pandas as pd

# initialize the flask app
app = Flask(__name__)

#df = pd.read_csv('https://raw.githubusercontent.com/koshalnirwan/flask/main/New.csv',error_bad_lines=False)

# default route
@app.route('/')
def index():
    return 'Hello World!'

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
        return {'fulfillmentText': 'hello'}
  
#def fetch_name(req):
#  element = req.get('queryResult').get('parameters').get('medicine').get('name')
#  #result  = list(df["Caution"][df['Name']==element].values)
#  return element
    
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
