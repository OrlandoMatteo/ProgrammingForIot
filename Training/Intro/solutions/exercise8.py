if __name__ == "__main__":
    # There are 2 way to to this exercise, we could create a dictionary

    # First method
    # With all the keys and the emtpy values and then fill it
    personal_data = {
        "projectName": "",
        "company": "",
        "deviceList": [
            {
                "deviceID": "",
                "deviceName": "",
                "deviceType": "",
            }
        ]}
    personal_data['projectName'] = input("Write the project name")
    personal_data['company'] = input("Write the company name")
    personal_data['deviceList'][0]['deviceID'] = input("Write the device ID")
    personal_data['deviceList'][0]['deviceName'] = input("Write the device name")
    personal_data['deviceList'][0]['deviceType'] = input("Write the device type")

    print(personal_data)

    # Second method
    # We will create an empty dictionary to store everything and then add keys and values one by one
    personal_data = {}
    personal_data['projectName'] = input("Write the project name")
    personal_data['company'] = input("Write the company name")
	# We create an empty list to store the devices
	personal_data['deviceList'] = []
	# We create a dictionary to store the device data
    device = {
        "deviceID": "",
        "deviceName": "",
        "deviceType": "",
    }
    device['deviceID'] = input("Write the device ID")
    device['deviceName'] = input("Write the device name")
    device['deviceType'] = input("Write the device type")
    # We add the device to the list
    personal_data['deviceList'].append(device)

    print(personal_data)
