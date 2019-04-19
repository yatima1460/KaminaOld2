import ipfsapi

try:
    api: ipfsapi.Client = ipfsapi.connect('127.0.0.1', 5001)
except ConnectionError as ce:
    print("Can't connect to IPFS local server")
    
    
