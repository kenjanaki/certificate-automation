# certificate-automation
Automating certificate issual for an online platform (geeta pariwar)

### Requirements
- Python (Version 3.7 or higher)
- Selenium Library (Can be installed via requirements.txt)
- Google Chrome (Version 131.0.6778.139)
- ChromeDriver (Version 131.0.6778.108, matching the Chrome version)

### Installation Steps

1. Clone the Repository
'''console
git clone <repository-link>
cd certificate-automation
'''

2. Install Dependencies
   Use the requirements.txt file to install the necessary Python libraries.
'''console
pip install -r requirements.txt
'''

3. Download ChromeDriver
- Ensure you download the ChromeDriver version matching your installed Google Chrome version (131.0.6778.108).
- For other browsers, download their corresponding webdrivers (e.g., Firefox WebDriver: mozilla/geckodriver, Brave being Chromium-based uses Chrome WebDriver)
- Download it from ChromeDriver Downloads
- Place the downloaded chromedriver.exe file in the correct path (e.g., C:/path/to/chromedriver.exe).

4. Enable Remote Debugging in Chrome
- To connect the script to a running Chrome instance, you need to start Chrome with remote debugging enabled.
- Steps to Start Chrome with Debugging Mode:
    - Close all running instances of Chrome.
    - Open a terminal or command prompt and run:
    '''console
    "C:/Program Files/Google/Chrome/Application/chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:/ChromeProfile"
    '''
      - Replace the path with the actual installation directory of Chrome on your system.
      - This starts Chrome in debugging mode on port 9222.

5. Update the Script
   In the script, update the following paths according to your setup:
7. Run the Script
