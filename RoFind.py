import json, requests

def GetName(Input):
    with requests.Session() as Session:
      try:
        Info = json.loads(Session.get(f'http://verify.eryn.io/api/user/{Input}').text)['robloxUsername']
        return Info
      except:
        return "Unknown User."

def GetID(Input):
    with requests.Session() as Session:
      try:
        Info = json.loads(Session.get(f'http://verify.eryn.io/api/user/{Input}').text)['robloxId']
        return Info
      except:
        return "Unknown User."
