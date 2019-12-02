import NetIMAPI

def main():
    print("Provide the device id: ")
    deviceid = input()
    NetIMAPI.get_device(deviceid) 

if __name__ == '__main__':
    main()
