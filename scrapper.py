from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Define the WebDriver and target URL
from selenium import webdriver

driver = webdriver.Chrome()  # No need to specify the path if added to PATH

url = 'https://results.jssstuniv.in/'  # Replace with the actual URL

# Define the name you're looking for
target_name = 'Adithya Deepthi Kumar'


def generate_usns():
    """Generate USNs in the format of 01JCE21CSXXX."""
    for i in range(1, 300):
        yield f'01JST21CS{i:03d}'

usn = 01JST21CS005

def check_usn(usn):
    """Submit the USN and check if the target name is found."""
    driver.get(url)

    # Find the input field and submit the USN (adjust based on actual HTML structure)
    input_field = driver.find_element(By.ID, 'USN')  # Update this selector
    input_field.send_keys(usn)
    input_field.send_keys(Keys.RETURN)

    # Allow time for the page to load
    time.sleep(2)

    try:
        # Look for the name in the <h1> tag
        name_element = driver.find_element(By.TAG_NAME, 'h1')
        name = name_element.text.strip()

        if name == target_name:
            print(f"Target found for USN: {usn}")
            return True
    except Exception as e:
        print(f"Error checking USN {usn}: {str(e)}")
    return False


try:
    for usn in generate_usns():
        if check_usn(usn):
            break
    else:
        print("Target name not found in any USN.")
finally:
    driver.quit()