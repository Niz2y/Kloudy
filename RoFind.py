import json, requests

def GetName(Input):
    Info = json.loads(requests.get(f'http://verify.eryn.io/api/user/{Input}').text)['robloxUsername']
    return Info

def GetID(Input):
    Info = json.loads(requests.get(f'http://verify.eryn.io/api/user/{Input}').text)['robloxId']
    return Info
