import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL template
base_url = 'https://www.thegioididong.com/{}?p={}'

# List of phone names
phone_names = [
    'dtdd-samsung',
    'dtdd-apple-iphone',
    'dtdd-oppo',
    'dtdd-xiaomi',
    'dtdd-vivo',
    'dtdd-realme',
    'dtdd-honor',
    'dtdd-tcl',
    'dtdd-tecno',
    'dtdd-nokia',
    'dtdd-masstel',
    'dtdd-mobell',
    'dtdd-itel'
]

# List of price ranges
price_ranges = [
    'tu-2-4-trieu',
    'tu-4-7-trieu',
    'tu-7-13-trieu',
    'tu-13-20-trieu',
    'tren-20-trieu'
]

# Define user-agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Store results in a list of dictionaries to convert into a DataFrame later
results = []

# Iterate over each phone name and price range, send a request, and extract hrefs and data-name
for phone_name in phone_names:
    for price_range in price_ranges:
        url = base_url.format(phone_name, price_range)
        print(f"Crawling URL: {url}")
        
        # Send GET request to the page
        response = requests.get(url, headers=headers)
        
        # Parse the page content
        soup = BeautifulSoup(response.content, 'lxml')
        
        # Find the ul containing class "listproduct"
        product_list = soup.find('ul', class_='listproduct')
        
        # If product list not found, skip to the next URL
        if product_list is None:
            print(f"No product list found for {url}, skipping.")
            continue
        
        # Extract href and data-name from each li > a
        for li in product_list.find_all('li'):
            a_tag = li.find('a', href=True)
            if a_tag:
                href = a_tag['href']
                print (href)
                data_name = a_tag.get('data-name', 'Unknown')
                results.append({
                    'Phone Name': phone_name,
                    'Price Range': price_range,
                    'Href': href,
                    'Data Name': data_name
                })
        
        print("---")
    
    print ("====")

# Convert results to a DataFrame
df = pd.DataFrame(results)

# Save the DataFrame to an Excel file
df.to_excel('tgdd_phone_data.xlsx', index=False)
print("Data has been saved to 'tgdd_phone_data.xlsx'")
