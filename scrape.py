from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Set up ChromeDriver path
webdriver_path = "PATH_TO_WEBDRIVER"

chrome_options = Options()

# Connect to the already running Chrome instance using remote debugging
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # The port where Chrome is running with the remote debugger
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

url = "https://online.learngeeta.com/faculty/examl1.php"
print(f"Opening the URL: {url}")
driver.get(url)

# PRN and corresponding Adhyayams as a dictionary (with lists of integers for Adhyayams)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Enter PRNs and their corresponding adhyayam like in the example
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
prn_adhyayam_dict = {
    1: [12],
    2: [12, 15],
    3: [12],
    4: [15],
    5: [15],
    6: [15],
    7: [15],
    8: [15]
}

# File to save the SMS contents
output_file = "all_sms_contents.txt"

download_dir = "downloads"
os.makedirs(download_dir, exist_ok=True)

with open(output_file, "w", encoding="utf-8") as file:

    for pnr, adhyayams in prn_adhyayam_dict.items():
        print(f"Processing PRN: {pnr}, Adhyayams: {adhyayams}")

        prn_input = driver.find_element(By.ID, "prn")
        prn_input.clear()
        prn_input.send_keys(str(pnr))
        print(f"PRN {pnr} entered.")
        prn_input.send_keys(Keys.RETURN)

        print("Waiting for the row to load...")
        time.sleep(1)

        # Loop through each Adhyayam for the given PRN
        for adhyayam in adhyayams:
            if adhyayam == 12:
                checkbox_id = f"chk_{pnr}_12"
                button_xpath = f"//*[@id='{pnr}']"  # 12th SMS button
                close_button_xpath = "/html/body/div[3]/div/div/div[1]/button"  # Close button for 12th
            elif adhyayam == 15:
                checkbox_id = f"chk_{pnr}_15"
                button_xpath = f"//*[@id='{pnr}'][@ad='15']"  # 15th SMS button
                close_button_xpath = "/html/body/div[3]/div/div/div[1]/button"  # Close button for 15th

            # Check the corresponding checkbox
            try:
                checkbox = driver.find_element(By.ID, checkbox_id)
                if not checkbox.is_selected():
                    checkbox.click()
                    print(f"Adhyayam {adhyayam} checkbox clicked for PRN {pnr}.")
                else:
                    print(f"Adhyayam {adhyayam} checkbox already checked for PRN {pnr}.")
            except Exception as e:
                print(f"Error locating checkbox for PRN {pnr}, Adhyayam {adhyayam}: {e}")
                continue

            # Click the corresponding SMS button
            try:
                sms_button = driver.find_element(By.XPATH, button_xpath)
                sms_button.click()
                print(f"Adhyayam {adhyayam} SMS button clicked for PRN {pnr}.")
            except Exception as e:
                print(f"Error locating SMS button for PRN {pnr}, Adhyayam {adhyayam}: {e}")
                continue

            time.sleep(1)

            # Extract the message from the popup
            try:
                popup_text = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]").text
                print(f"Popup Message for PRN {pnr}, Adhyayam {adhyayam}: {popup_text}")

                # Write the result into the file in the required format
                file.write(f"PRN: {pnr} | Adhyayam {adhyayam} SMS:\n")
                file.write(f"{popup_text}\n")
                file.write("-" * 30 + "\n")
                print(f"Popup message saved to '{output_file}'.")
            except Exception as e:
                print(f"Error extracting popup message for PRN {pnr}, Adhyayam {adhyayam}: {e}")

            # Close the popup
            try:
                copy_close_button = driver.find_element(By.XPATH, close_button_xpath)
                copy_close_button.click()
                print("Popup closed.")
            except Exception as e:
                print(f"Error closing popup for PRN {pnr}, Adhyayam {adhyayam}: {e}")

            # Download the PDF
            try:
                download_button_xpath = f"//*[@id='d{pnr}']"
                download_button = driver.find_element(By.XPATH, download_button_xpath)
                download_button.click()
                print(f"PDF download initiated for PRN {pnr}.")
                
                time.sleep(1)
            except Exception as e:
                print(f"Error downloading PDF for PRN {pnr}: {e}")

# Close the browser
driver.quit()

print(f"All SMS contents saved to '{output_file}'. PDFs have been downloaded.")
