# reload page

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

# List of common English syllables for email generation
syllables = [
    "ba", "be", "bi", "bo", "bu", "by",
    "cha", "che", "chi", "cho", "chu",
    "da", "de", "di", "do", "du",
    "fa", "fe", "fi", "fo", "fu",
    "ga", "ge", "gi", "go", "gu",
    "ha", "he", "hi", "ho", "hu",
    "ja", "je", "ji", "jo", "ju",
    "ka", "ke", "ki", "ko", "ku",
    "la", "le", "li", "lo", "lu",
    "ma", "me", "mi", "mo", "mu",
    "na", "ne", "ni", "no", "nu",
    "pa", "pe", "pi", "po", "pu",
    "ra", "re", "ri", "ro", "ru",
    "sa", "se", "si", "so", "su",
    "ta", "te", "ti", "to", "tu",
    "va", "ve", "vi", "vo", "vu",
    "wa", "we", "wi", "wo",
    "ya", "ye", "yi", "yo",
    "za", "ze", "zi", "zo", "zu", "AI", "ai"
]

# Function to generate a human-like email address with numbers in random positions
def generate_random_email():
    # Randomly choose the number of syllables for the email (between 1 and 4)
    num_syllables = random.randint(3, 8)
    
    # Initialize the email as an empty string
    email = ""

    # Generate the syllables and insert a number at random positions
    for i in range(num_syllables):
        syllable = random.choice(syllables)
        email += syllable
        
        # Add a random number with a 30% chance if it's not the last syllable
        if i < num_syllables - 1 and random.random() < 0.5:
            email += str(random.randint(0, 9))
    
    # Add a domain
    email += "@gmail.com"

    return email

# Set the number of times you want to repeat the process
num_iterations = 1000

# Maximum number of retry attempts
max_retries = 3

# Sleep duration between retries (in seconds)
retry_sleep = 5

# Start a new instance of the Chrome browser
driver = webdriver.Chrome()

# Main loop with error handling and retries
for _ in range(num_iterations):
    retry_count = 0
    while retry_count < max_retries:
        try:
            # Open the web page in the browser
            driver.get("https://lorescan.com/lore-stories/?ref=Qp2DcK")  # Replace with the actual URL of the webpage
            # Locate the input field and submit button by their IDs
            input_field = driver.find_element(By.ID, "email-4")
            # Locate the submit button that's immediately adjacent to the input field
            submit_button = input_field.find_element(By.XPATH, "./following-sibling::input[@type='submit']")

            # Generate a random email address
            random_email = generate_random_email()

            # Fill the input field with the generated email
            input_field.clear()
            input_field.send_keys(random_email)

            # Submit the form
            submit_button.click()

            # Wait for xxx seconds
            time.sleep(3)
        except Exception as e:
            print(f"Error encountered: {e}")
            retry_count += 1
            if retry_count < max_retries:
                print(f"Retrying in {retry_sleep} seconds...")
                time.sleep(retry_sleep)
            else:
                print("Maximum retry attempts reached. Exiting script.")
                break
        else:
            print("Iteration completed successfully.")
            break

# Close the browser
driver.quit()
