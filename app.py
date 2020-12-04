# import flask dependencies
from flask import Flask, request, make_response, jsonify
import pandas as pd
# initialize the flask app
app = Flask(__name__)

df = pd.read_csv('New.csv',index_col=0)
df2 = df.to_dict()

@app.route('/')
def index():
    return 'Hello World!'

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)
   
    #fetch action from json
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error
        
    if action == 'get_results':
        res = 'This is a response from webhook for color.'
    elif action == 'put_results':
        res = 'This is a response from webhook for name.'
    elif action == 'set_results':
         res = fetch_name(req)
         
    return {'fulfillmentText': res}
def fetch_name(req):
    #element = req.get('queryResult').get('parameters').get('medicine').get('name')
    try:
        #element = input_params['medicine']
        element = req.get('queryResult').get('parameters').get('medicine').get('name')
        return element
    except:
        return 'Done'
    #for key,value in df2.items():
    #        for k,v in value.items():
    #           if element==k:
    #                return v
                
# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
   app.run(threaded=True, port=5000)
