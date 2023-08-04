import requests

target_url = input("[+] Enter target URL: ")
file_name = input("[+] Enter the file name containing directories: ")

file = open(file_name, "r")


def request(url):
    try:
        return requests.get(f"http://{url}")
    except requests.exceptions.ConnectionError:
        pass


for line in file:
    directory = line.strip()
    full_url = f"{target_url}/{directory}"
    response = request(full_url)
    if response:
        print(f"[+] Discovered Directory Path: {full_url}")

# Coded By Erfan Samadi
