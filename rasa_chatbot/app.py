from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():


  if request.method != 'GET':
    pass
  else:
    val = str(request.args.get('text'))
    data = json.dumps({"sender": "Rasa","message": val})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
    res = res.json()
    val = res[0]['text']
    return render_template('index.html', val=val)

if __name__ == '__main__':
  app.run(debug=True)