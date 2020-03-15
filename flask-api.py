#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import urllib.request

import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# r = requests.get("https://api.github.com/users/harishvc")

def get_path(arg_json, arg_path):
  nodes = arg_path.split(".")
  out_json = arg_json
  for node in nodes:
    print("Asking for {} of type {} in {}".format(node,  type(node), type(out_json)))
    if out_json is None:
      print("OutJSON is None")
      return ""
    if isinstance(out_json, dict):
      print("It is JSONObject")
      if not(node.isdigit()):
        out_json = out_json[node]
        print(out_json)
      else:
        print("Type mismatch dict")
        return ""
    else:
      if isinstance(out_json, list):
        print("It is JSONArray")
        if node.isnumeric():
          out_json = out_json[int(node)]
        else:
          print("Type mismatch list")
          return ""
      else:
        print("Neither list nor dict")
        return out_json
  return out_json


@app.route('/', methods=['GET'])
def home():
  in_path = request.args.get('querypath')
  print("User asked for {}".format(in_path))
  in_json = json.load(urllib.request.urlopen("https://api.github.com/users"))
  return get_path(in_json, in_path)


if __name__ == "__main__":
  app.run(host='0.0.0.0')
