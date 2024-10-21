# WAF-Hunter

**WAF-Hunter** is an advanced tool developed by **WizSafe Organization** to detect and bypass Web Application Firewalls (WAFs) on websites. This tool integrates with **wafw00f** to detect WAFs and provides various techniques to attempt bypassing them.

![WAF-Hunter Screenshot](screenshot.png)  <!-- Add a relevant screenshot link -->

## Features
- Detects Web Application Firewalls using **wafw00f**.
- Provides multiple techniques to attempt WAF bypass.
- Simple and intuitive interface with colorful banners.
- Supports URL Encoding, Base64 Encoding, Hex Encoding, and more.

## Prerequisites

Before running this tool, ensure you have the following installed:

- **Termux (or Linux environment)**
- **Python 3**
- **wafw00f** package

## Installation

1. Update and upgrade Termux:
   ```bash
   pkg update && pkg upgrade

2. Install Python and necessary dependencies

 ```bash
pkg install python
pip install termcolor requests
```

3. Install wafw00f
```bash
pkg install wafw00f
```
4. Clone the repository
```bash
git clone https://github.com/WizSafe/WAF-Hunter.git
cd WAF-Hunter
```
5. Run The Script

```bash
python waf-hunter.py
```
Usage 
1. Enter the URL of the website you want to scan for WAFs.
2. If a WAF is detected, choose whether you want to attempt bypass techniques.
3. Select from the following WAF bypass techniques:

**URL Encode Payload**
**Case Manipulation**
**String Obfuscation**
**Base64 Encode Payload**
**Hex Encode Payload**
**Use Custom HTTP Method**

4. Enter the payload to attempt bypassing the WAF.

Supported WAFs

WAF-Hunter can detect and attempt to bypass many common WAFs, including:

**1. Cloudflare**
**2. Mod Security (SpiderLabs)**
**3. Sucuri**
**4. Akamai**

```And many more...```

⚠️Disclaimer⚠️

This tool is intended for educational purposes only. WizSafe Organization does not take responsibility for any misuse of this tool. Use it ethically and only on sites you have permission to test.
   
