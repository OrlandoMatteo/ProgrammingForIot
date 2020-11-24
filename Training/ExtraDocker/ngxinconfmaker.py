import json
import yaml

if __name__ == "__main__":
    structure = json.load(open("structure.json"))
    dockerCompose = {'version': '3.5',
                     'services': {}}
    nginxConf = "server {\n\tlisten 80;"
    port = 8080
    delta = 2
    globalServices = structure["globalServices"]

    dockerCompose["services"]["nginx"] = {
        "image": "nginx:latest",
        "ports": ["80:80"],
        "volumes": ["./default.conf:/etc/nginx/conf.d/default.conf"],
        "depends_on": []}

    for gs in globalServices:
        serviceName = gs['serviceName']
        dockerCompose['services'][serviceName] = {"build": "./"+serviceName,
                                                  "image": serviceName,
                                                  "expose": ["80"],
                                                  "ports": [str(port)+":80"]
                                                  }
        nginxConf += f"\n\tlocation /{serviceName}/ {{\n\t\tproxy_pass http://{serviceName}:80/;\n\t}}"
        port += delta
        dockerCompose["services"]["nginx"]["depends_on"].append(serviceName)

    for user in structure['users']:
        userID = user["userID"]
        for device in user["sensor"]:
            deviceName = device['deviceName']
            dockerCompose['services'][deviceName] = {"build": "./sensor",
                                                    "container_name": userID+"_"+deviceName,
                                                     "image": deviceName,
                                                     "expose": ["80"],
                                                     "ports": [str(port)+":80"],
                                                     "links": [gs["serviceName"] for gs in globalServices],
                                                     "depends_on": [gs["serviceName"] for gs in globalServices]
                                                     }
            nginxConf += f"\n\tlocation /{userID}/{deviceName}/ {{\n\t\tproxy_pass http://{userID}_{deviceName}:80/;\n\t}}"
            port += delta
            dockerCompose["services"]["nginx"]["depends_on"].append(deviceName)

    with open('docker-compose.yml', 'w', encoding='utf8') as outfile:
        yaml.dump(dockerCompose, outfile, sort_keys=False)
    with open('default.conf', 'w') as outfile:
        outfile.write(nginxConf+"\n}")
