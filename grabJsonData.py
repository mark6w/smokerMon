
import urllib, json
url = "http://192.168.10.108"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data
