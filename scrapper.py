from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Define the WebDriver and target URL
from selenium import webdriver

driver = webdriver.Chrome()

url = ''  # Replace with the actual URL

# Define the name you're looking for
target_name = 'elon musk' # dummy target name


def generate_combinations():
    """Generate credentials in the format of your regex."""
    for i in range(1, 300):
        yield f""


def check_credential(credentials):
    """Submit the inputs and check if the target name is found."""
    driver.get(url)

    # Find the input field and submit the USN (adjust based on actual HTML structure)
    input_field = driver.find_element(By.ID, 'SELECTOR')  # Update this selector
    input_field.send_keys(credentials)
    input_field.send_keys(Keys.RETURN)

    # Allow time for the page to load
    time.sleep(2)

    try:
        # Look for the name in the <h1> tag
        name_element = driver.find_element(By.TAG_NAME, 'h1')
        name = name_element.text.strip()

        if name == target_name:
            print(f"Target found for input: {credentials}")
            return True
    except Exception as e:
        print(f"Error checking input {credentials}: {str(e)}")
    return False


try:
    for credential in generate_combinations():
        if check_credential(credential):
            break
    else:
        print("Target name not found in any HTML SOURCE DATA.")
finally:
    driver.quit()