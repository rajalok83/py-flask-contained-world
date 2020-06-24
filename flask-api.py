#!/usr/bin/env python
# coding: utf-8

import json
import sys
import traceback
#import urllib.request
import socket
from os import path
import flask
from flask import request, jsonify
import logging

hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
#Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
# Create Console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# Add formatter too Console Handler
ch.setFormatter(formatter)
# Creae Logger
logger = logging.getLogger("flask-api-json")
logger.setLevel(logging.DEBUG)
# Add Handler to Logger
logger.addHandler(ch)

app = flask.Flask(__name__)
app.config["DEBUG"] = True
qp_splitter = "."
json_file = "in_sample_file.json"
# r = requests.get("https://api.github.com/users/harishvc")

def get_path(arg_json, arg_path, arg_splitter="."):
  nodes = arg_path.split(arg_splitter)
  out_json = arg_json
  for node in nodes:
    # logger.info("Asking for {} of type {} in {}".format(node,  type(node), type(out_json)))
    if out_json is None:
      logger.warning("OutJSON is None")
      return ""
    if isinstance(out_json, dict):
      # logger.info("It is JSONObject")
      if not(node.isdigit()):
        out_json = out_json[node]
        # print(out_json)
      else:
        logger.error("Type mismatch dict")
        return ""
    else:
      if isinstance(out_json, list):
        # logger.info("It is JSONArray")
        if node.isnumeric():
          out_json = out_json[int(node)]
        else:
          logger.error("Type mismatch list")
          return ""
      else:
        logger.error("Neither list nor dict")
        return out_json
  return out_json


@app.route('/', methods=['GET'])
def home():
  global json_file, qp_splitter
  app.logger.info("Running in host {} with {}".format(hostname, ipaddr))
  in_path = request.args.get('qp')
  in_qp_splitter = request.args.get('qps')
  in_json_file = request.args.get('jlf')
  if in_qp_splitter is None:
    logger.info("No input specified for qps")
    run_qp_splitter = qp_spliiter
  else:
    logger.info("Spliiter specified: {}".format(in_qp_splitter))
    run_qp_splitter = in_qp_splitter
  if in_json_file is None:
    logger.info("No input specified for jlf")
    run_json_file = json_file
  else:
    logger.info("File specified: {}".format(in_json_file))
    run_json_file = in_json_file
  app.logger.info("User asked for {}".format(in_path))
  # in_json = json.load(urllib.request.urlopen("https://api.github.com/users"))
  try:
    with open(".{}{}{}{}".format(path.sep,"conf",path.sep,run_json_file), 'r') as f:
      in_json = json.load(f)
      return jsonify(get_path(in_json, in_path, run_sp_splitter))
  except :
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("*** print_tb:")
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
    return ""

  
if __name__ == "__main__":
  app.run(host='0.0.0.0')
