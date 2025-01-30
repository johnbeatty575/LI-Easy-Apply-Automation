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

### Limitations 
- The script applies to a **maximum of 10 jobs** by default. This limit can be adjusted in `main.py`.
- LinkedIn may flag your account for unusual activity if the script is run too frequently. Add delays between actions to mimic human behavior.
- The script only works with "Easy Apply" job postings. Multi-step applications are not supported.

### Contributions
Contributions are welcome! If you’d like to contribute, please:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.
