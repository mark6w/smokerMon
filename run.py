#!flask/bin/python
from app import app
app.run(debug=True)



'''
import urllib, json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/id')
def data():
    url = "http://192.168.10.108"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    print data
    return "grabbing data"


    

if __name__ == '__main__':
    app.run(debug=True)

'''
