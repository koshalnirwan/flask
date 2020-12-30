# import flask dependencies
from flask import Flask, request, make_response, jsonify
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request

# initialize the flask app
app = Flask(__name__)

@app.route('/')
def index():
    return 'Medbot!'

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
        med= fetch_name(req)
        #res = f'What do you want to know about {med}'.format(med) + '\n\n\n Uses \n Side Effects \n Precautions \n Interactions \n Overdose'
        
        respond = about_med(req) 
        #med= fetch_name(req)
        url = 'https://www.webmd.com/drugs/2/search?type=drugs&query='+med
        requ = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
        response = urllib.request.urlopen( requ )
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        #if med in respond:
        rs = soup.find('div',{'id':'tab-1'})
        rs2 = rs.find_all('p')
        res = rs2[0].text
            #for i in range(2):
                #res = rs2[i].text
        
    return {'fulfillmentText': res}

def fetch_name(req):
    element = req.get('queryResult').get('parameters').get('medicine')     
    return element

def about_med(req):
    element2 = req.get('queryResult').get('parameters').get('user_select')     
    return element2
# run the app
if __name__ == '__main__':
   app.run(threaded=True, port=5000)
