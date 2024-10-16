# WAF-Hunter

**WAF-Hunter** is an advanced tool designed to detect Web Application Firewalls (WAFs) and retrieve detailed information about them, including their version and provider. It works on both **Termux** and **Kali Linux**, providing a colorful and intuitive user interface with bold fonts and terminal clearing on startup.

## Features
- Detect Web Application Firewalls (WAFs) protecting websites.
- Retrieve WAF version and provider details.
- Attractive and colorful user interface with bold fonts.
- Clears the terminal and opens in full-screen mode for a professional appearance.
- Supports both **Termux** and **Kali Linux** environments.

## Installation

### Requirements
- Python 3.x
- `pip` (Python package manager)
- Internet connection

### Install on Termux
1. Update packages:
   ```bash
   pkg update && pkg upgrade
   pkg install python git
   git clone https://github.com/WizSafe/WAF-Hunter.git
   cd WAF-Hunter
   pip install -r requirements.txt
Usage
  ```bash
python3 waf-hunter.py

