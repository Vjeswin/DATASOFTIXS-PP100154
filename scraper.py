import requests
from bs4 import BeautifulSoup
import csv
import time
def fetch_data(page=1):
    url = f"http://quotes.toscrape.com/page/{page}/"
    headers = {"User-Agent": "Mozilla/5.0"} 
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []    
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []    
    for item in soup.select(".quote"):
        text = item.select_one(".text").text.strip() if item.select_one(".text") else "N/A"
        author = item.select_one(".author").text.strip() if item.select_one(".author") else "N/A"
        quotes.append({"quote": text, "author": author})    
    return quotes
def save_to_csv(data, filename="quotes.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["quote", "author"])
        writer.writeheader()
        writer.writerows(data)
def main():
    all_quotes = []
    page = 1    
    while True:
        print(f"Fetching page {page}...")
        data = fetch_data(page)        
        if not data:
            break        
        all_quotes.extend(data)
        page += 1
        time.sleep(2)    
    save_to_csv(all_quotes)
    print("Data saved to quotes.csv")
if __name__ == "__main__":
    main()
