#!/usr/bin/python

import urllib
import urllib2

base_url = 'http://localhost:8080/PythonHttp/getTest?'

firstParam = 'firstParam=param1'
secondParam = '&secondParam=param2'

httpHeaders = {'Accept-Language':'ko-kr','Cookie':'Cookie Value', 'Accept-Charset':'iso-8859-5'}

requestURL = base_url + firstParam + secondParam

request = urllib2.Request(url=requestURL, headers=httpHeaders)
response = urllib2.urlopen(request)

print response.read()
