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

@app.route('/webhook', methods=['GET','POST'])
# function for responses
def webhook():
    # build a request object
    req = request.get_json(force=True)
    query_result = req.get('queryResult')
    #fetch action from json
    action = req.get('queryResult').get('action')
        
    if action == 'get_results':
        res = 'This is a response from webhook for color.'
    elif action == 'put_results':
        res = 'This is a response from webhook for name.'
    elif action == 'set_results':
        res = fetch_name(req)
        #res = 'This is a response from webhook for medicine.'
    return {'fulfillmentText': res}
def fetch_name(req):
    #element = req.get('queryResult').get('parameters').get('medicine').get('name')
    try:
        element = req.get('queryResult').get('parameters').get('medicine')
    except:
        element = 'Done'
    return element
        
    #for key,value in df2.items():
    #        for k,v in value.items():
    #           if element==k:
    #                return v
                
# create a route for webhook
#@app.route('/webhook', methods=['POST'])
'''def webhook():
    # return response
    req = request.get_json(silent=True, force=True)
    query_result = req.get('queryResult')
    
    if query_result.get('action') == 'set_results':
        element = str(query_result.get('parameters').get('medicine'))
    #num2 = int(query_result.get('parameters').get('number1'))
    
    #fulfillmentText = element
    return {"fulfillmenttext":element}
    #return make_response(jsonify(results()))'''

# run the app
if __name__ == '__main__':
   app.run(threaded=True, port=5000)
