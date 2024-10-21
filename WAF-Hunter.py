import os
import subprocess
from termcolor import colored
import urllib.parse
import base64
import requests

def clear_screen():
    os.system('clear')  # Clear terminal

def banner():
    print(colored("""
     ________ _______ _______ 
    |  |  |  |   _   |    ___|
    |  |  |  |       |    ___|
    |________|___|___|___|    
    """, 'green', attrs=['bold']))
    print(colored("Developed by WizSafe Organization", 'green', attrs=['bold']))

def detect_waf(url):
    try:
        # WAF detection logic (integrating wafw00f)
        result = subprocess.run(['wafw00f', url], capture_output=True, text=True)
        print(colored(result.stdout, 'cyan'))
    except Exception as e:
        print(colored(f"Error: {e}", 'red', attrs=['bold']))

# URL Encoding Bypass
def url_encode(payload):
    return urllib.parse.quote(payload)

# Case Manipulation Bypass
def case_manipulation(payload):
    manipulated = ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(payload)])
    return manipulated

# String Obfuscation Bypass
def string_concatenation(payload):
    obfuscated = "'+'".join(payload.split(' '))
    return obfuscated

# Base64 Encoding Bypass
def base64_encode(payload):
    encoded = base64.b64encode(payload.encode()).decode()
    return encoded

# Hex Encoding Bypass
def hex_encode(payload):
    return ''.join([hex(ord(c))[2:] for c in payload])

# Custom HTTP Method Bypass
def send_custom_method(url, method="PUT", data=None):
    headers = {'User-Agent': 'WAF-Hunter'}
    response = requests.request(method, url, headers=headers, data=data)
    return response.text

def display_menu():
    print(colored("Choose a WAF Bypass Technique", 'yellow', attrs=['bold']))
    print(colored("1. URL Encode Payload", 'green'))
    print(colored("2. Case Manipulation", 'green'))
    print(colored("3. String Obfuscation", 'green'))
    print(colored("4. Base64 Encode Payload", 'green'))
    print(colored("5. Hex Encode Payload", 'green'))
    print(colored("6. Use Custom HTTP Method", 'green'))
    
    choice = input(colored("Select an option: ", 'yellow', attrs=['bold']))
    return choice

def bypass_waf():
    choice = display_menu()
    if choice == '1':
        payload = input(colored("Enter payload: ", 'yellow'))
        print(colored("Encoded Payload: " + url_encode(payload), 'cyan'))
    elif choice == '2':
        payload = input(colored("Enter payload: ", 'yellow'))
        print(colored("Case Manipulated Payload: " + case_manipulation(payload), 'cyan'))
    elif choice == '3':
        payload = input(colored("Enter payload: ", 'yellow'))
        print(colored("Obfuscated Payload: " + string_concatenation(payload), 'cyan'))
    elif choice == '4':
        payload = input(colored("Enter payload: ", 'yellow'))
        print(colored("Base64 Encoded Payload: " + base64_encode(payload), 'cyan'))
    elif choice == '5':
        payload = input(colored("Enter payload: ", 'yellow'))
        print(colored("Hex Encoded Payload: " + hex_encode(payload), 'cyan'))
    elif choice == '6':
        url = input(colored("Enter URL: ", 'yellow'))
        method = input(colored("Enter HTTP Method (PUT/DELETE): ", 'yellow'))
        print(colored("Response: \n" + send_custom_method(url, method), 'cyan'))
    else:
        print(colored("Invalid choice!", 'red'))

def main():
    clear_screen()
    banner()
    url = input(colored("Enter the URL to scan: ", 'yellow', attrs=['bold']))
    detect_waf(url)
    
    bypass_choice = input(colored("Do you want to attempt WAF bypass techniques? (y/n): ", 'yellow', attrs=['bold']))
    if bypass_choice.lower() == 'y':
        bypass_waf()

if __name__ == "__main__":
    main()

