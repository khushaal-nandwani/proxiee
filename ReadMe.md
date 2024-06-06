# Proxiee
Proxiee is a straightforward Flask-based proxy server. Clients can request Proxiee to call a specified API URL along with other req uired parameters. Proxiee then executes the request and relays the response back to the user. 

## ToDo
- Add Payload Support

## Features
- Supports popular methods - GET, PUT, DELETE, POST.
- Supports headers and parameters.
- Logs the server's health by logging the API called, time Proxiee took in complete processing (includes the parent api time), the IP of the Client, method etc. into a new log file every midnight along with an analysis tool for log. 
- Includes a configuration file where permissible APIs and username passwords can be specified, controlling access to Proxiee's functionality.

## Setup
- Activate the virtual enviornemnt .venv
- run `python main.py` to start the server

## Troubleshooting
- Make sure the python is correctly located in the .venv/pyvenv.cfg
- Make sure python is installed and is in the PATH. 
- Make sure to configure myconfig.ini as per your requirements. 