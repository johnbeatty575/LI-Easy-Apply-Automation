# LinkedIn Easy Apply Automation Tool
This Python-based automation tool streamlines the process of applying for jobs on LinkedIn using the "Easy Apply" feature. It uses Selenium for browser automation and SQLite for tracking applications. The tool is designed to save time and effort for job seekers by automatically submitting applications to jobs that match their preferences.

**`NOTE`**: This project is being tested and will have ad hoc updates. 

## Features
- Automatically logs into LinkedIn.
- Searches for jobs based on customizable keywords and location.
- Applies to jobs with the "Easy Apply" option.
- Tracks applied for jobs in an SQLite database to prevent duplicates.
- Logs application activity in a log file for easy review.
## Requirements
- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- The following Python libraries:
  - `selenium`
  - `pandas` (optional, for any data manipulation)
## Setup Instructions
1. Clone the Repository
```bash
git clone https://github.com/your-username/linkedin_easy_apply.git
cd linkedin_easy_apply
```
3. Install Dependencies

It’s recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
pip install -r requirements.txt
```
3. Download ChromeDriver
- Check your Google Chrome version:
  - Open Chrome and navigate to `chrome://settings/help`.
- Download the compatible version of [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/).
- Place the `chromedriver.exe` file in the root directory of the project.
4. Configure Your Credentials
- Open `config.py` and provide your LinkedIn credentials and job search preferences:

```python
USERNAME = "your_email@example.com"
PASSWORD = "your_password"

KEYWORDS = ["Python Developer", "Data Analyst"]
LOCATION = "United States"
```
5. Initialize the SQLite Database

The database will be automatically created and initialized when you run the script for the first time.

## Usage
1. Run the script:

```bash
python main.py
```
2. The script will:
- Log into LinkedIn using your credentials.
- Search for jobs matching the specified keywords and location.
-Apply to jobs with the "Easy Apply" option.
- Log applications in:
  - `logs/application_logs.log` (log file).
  - `applications.db` (SQLite database).
3. To view the database contents:

```bash
sqlite3 applications.db
SELECT * FROM applications;
```
## Project Structure
```bash
linkedin_easy_apply/
│
├── main.py              # Main script to run the automation
├── config.py            # Stores user credentials and job preferences
├── utils.py             # Helper functions (logging, SQLite operations)
├── requirements.txt     # List of Python dependencies
├── logs/                # Directory for log files
│   └── application_logs.log
├── applications.db      # SQLite database (created on first run)
├── chromedriver.exe     # ChromeDriver executable (download separately)
└── README.md            # Project documentation
```
## How It Works
1. **Login**: The script uses Selenium to log into LinkedIn using the provided credentials.
2. **Search Jobs**: It navigates to LinkedIn's job search page and searches for jobs based on your preferences.
3. **Apply**: For each job in the search results, the script attempts to apply via the "Easy Apply" button. If successful, it logs the application in both the database and the log file.

## Troubleshooting
- **ChromeDriver Version Mismatch**: Ensure that your ChromeDriver version matches your Chrome browser version.
- **Blocked Account**: Limit usage to avoid being flagged for automation by LinkedIn.
- **Selenium Timeout Errors**: Adjust the wait times in the script if pages load slowly.
- **Database Issues**: If the database is corrupted, delete `applications.db` and rerun the script to recreate it.
  
## Future Enhancements
- Add filters for job type (full-time, part-time, remote).
- Add filters for "Date posted" (Any time, Past Month, Past week, etc.).
- Add Resume == Seach Parameter correlation.
- Add Cover Letter functionality.
- Expand database schema to track application status.
- Enable CAPTCHA solving (if required by LinkedIn).

## Disclaimer
This project is for educational purposes only. Use it responsibly to avoid violating LinkedIn’s terms of service. The creator is not liable for any misuse of this tool.

### License
This project is licensed under the MIT License. See 'LICENSE' for more details.
