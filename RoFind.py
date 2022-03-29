import json, requests

def GetName(Input):
    with requests.Session() as Session:
        Info = json.loads(Session.get(f'http://verify.eryn.io/api/user/{Input}').text)['robloxUsername']
        return Info

def GetID(Input):
    with requests.Session() as Session:
        Info = json.loads(Session.get(f'http://verify.eryn.io/api/user/{Input}').text)['robloxId']
        return Info
