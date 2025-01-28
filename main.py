from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import requests
import os
import json

# Path to your ChromeDriver (replace with your actual path)
CHROMEDRIVER_PATH = './chromedriver'  # Update this path
SEEN_LISTINGS_FILE = 'seen_listings.json'

# Configure Chrome options
options = Options()
options.add_argument("--headless")  # Run headless Chrome (no GUI)
service = Service(CHROMEDRIVER_PATH)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

def load_seen_listings():
    if os.path.exists(SEEN_LISTINGS_FILE):
        with open(SEEN_LISTINGS_FILE, 'r') as file:
            return set(json.load(file))
    return set()

def save_seen_listings(seen_listings):
    with open(SEEN_LISTINGS_FILE, 'w') as file:
        json.dump(list(seen_listings), file)

def check_new_listings(driver, url):
    driver.get(url)
    time.sleep(5)  # Wait for the page to load
    
    # Use XPath to find the listings
    listings = driver.find_elements(By.XPATH, '//article[contains(@class, "angebot-big-box")]')
    
    # Print the number of listings found
    print(f"Found {len(listings)} listings")
    
    # Extract listing information (e.g., title, address, area, availability, URL)
    new_listings = []
    for listing in listings:
        try:
            title = listing.find_element(By.CLASS_NAME, 'angebot-title').text
        except:
            title = 'N/A'
        
        try:
            address = listing.find_element(By.TAG_NAME, 'address').text
        except:
            address = 'N/A'

        try:
            area = listing.find_element(By.CLASS_NAME, 'angebot-area').text
        except:
            area = 'N/A'
        
        try:
            availability = listing.find_element(By.CLASS_NAME, 'availability').text
        except:
            availability = 'N/A'
        
        try:
            link = listing.find_element(By.CLASS_NAME, 'read-more-link').get_attribute('href')
        except:
            link = 'N/A'
        
        new_listings.append((title, address, area, availability, link))
    
    return new_listings

def send_telegram_notification(new_listings, bot_token, chat_id):
    base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    headers = {'Content-Type': 'application/json'}
    
    for title, address, area, availability, link in new_listings:
        message = (f"New Listing:\n"
                   f"Title: {title}\n"
                   f"Address: {address}\n"
                   f"Area: {area}\n"
                   f"Availability: {availability}\n"
                   f"Link: {link}")
        payload = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.post(base_url, json=payload, headers=headers)
        if response.status_code != 200:
            print(f"Failed to send message: {response.text}")

def main():
    url = 'https://www.example.com/real-estate-listings'  # Replace with actual URL
    bot_token = 'YOUR_BOT_TOKEN'  # Replace with your Telegram bot token
    chat_id = 'YOUR_CHAT_ID'  # Replace with your Telegram chat ID
    
    seen_listings = load_seen_listings()
    new_listings = check_new_listings(driver, url)
    
    # Filter out already seen listings
    unique_new_listings = [listing for listing in new_listings if listing[0] not in seen_listings]
    
    if unique_new_listings:
        send_telegram_notification(unique_new_listings, bot_token, chat_id)
        # Update the set of previously seen listings
        seen_listings.update([listing[0] for listing in unique_new_listings])
        save_seen_listings(seen_listings)
    else:
        print("No new listings found.")


if __name__ == "__main__":
    main()
