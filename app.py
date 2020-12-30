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
        med = fetch_name(req)
        res = f'What do you want to know about {med}'.format(med) + '\n\n\n Uses \n Side Effects \n Precautions \n Interactions \n Overdose'
    return {'fulfillmentText': res}

def fetch_name(req):
    element = req.get('queryResult').get('parameters').get('medicine')     
    '''for key,value in df2.items():
            for k,v in value.items():
               if element==k:
                    return'''
    return element
# run the app
if __name__ == '__main__':
   app.run(threaded=True, port=5000)
