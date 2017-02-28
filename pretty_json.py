import simplejson as json

def formatInput(input):
    return json.dumps(json.loads(input), indent=4)