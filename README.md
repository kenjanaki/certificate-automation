# certificate-automation
Automating certificate issual for an online platform (Geeta Pariwar)

## Requirements
- Python (Version 3.7 or higher)
- Selenium Library (Can be installed via requirements.txt)
- Google Chrome (Version 131.0.6778.139)
- ChromeDriver (Version 131.0.6778.108, matching the Chrome version)

## Installation Steps

### Clone the Repository
```bash
git clone https://github.com/kenjanaki/certificate-automation.git
cd certificate-automation
```

### Install Dependencies
   Use the requirements.txt file to install the necessary Python libraries.
```bash
pip install -r requirements.txt
```

### Download ChromeDriver
- Ensure you download the ChromeDriver version closest to your installed Google Chrome version (can be found [here](https://googlechromelabs.github.io/chrome-for-testing/)).
- Select the right version (ensure Stable) and paste the ChromeDriver matching your system and paste the URL in your browser.
- For other browsers, download their corresponding webdrivers (e.g., Firefox WebDriver: mozilla/geckodriver, Brave being Chromium-based uses Chrome WebDriver)
- Download it from ChromeDriver Downloads
- Place the downloaded chromedriver.exe file in the correct path (e.g., C:/path/to/chromedriver.exe).

### Enable Remote Debugging in Chrome
- To connect the script to a running Chrome instance, you need to start Chrome with remote debugging enabled.
- Steps to Start Chrome with Debugging Mode:
  
    1. Close all running instances of Chrome.
    2. Open a terminal or command prompt and run:
       
    ```bash
    "C:/Program Files/Google/Chrome/Application/chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:/ChromeProfile"
    ```
    
  - Replace the path with the actual installation directory of Chrome on your system.
  - This starts Chrome in debugging mode on port 9222.

### Update the Script
In the script, update the following paths according to your setup:
- webdriver_path: Path to your chromedriver.exe. Example:
```bash
webdriver_path = "C:/path/to/chromedriver.exe"
```
- download_dir: Directory where downloaded PDFs will be stored. Example:
```bash
download_dir = "downloads"
```

### Run the Script
Run the Python script using the command:
```bash
python automation.py
```
The script will automatically:

   - Log in to the platform.
   - Process PRNs (student IDs) and Adhyayams.
   - Extract and save SMS messages to a file (all_sms_contents.txt).
   - Download certificates as PDFs.


## Instructions for Use
1. Ensure the platform URL is accessible and you have the required permissions.
2. Add the PRNs and Adhyayams in the script’s dictionary (prn_adhyayam_dict) in the format:
   
```bash
prn_adhyayam_dict = {
    1: [12],
    2: [12, 15],
    ...
}
```

- 1: PRN (Student ID)
- [12, 15]: List of Adhyayams to process for that PRN.
3. Run the script, and it will:
  
   - Enter PRNs in the input field on the platform.
   - Click checkboxes for specified Adhyayams.
   - Extract SMS messages from popups.
   - Save SMS content in all_sms_contents.txt.
   - Download PDF certificates.


## Troubleshooting
1. Error: "ChromeDriver Version Mismatch"
   
    - Ensure your ChromeDriver version matches your Chrome browser version.
      
3. Popup or Button Not Found
   
    - The platform’s layout may have changed. Check and update the XPATH or ID selectors in the script.
      
5. File Download Issues
   
    - Ensure the download_dir exists and your browser is configured to allow downloads automatically.


## File Overview
- ```automation.py```: The main Python script.
- ```requirements.txt```: Dependencies for the project.
- ```all_sms_contents.txt```: File where extracted SMS messages are saved.
- ```downloads/```: Directory for downloaded PDF certificates.

## Notes
- Adjust the sleep times in the script if the platform is slow to load.
- The script assumes a standard browser layout for Geeta Pariwar's platform. If the layout changes, you may need to update the element locators (IDs/XPATHs).
For additional help or questions, feel free to open an issue or reach out to me.
