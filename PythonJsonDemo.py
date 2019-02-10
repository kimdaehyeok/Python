#!/usr/bin/python
#-*- coding: utf-8 -*-

import json

httpResponse = { "response": {
  "header": {
    "resultCode": "00",
    "resultMsg": "정상"
  },
  "body": {
    "items": [
      {
        "bizno": "6168122531",
        "corpNm": "주식회사청마토건",
        "engCorpNm": "cheongma CO.LTD",
        "opbizDt": "1997-12-15 00:00:00",
        "rgnCd": "42130",
        "rgnNm": "강원도 원주시",
        "zip": "26433",
        "adrs": "강원도 원주시 남산로48번길",
        "dtlAdrs": "29, 1층(원동)",
        "telNo": "***-****-****",
        "faxNo": "033-764-2277",
        "cntryNm": "대한민국",
        "hmpgAdrs": "",
        "mnfctDivCd": "03",
        "mnfctDivNm": "공급",
        "emplyeNum": "7",
        "corpBsnsDivCd": "11000",
        "corpBsnsDivNm": "물품,공사,-,-,-",
        "hdoffceDivNm": "본사",
        "rgstDt": "2001-08-22 00:00:00",
        "chgDt": "2019-01-23 17:34:29",
        "esntlNoCertRgstYn": "N",
        "ceoNm": "조아름"
      }
    ],
    "numOfRows": 10,
    "pageNo": 1,
    "totalCount": 1
  }
}}

print '#################### JSON Encoding Start ########################'

#Convert Python Object(Dictionary, List, Tuple etc) To String, Json Encoding
jsonString = json.dumps(httpResponse, indent=4)

print '>>>>>> json.dumps type is : ' + str(type(jsonString)) #Type is str

print '>>>>>> Http response type is {type}'.format(type = type(httpResponse)) #Http Response type is dict

print '>>>>>> header is : ', httpResponse['response']['header']

print '>>>>>> items is : ', httpResponse['response']['body']['items']

#type is list
print '>>>>>> item type is ', type(httpResponse['response']['body']['items'])

for element in httpResponse['response']['body']['items']:
	print '>>>>>> Get Item Value : ' + element['chgDt'] + ' / ' +element['bizno']

print '#################### JSON Encoding End ########################'

print '\n'

print '#################### JSON Decoding Start ########################'

#Convert JSON String To Python Object(Dictionary, List, Tuple), JSON Decoding
jsonDict = json.loads(jsonString)

print 'json.load() type is ' + str(type(jsonDict))

print '>>>>>> GET Header Value in jsonDict : ' + str(jsonDict['response']['header'])
print '>>>>>> GET Item BizNo value in jsonDict : ' + str(jsonDict['response']['body']['items'][0]['bizno'])

print '#################### JSON Decoding End ########################'

