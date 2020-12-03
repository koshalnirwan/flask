# import flask dependencies
from flask import Flask, request, make_response, jsonify
import pandas as pd

# initialize the flask app
app = Flask(__name__)

df = pd.read_csv("med_100.csv")
# default route
@app.route('/')
def index():
  return 'Medical World!'

#function for responses
def results():
  # build a request object
  req = request.get_json(force=True)  
  #fetch action from json
  action = req.get('queryResult').get('action')  
  if action == 'med_results':
    res = calculate_sales(req)
   
  #action = 'Hi, I just wanted to check'  
  #return a fulfillment response
  return {'fulfillmentText': res}
  
def calculate_sales(req):
  element = req.get('queryResult').get('parameters').get('medicine').get('name')  
  med_link  = df[df['lower']==element].values 
  result = med_link[0,1]
  return(result)
  
#create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
  # return response
  #return "Koshal Singh"
  #return make_response(jsonify(results()))
  return 'hello world'
#run the app
if __name__ == '__main__':
  app.run(threaded=True, port=5000)
