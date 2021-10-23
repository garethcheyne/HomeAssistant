from os import stat
import time
import sys, getopt
import subprocess
import requests


def get_hostname():
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJiYTkyZjE0ODg5ZjI0NTQ5OWE2OWMwOWY3NzU3N2I2NyIsImlhdCI6MTYzNDg3MTA4NywiZXhwIjoxOTUwMjMxMDg3fQ.31e_xO59EwnEjLuJu_D4mq8IMlExN2IIjHZufwuyYAk"
    headers = {"Authorization": "Bearer " + token}   
    url = "http://localhost:8123/api/core/info"
    response = requests.request("GET", url, headers=headers) 
    print(response) 

if __name__ == "__main__":
    get_hostname()

