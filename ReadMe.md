# Proxiee
Proxiee is a straightforward Flask-based proxy server. Clients can request Proxiee to call a specified API URL along with other req uired parameters. Proxiee then executes the request and relays the response back to the user. 

## Features
- Supports popular methods - GET, PUT, DELETE, POST.
- Supports headers and parameters.
- Logs the server's health by logging the API called, time Proxiee took in complete processing (includes the parent api time), the IP of the Client, method etc. into a new log file every midnight along with an analysis tool for log. 
- Includes a configuration file where permissible APIs and username passwords can be specified, controlling access to Proxiee's functionality.

## Configuration Setup
Configure [myconfig](./myconfig.ini) file as follows

```ini
[allowed_apis]
api.endpoints.youwanttoaccess = 1

[users]
username = password

[special_apis]
if.api.haskeys = apiKey 

[allowed_ips]
127.0.0.1 = 1
```
- `allowed_apis` are the APIs that can be accessed by the user.
- `users` are the usernames and passwords that can be used to access the Proxy. 
- `special_apis` are the APIs that require special keys to be accessed. 
- `allowed_ips` are the IPs that can call Proxy. 

## Setup
- Create a virtual enviornment using `python -m venv .venv`
- Activate the virtual enviornment using `source .venv/bin/activate` for linux and `.\.venv\Scripts\activate` for windows.
- Install the dependecies using `pip install -r requirements.txt`
- run `waitress-server --host={yourHost} --port={yourPort} main:app` to start the server

## Making a Request
- The request should be made at `http://{yourHost}:{yourPort}/proxy` with the following parameters
    - 'api_url' : The API URL you want to access.

and the following **headers**

    - 'username' : The username you have configured in the myconfig.ini file.
    - 'password' : The password you have configured in the myconfig.ini file.

## Troubleshooting
- Make sure the python is correctly located in the .venv/pyvenv.cfg
- Make sure python is installed and is in the PATH. 
- Make sure to configure myconfig.ini as per your requirements. 