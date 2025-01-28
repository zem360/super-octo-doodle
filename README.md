# Real Estate Listing Scraper & Notifier

This Python project uses **Selenium** to scrape real estate listings from a website(Gewobag) and send notifications via **Telegram** for new listings. It is designed to run in headless mode and automatically checks for new listings that haven't been seen before.

## Features

- **Web Scraping**: Automatically scrapes real estate listings from a specific website.
- **Telegram Notifications**: Sends real-time updates to a Telegram chat when new listings are detected.
- **Headless Browsing**: Uses Selenium in headless mode for minimal resource consumption.
- **Data Storage**: Keeps track of previously seen listings to avoid duplicate notifications.

## Requirements

- Python 3.x
- Chrome browser
- ChromeDriver (make sure it matches your Chrome version)
- Selenium library
- Requests library

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/real-estate-listing-scraper.git
cd real-estate-listing-scraper
```

### 2. Install dependencies

Use `pip` to install the required Python libraries.

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes:

```
selenium
requests
```

### 3. Download ChromeDriver

Download the ChromeDriver version that matches your installed version of Google Chrome.

Place the downloaded `chromedriver` in the `chromedriver-linux64/` directory (or update the path in the code).

### 4. Set up Telegram Bot

- Create a Telegram bot using the [BotFather](https://core.telegram.org/bots#botfather).
- Get the **bot token** from BotFather.
- Get your **chat ID**. You can use this tool to find your chat ID: [Get My ID Bot](https://t.me/getmyid_bot).

### 5. Configure the script

In the `main.py` file, replace the following placeholders:

- **bot_token**: Your Telegram bot token.
- **chat_id**: Your Telegram chat ID.
- **CHROMEDRIVER_PATH**: The path to your downloaded `chromedriver`.

## Bash Script for Running the Script

You can use the provided bash script to run the Python script in a virtual environment. This script logs the output and errors, making it easier to track the script’s execution.

### Example Bash Script (`run_script.sh`)

```bash
#!/bin/bash

echo "Starting script at $(date)" >> /path/to/project/debug.log

# Navigate to the project directory
cd /path/to/project || { echo "Failed to change directory" >> /path/to/project/debug.log; exit 1; }

# Activate the virtual environment
source /path/to/project/.venv/bin/activate || { echo "Failed to activate virtual environment" >> /path/to/project/debug.log; exit 1; }

# Run the Python script
python /path/to/project/main.py >> /path/to/project/debug.log 2>&1

# Deactivate the virtual environment (optional, for clean-up)
deactivate

echo "Finished script at $(date)" >> /path/to/project/debug.log
```

### How to use the Bash Script

1. Save the script to a file, e.g., `run_script.sh`.
2. Make it executable:

```bash
chmod +x run_script.sh
```

3. Run the script:

```bash
./run_script.sh
```

This bash script will:
1. Navigate to the project directory.
2. Activate the virtual environment.
3. Run the Python script (`main.py`).
4. Log output and errors to a `debug.log` file in the project directory.

Make sure to replace `/path/to/project` with the actual path to your project directory.

## Usage

To manually run the script, you can execute the following command:

```bash
python main.py
```

The script will:
1. Scrape the specified website for new real estate listings.
2. Compare the listings with those already seen (stored in `seen_listings.json`).
3. Send a Telegram notification for any new listings.
4. Update the list of seen listings to ensure no duplicates are processed.

## File Structure

```
real-estate-listing-scraper/
│
├── chromedriver-linux64/        # Directory containing the ChromeDriver
│   └── chromedriver             # ChromeDriver executable
│
├── seen_listings.json           # Stores previously seen listings (to avoid duplicates)
├── main.py                      # Main Python script for scraping and notifications
├── requirements.txt             # Python dependencies
├── run_script.sh                # Bash script to run the Python script with logging
└── README.md                    # This README file
```

## Contributing

Feel free to fork the repository and submit pull requests. Contributions are welcome!

## License

This project is open source and available under the [MIT License](LICENSE).

