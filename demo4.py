import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
response = urllib.request.urlopen('https://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))
