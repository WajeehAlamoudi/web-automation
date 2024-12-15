

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Remote debugging address
remote_debugging_address = "127.0.0.1:1980"  # HERE YOU MAY CHANGE THE KEY 1980 but check the CMD user-data-dir FILE


# Create Chrome options and set the debugging address
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", remote_debugging_address)

# Initialize the WebDriver with the existing Chrome session
driver = webdriver.Chrome(options=chrome_options)

# Navigate
urls = [
    'https://www.khanacademy.org/math/statistics-probability/analysis-of-variance-anova-library/analysis-of-variance-anova/v/anova-1-calculating-sst-total-sum-of-squares',
    'https://www.khanacademy.org/math/statistics-probability/analysis-of-variance-anova-library/analysis-of-variance-anova/v/anova-2-calculating-ssw-and-ssb-total-sum-of-squares-within-and-between-avi',
    'https://www.khanacademy.org/math/statistics-probability/analysis-of-variance-anova-library/analysis-of-variance-anova/v/anova-3-hypothesis-test-with-f-statistic'
]
mins = [240, 420, 320]

# Iterate through the URLs
for i, (url, duration) in enumerate(zip(urls, mins), 1):
    # Navigate to the URL
    driver.get(url)
    print(f"{i}. Navigating to: {url}")

    try:
        # Wait until the play button is clickable
        play_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play video"]'))
        )
        play_button.click()
        print(f"{i}. Play button clicked.")

        # Wait for the video to play for at least the specified duration
        start_time = time.time()
        while time.time() - start_time < duration:
            time.sleep(1)

        print(f"{i}. Video played for at least {duration} seconds.")
    except Exception as e:
        print(f"{i}. Error: CHECK THE WEB PAGE SOME THING POP-UP \n {str(e)} ")

# Close the browser
driver.quit()
