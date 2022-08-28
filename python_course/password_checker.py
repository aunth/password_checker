import hashlib
import requests
import sys
    
def request_data_api(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise f"Something went wrong try again. Error {res.status_code}"
    return res

def passwords_leaks_count(respone, tail):
    hashes = (line.split(':') for line in respone.text.splitlines())
    for hash, count in hashes:
        if hash == tail:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    head, tail = sha1password[:5], sha1password[5:]
    respone = request_data_api(head)
    return passwords_leaks_count(respone, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"Password {password} was found {count} times")
        else:
            print(f"Password {password} was not found. Carry on")

if __name__ == "__main__":
    main(sys.argv[1:])








