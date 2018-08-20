#used to make requests
import urllib.request
import urllib.parse


#x = urllib.request.urlopen('https://www.github.com')

#print(x.read())

url = 'https://www.tutorialspoint.com'
values = {' ': 'python programming tutorials'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)