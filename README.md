# LinkedIn Easy Apply Automation (Raspberry Pi)

This project automates the application process for LinkedIn's "Easy Apply" job postings using Selenium and Python. It is optimized for Raspberry Pi and runs in headless mode, making it ideal for unattended operation.

---

## Features
- Automates job applications on LinkedIn using the "Easy Apply" feature.
- Saves applied jobs to a SQLite database (`applications.db`).
- Logs all actions to `logs/application.log`.
- Runs in headless mode for efficiency on Raspberry Pi.
- Configurable job search criteria (keywords and location).

---

## Hardware Requirements
- **Raspberry Pi 4 (4GB or 8GB RAM)** recommended.
- **32GB microSD Card** (Class 10 or higher).
- **Stable Internet Connection** (Wi-Fi or Ethernet).
- **Official Raspberry Pi 4 Power Supply** (5.1V/3A).
- **Heatsinks and Fan** for cooling.

---

## Software Requirements
- **Raspberry Pi OS (64-bit)**.
- **Chromium Browser**.
- **ChromiumDriver**.
- **Python 3.9+**.
- **Selenium** and **WebDriver Manager**.

---

## Setup Instructions

### 1. Install Raspberry Pi OS
1. Download the 64-bit Raspberry Pi OS from the official website: [Raspberry Pi OS](https://www.raspberrypi.com/software/).
2. Use **Raspberry Pi Imager** to flash the OS to your microSD card.
3. Enable SSH and Wi-Fi (optional) by creating `ssh` and `wpa_supplicant.conf` files in the boot partition.

### 2. Update the System
1. Open the terminal and run:
   ```bash
   sudo apt update
   sudo apt upgrade -y
   sudo apt dist-upgrade -y