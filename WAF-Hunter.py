import os
import subprocess
from termcolor import colored

def clear_screen():
    os.system('clear')  # Clear terminal

def banner():
    print(colored("Advanced WAF Detector", 'blue', attrs=['bold']))
    print(colored("Developed by WizSafe Organization", 'green', attrs=['bold']))

def detect_waf(url):
    try:
        # WAF detection logic (integrating wafw00f)
        result = subprocess.run(['wafw00f', url], capture_output=True, text=True)
        print(colored(result.stdout, 'cyan'))
    except Exception as e:
        print(colored(f"Error: {e}", 'red', attrs=['bold']))

def main():
    clear_screen()
    banner()
    url = input(colored("Enter the URL to scan: ", 'yellow', attrs=['bold']))
    detect_waf(url)

if __name__ == "__main__":
    main()
