import base64, json, requests, pytz
from dataclasses import replace
from datetime import datetime
from httplib2 import Http
import param


def alert(request):
   request_json= request.get_json()
   stores = request_json["stores"]
   gsheet_link = request_json["gsheet"]


   data = {"store":stores, "gsheet":gsheet_link}


   #Sending message to google chat
   bot_message = json.dumps(template_parser(data))
   url = "{}".format(param.GOOGLE_CHAT_URL)
   message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}
   http_obj = Http()
   response = http_obj.request(
       uri=url,
       method='POST',
       headers=message_headers,
       body=bot_message,
       )
   print("Response output: {}".format(response))
   return "True"


#Pass it to message object
def widgets(results={}):
   return [{"keyValue": {"topLabel": "<b><i>{}</i></b>".format(k), "content": v}} for k,v in results.items()]


# Google chat message object
def template_parser(load={}):
   print(type(load))
   card =  {
        "cards": [
            {
                "header": {
                    "title": "Store monitoring",
                    "subtitle": "Control date: {}".format(datetime.now(pytz.timezone('Europe/Paris')).strftime('%Y-%m-%dT%H:%M:%S')),
                    "imageUrl": "{}".format(param.LINKS_IMAGE)
                },
                "sections": [
                    {
                        "widgets": [
                            {
                                "textParagraph": {
                                    #"text": "<b>Store not conform to control rules ==> </b> <i><font color=\"#ff0000\">{}</font></i><br><a href={}> details</a>".format(load['store'],load['gsheet'])
                                    "text" : "<a href={}> Control rules file </a>".format(load['gsheet'])
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
   return card 
