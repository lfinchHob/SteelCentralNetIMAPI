import requests
import json 
import config

_urls = {
  "devices": "/v1/devices",
  "device": "/v1/devices/{id}",
  "create_device": "/v1/devices/"
}

def get(_path):
    return requests.get(_path, verify=False, auth=(config.username, config.password))

def post(_path, _data):
    return requests.post(_path, verify=False, auth=(config.username, config.password),
			data = _data,
			headers={'Content-Type':'application/json'})

def delete(_path):
    return requests.delete(_path)

def put(_path, _data):
    return requests.put(path, 
        data = data,
        headers={'Content-Type':'application/json'})

def build_path(_base_url, _operation):
    return _base_url + _urls[_operation];

def get_devices():
    path = build_path(config.base_url, "devices")
    print(get(path).json())

def get_device(_device_id):
    path = build_path(config.base_url, "device").format(id=_device_id)
    print(get(path).json())

def create_device(_device_model):
    path = build_path(config.base_url, "create_device")
    obj = post(path, json.dumps(_device_model))
    print(obj.content)
