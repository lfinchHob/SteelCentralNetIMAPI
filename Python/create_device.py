import NetIMAPI

model = {
  "items": [
    {
      "name": "string",
      "displayName": "string",
      "deviceName": "string",
      "accessAddress": "string",
      "deviceAccessInfo": {
        "name": "string",
        "displayName": "string",
        "active": True,
        "activeCLIConfigCollection": False,
        "activeMIBConfigCollection": True,
        "activeWMIConfigCollection": False,
        "activeMetricsCollection": True,
        "activeAWSConfigCollection": False,
        "description": "string",
        "accessAddress": "string",
        "snmpVersion": 1,
        "snmpCommunityString": "string",
      }
    }
  ]}

def main():
    print("Device name: ", end = " ")
    device_name = input()
    
    print("Device Description: ", end = " ")
    device_description = input()
    
    print("Device Community String: ", end = " ")
    device_community = input()
    
    print("Device Access Address: ", end = " ")
    device_access_address = input()

    model['items'][0]['name'] = device_name
    model['items'][0]['displayName'] = device_name
    model['items'][0]['deviceName'] = device_name
    model['items'][0]['accessAddress'] = device_access_address 
    model['items'][0]['deviceAccessInfo']['name'] = device_name 
    model['items'][0]['deviceAccessInfo']['displayName'] = device_name 
    model['items'][0]['deviceAccessInfo']['description'] = device_description 
    model['items'][0]['deviceAccessInfo']['accessAddress'] = device_access_address 
    model['items'][0]['deviceAccessInfo']['snmpCommunityString'] = device_community 

    NetIMAPI.create_device(model) 

if __name__ == '__main__':
    main()
