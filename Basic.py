"""
Web Scraping with Python:
    * Web scraping involves extracting data from websites.
    * BeautifulSoup is a Python library used to parse HTML and XML documents.
"""

# Importing necessary libraries
import requests
from bs4 import BeautifulSoup

"""
Web Scraping Principles:
    * Understand the structure of a web page using HTML tags.
    * Use Python libraries like requests to fetch the content of a web page.
    * Use BeautifulSoup to parse the HTML and extract information.
"""

# Fetching the content of a static web page
url = 'https://google.com'
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    page_content = response.content
    print("Page fetched successfully")
else:
    print("Failed to fetch the page")

"""
Parsing and Extracting Information:
    * BeautifulSoup is used to parse the fetched HTML content.
    * Commonly extracted elements include text, links, and images.
"""
# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')

# Extracting the title of the page
title = soup.title.string
print("Page Title:", title)

# Extracting all the links on the page
links = soup.find_all('a')
for link in links:
    print("Link:", link.get('href'))

# Extracting all the images on the page
images = soup.find_all('img')
for image in images:
    print("Image Source:", image.get('src'))

"""
Saving Extracted Data (Optional):
    * The extracted data can be saved to a file or database for further analysis.
"""
# Example of saving links to a text file
with open('extracted_links.txt', 'w') as file:
    for link in links:
        file.write(link.get('href') + '\n')

