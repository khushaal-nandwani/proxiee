# Proxiee
Proxiee is a straightforward Flask-based proxy server. Clients can request Proxiee to call a specified API URL along with other required parameters. Proxiee then executes the request and relays the response back to the user. 

## Features
- Supports all the four methods - GET, PUT, DELETE, POST.
- Supports headers and parameters.
- Logs the server's health by logging the API called, time Proxiee took in complete processing (includes the parent api time)
- Includes a configuration file where permissible APIs and API keys can be specified, controlling access to Proxiee's functionality.
