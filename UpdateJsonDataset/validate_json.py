import json

# return true is json is valid or false if unable to load
def is_json(json_file):
  try:
    json_object = json.loads(json_file)
  except ValueError:
    return False
  return True