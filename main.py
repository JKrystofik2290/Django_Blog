#!/usr/bin/env python3
"""Bug tracking program for my website and other projects.

Google's style guide was used throughout this doc, reference:
http://google.github.io/styleguide/pyguide.html
"""
import requests

response = requests.get('https://randomuser.me/api/?results=10')

data = response.json()

for user in data['results']:
    print(user['name']['first'])
    print(user['email'])
