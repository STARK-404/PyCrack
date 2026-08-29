
# 💀 PyCrack - Instagram Brute Force Suite 🔥


![Python Badge](https://img.shields.io/badge/Written%20In-Python-yellow?style=flat-square&logo=python)
![Open Source Badge](https://img.shields.io/badge/Open%20Source-No-red?style=flat-square&logo=open-source-initiative)

## 🔥 About

**PyCrack** is a Python-based Instagram security testing tool designed for credential validation and account auditing. It uses Instagram's private mobile API with proper encryption to test username and password combinations efficiently.

The tool implements AES-256-GCM encryption for password protection and RSA PKCS#1 v1.5 for session key encryption, matching Instagram's own security protocol. With support for 35+ Android device configurations, proxy rotation, and random user-agent generation, PyCrack operates with anti-detection capabilities to avoid rate limiting and blocking.

Key capabilities include:

- **Encrypted Password Testing** - Uses Instagram's proprietary encryption algorithm
- **Device Spoofing** - Rotates between 35+ real Android device fingerprints
- **Proxy Support** - Optional proxy rotation with authentication support
- **Smart Wordlist** - Automatically filters invalid password combinations
- **Stealth Mode** - Random headers and parameters to avoid detection
- **Result Management** - Saves successful logins and checkpoint accounts separately

## 📦 Installation

### Windows
```bash
git clone https://github.com/username/PyCrack.git
cd PyCrack
pip install -r requirements.txt
python install.py
python PyCrack.py
```

### Termux (Android)
```bash
pkg update -y && pkg upgrade -y
pkg install python-pip git
git clone https://github.com/username/PyCrack.git
cd PyCrack
pip install -r requirements.txt
python install.py
python PyCrack.py
```

### Linux
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip git
git clone https://github.com/username/PyCrack.git
cd PyCrack
pip3 install -r requirements.txt
python install.py
python PyCrack.py
```

![Screenshot](https://raw.githubusercontent.com/STARK-404/INSTAHACK/refs/heads/main/repo/ss.jpg)

## 🛠️ Support

If you find this tool useful, consider supporting the developer by **starring the repository** or making a donation. Your support helps in maintaining and improving the tool.

[![Telegram](https://img.shields.io/badge/Telegram-MR__S74RK-blue?logo=telegram)](https://t.me/MR_S74RK)
[![Instagram](https://img.shields.io/badge/Instagram-la1uuuuu-red?logo=instagram)](https://instagram.com/)
[![Email](https://img.shields.io/badge/Email-gamerunknown509%40gmail.com-green?logo=gmail)](mailto:lautaronahuelus@gmail.com?subject=Insta)

If you encounter any issues while using this tool, please open an [Issue](https://github.com/username/PyCrack/issues) on GitHub.

## ⚠️ Disclaimer

This tool is for educational purposes and security research only. The developer is not responsible for any misuse, damage, or illegal activities conducted with this tool. Users are solely responsible for complying with applicable laws and obtaining proper authorization before testing any accounts.

## 📜 License

This project is not open source. All copyrights to the source code belong to the developer. You are granted the right to use this tool, but you are not permitted to modify, distribute, or resell the source code without permission.
