from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from config import USERNAME, PASSWORD, KEYWORDS, LOCATION
from utils import log_application, initialize_db, save_application
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/application.log"),
        logging.StreamHandler()
    ]
)

# Initialize WebDriver for Chromium on Raspberry Pi
def initialize_driver():
    try:
        # Use ChromiumDriver for Raspberry Pi
        service = Service(ChromeDriverManager().install())
        
        # Configure Chromium options for Raspberry Pi
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--disable-gpu")  # Disable GPU acceleration
        options.add_argument("--no-sandbox")  # Bypass OS security model
        options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        options.add_argument("--start-maximized")  # Start maximized (even in headless mode)
        options.add_argument("--disable-blink-features=AutomationControlled")  # Disable automation flags

        # Specify the Chromium binary location
        options.binary_location = "/usr/bin/chromium-browser"

        # Initialize the WebDriver
        driver = webdriver.Chrome(service=service, options=options)
        logging.info("WebDriver initialized successfully.")
        return driver
    except Exception as e:
        logging.error(f"Failed to initialize WebDriver: {e}")
        raise

# Log in to LinkedIn
def linkedin_login(driver):
    try:
        driver.get("https://www.linkedin.com/login")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        logging.info("Logged in to LinkedIn successfully.")
    except Exception as e:
        logging.error(f"Failed to log in to LinkedIn: {e}")
        raise

# Search for jobs
def search_jobs(driver):
    try:
        driver.get("https://www.linkedin.com/jobs/")
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search jobs"]'))
        )
        search_box.send_keys(KEYWORDS[0])
        location_box = driver.find_element(By.XPATH, '//input[@placeholder="Search location"]')
        location_box.clear()
        location_box.send_keys(LOCATION)
        location_box.send_keys(Keys.RETURN)
        time.sleep(3)  # Allow search results to load
        logging.info(f"Job search completed for: {KEYWORDS[0]} in {LOCATION}.")
    except Exception as e:
        logging.error(f"Failed to search for jobs: {e}")
        raise

# Apply to jobs (limit to 10 jobs)
def apply_to_jobs(driver):
    try:
        jobs = driver.find_elements(By.CLASS_NAME, "job-card-container")
        logging.info(f"Found {len(jobs)} jobs to apply to.")
        
        applied_count = 0
        for job in jobs:
            if applied_count >= 10:  # Limit to 10 applications
                break
            
            try:
                job.click()
                time.sleep(2)
                
                # Check for "Easy Apply" button
                easy_apply_button = driver.find_element(By.XPATH, '//button[contains(text(), "Easy Apply")]')
                easy_apply_button.click()
                time.sleep(2)
                
                # Submit the application
                submit_button = driver.find_element(By.XPATH, '//button[contains(text(), "Submit application")]')
                submit_button.click()
                
                # Log the application
                job_title = driver.find_element(By.CLASS_NAME, "t-24").text
                company = driver.find_element(By.CLASS_NAME, "t-16").text
                save_application(job_title, company)
                log_application(job_title, company)
                logging.info(f"Applied to {job_title} at {company}.")
                applied_count += 1
            except Exception as e:
                logging.warning(f"Skipping job due to error: {e}")
                continue
    except Exception as e:
        logging.error(f"Failed to apply to jobs: {e}")
        raise

# Main function
def main():
    try:
        # Initialize the database
        initialize_db()
        
        # Initialize the WebDriver
        driver = initialize_driver()
        
        # Log in to LinkedIn
        linkedin_login(driver)
        
        # Search for jobs
        search_jobs(driver)
        
        # Apply to jobs
        apply_to_jobs(driver)
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")
    finally:
        # Quit the WebDriver
        if 'driver' in locals():
            driver.quit()
            logging.info("WebDriver closed successfully.")

if __name__ == "__main__":
    main()