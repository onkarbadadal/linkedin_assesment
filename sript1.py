import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_linkedin_data(first_name, last_name):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    # Load LinkedIn search page
    driver.get('https://www.linkedin.com/search/results/people/')

    # Wait for the page to load
    time.sleep(2)

    # Find the search input field
    search_input = driver.find_element_by_xpath('//input[@placeholder="Search"]')

    # Input the first and last name
    search_input.send_keys(first_name + ' ' + last_name)
    search_input.send_keys(Keys.RETURN)

    # Wait for search results to load
    time.sleep(5)

    # Find all search result elements
    search_results = driver.find_elements_by_class_name('search-result__info')

    # Prepare CSV file
    with open('linkedin_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Headline', 'Location', 'Profile URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate over the first 10 search results
        for result in search_results[:10]:
            try:
                name = result.find_element_by_class_name('actor-name').text
            except:
                name = ""
            try:
                headline = result.find_element_by_class_name('subline-level-1').text
            except:
                headline = ""
            try:
                location = result.find_element_by_class_name('subline-level-2').text
            except:
                location = ""
            try:
                profile_url = result.find_element_by_tag_name('a').get_attribute('href')
            except:
                profile_url = ""

            # Write data to CSV
            writer.writerow({'Name': name, 'Headline': headline, 'Location': location, 'Profile URL': profile_url})

    # Close the WebDriver
    driver.quit()

if __name__ == "__main__":
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    get_linkedin_data(first_name, last_name)
    print("Data saved to linkedin_data.csv")

