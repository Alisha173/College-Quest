from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv

# Specify the website and path to chromedriver
website = 'https://collegedunia.com/btech/private-colleges'
path = "Program Codes\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

# Create a Service object using the path
service = Service(path)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service)

# Open the website
driver.get(website)

# Function to scroll the page
def scroll_down(driver):
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(1)
# Initialize a list to store unique colleges with URLs while maintaining order
colleges_list = []

# Scroll and scrape until we have 500 unique colleges
while len(colleges_list) < 50:
    # Find all college links (parent <a> tags)
    college_elements = driver.find_elements(By.XPATH, '//a[@class="jsx-3230181281 college_name underline-on-hover"]')
    
    # Add colleges to the list if they are unique
    for college in college_elements:
        # Extract the college name and URL
        college_name_elem = college.find_element(By.TAG_NAME,'h3')
        college_info = college_name_elem.text
        partial_url = college.get_attribute("href")
        
        # Full URL by appending the base URL
        full_url = f"https://collegedunia.com{partial_url}" if partial_url.startswith('/') else partial_url
        
        # Split the college name and location at the last comma
        if ',' in college_info:
            name, location = college_info.rsplit(',', 1)
            name = name.strip()  # Remove leading/trailing whitespace from the name
            location = location.strip()  # Remove leading/trailing whitespace from the location
            college_tuple = (name, location, full_url)
        else:
            college_tuple = (college_info.strip(), "", full_url)  # In case there is no location
        
        # Add only if not already in the list to maintain order
        if college_tuple not in colleges_list:
            colleges_list.append(college_tuple)  # Append the tuple to maintain order

    # Scroll to load more colleges if necessary
    scroll_down(driver)
    
    # Print progress
    print(f"Collected {len(colleges_list)} unique colleges...")

# Limit to the first 500 unique colleges
colleges_list = colleges_list[:50]  # Take only the first 500 unique colleges

# Save the first 500 unique colleges to a CSV file
with open('CSV files\\sample50college.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Serial No.', 'College Name', 'Location', 'URL'])  # Updated header with 'URL'

    for idx, (college_name, location, url) in enumerate(colleges_list, start=1):
        writer.writerow([idx, college_name, location, url])

# Close the driver after scraping
driver.quit()

print(f"Scraped the first 500 colleges and saved to 'sample50college'.")
