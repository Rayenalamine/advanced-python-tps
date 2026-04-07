# simple_scraper.py
import requests
from bs4 import BeautifulSoup

# The website we want to scrape
url = "http://httpbin.org/html"  # simple test page

# Get the page content
response = requests.get(url, verify=False)  # skip SSL check for simplicity

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Print the page title (if it exists)
if soup.title:
    print("Page title:", soup.title.text)
else:
    print("Page has no title")

# Print the first header (h1)
header = soup.find("h1")
if header:
    print("H1 header:", header.text)
else:
    print("No H1 header found")

# Print all links
links = soup.find_all("a")
if links:
    for i, link in enumerate(links, start=1):
        print(f"Link {i}: {link.text} -> {link.get('href')}")
else:
    print("No links found")