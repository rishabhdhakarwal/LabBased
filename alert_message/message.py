import requests
import json

URL = 'http://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':'ICAUVWG32ISHQYIG489EI9VWJABO6Q08',
  'secret':'PYN8DUCD16QL5913',
  'usetype':'stage',
  'phone':'8006476100',
  'message':'The textMessage I want to send',
  'senderid':'Rishabh Dhakarwal'
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
and then requst to api
"""
# print response if you want
print response.text