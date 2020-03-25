#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import sys
import traceback
import urllib.request
import socket
import flask
from flask import request, jsonify

hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# r = requests.get("https://api.github.com/users/harishvc")

def get_path(arg_json, arg_path):
  ob_typ = ""
  nodes = arg_path.split(".")
  out_json = arg_json
  for node in nodes:
    print("Asking for {} of type {} in {}".format(node,  type(node), type(out_json)))
    if out_json is None:
      print("OutJSON is None")
      return ""
    if isinstance(out_json, dict):
      ob_typ = "o"
      print("It is JSONObject")
      if not(node.isdigit()):
        out_json = out_json[node]
        print(out_json)
      else:
        ob_typ = "s"
        print("Type mismatch dict")
        return ""
    else:
      if isinstance(out_json, list):
        print("It is JSONArray")
        ob_typ = "a"
        if node.isnumeric():
          out_json = out_json[int(node)]
        else:
          print("Type mismatch list")
          ob_typ = "s"
          return ""
      else:
        print("Neither list nor dict")
        ob_typ = "v"
        return out_json
  if ob_typ == "o":
    return jsonify(out_json)
  else:
    return out_json


@app.route('/', methods=['GET'])
def home():
  app.logger.info("Running in host {} with {}".format(hostname, ipaddr))
  in_path = request.args.get('querypath')
  app.logger.info("User asked for {}".format(in_path))
  # in_json = json.load(urllib.request.urlopen("https://api.github.com/users"))
  try:
    with open('in_sample_file.json') as f:
      in_json = json.load(f)
  except :
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("*** print_tb:")
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
    return ""
  return get_path(in_json, in_path)


if __name__ == "__main__":
  app.run(host='0.0.0.0')
