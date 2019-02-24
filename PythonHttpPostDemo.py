#!/bin/usr/python

import urllib
import urllib2

base_url = 'http://localhost:8080/PythonHttp/postTest?'

httpHeaders = {'Accept-Language':'ko-kr','Cookie':'Cookie Value', 'Accept-Charset':'iso-8859-5'}

values = {'names' : 'kdh', 'email':'yeriel9159@gmail.com','telNumber':'010-1234-5678'}

data = urllib.urlencode(values)

request = urllib2.Request(url=base_url, headers=httpHeaders, data=data)
response = urllib2.urlopen(request)

print response.read()
