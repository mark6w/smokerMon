from flask import render_template
from app import app
import urllib, json

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Mark'}  # fake user
    return render_template('index.html',
                          title='Home',
                            user=user)


@app.route('/id/')
def id():

    url = "http://192.168.10.108"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    variables = data['variables']
    print variables
    return '''
<html>
  <head>
    <title>Temperature Probe Page</title>
  </head>
  <body>
    <h1>''' + variables['name'] + '''</h1>
        <h2>Probe#1 = ''' + str(variables['probe1']) + ''' ''' + variables['probe1Status'] + '''
        <h2>Probe#2 = ''' + str(variables['probe2']) + ''' ''' + variables['probe2Status'] + '''
        <h3>Battery = ''' + str(variables['batterylvl']) + '''%
  </body>
</html>
'''

