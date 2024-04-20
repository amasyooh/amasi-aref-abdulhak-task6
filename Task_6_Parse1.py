import requests
from bs4 import BeautifulSoup

def scrape_headlines_and_links(url):
    # Fetch the webpage
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return [], []

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract headlines from <h1> tags
    headlines = [h1.get_text(strip=True) for h1 in soup.find_all('h1')]

    # Extract links from <a> tags
    links = [a['href'] for a in soup.find_all('a') if 'href' in a.attrs]

    return headlines, links

# Example usage:
url = 'https://dribbble.com/'  # Change to the desired URL
headlines, links = scrape_headlines_and_links(url)

print("Headlines:")
for headline in headlines:
    print(headline)

print("\nLinks:")
for link in links:
    print(link)
