import csv
import requests
from bs4 import BeautifulSoup

def get_linkedin_data(first_name, last_name):
    # Prepare CSV file
    with open('linkedin_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Headline', 'Location', 'Profile URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Search for users on LinkedIn
        search_url = f"https://www.linkedin.com/pub/dir/?first={first_name}&last={last_name}"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract data from search results
        profiles = soup.find_all('li', class_='content-type-search')

        # Iterate over the first 10 search results
        for profile in profiles[:10]:
            try:
                name = profile.find('span', class_='name').text.strip()
            except:
                name = ""
            try:
                headline = profile.find('p', class_='headline').text.strip()
            except:
                headline = ""
            try:
                location = profile.find('p', class_='subline').text.strip()
            except:
                location = ""
            try:
                profile_url = profile.find('a', class_='link')['href']
            except:
                profile_url = ""

            # Write data to CSV
            writer.writerow({'Name': name, 'Headline': headline, 'Location': location, 'Profile URL': profile_url})

if __name__ == "__main__":
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    get_linkedin_data(first_name, last_name)
    print("Data saved to linkedin_data.csv")

