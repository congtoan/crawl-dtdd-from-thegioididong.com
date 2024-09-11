import requests
from bs4 import BeautifulSoup
import pandas as pd

# Read the Excel file
input_file = 'tgdd_phone_data.xlsx'
df = pd.read_excel(input_file)

# Create a list to hold the scraped data
data = []

# Define user-agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    phone_name = row["Phone Name"]
    price_range = row["Price Range"]
    title = row["Data Name"]
    href_value = row['Href']  # Get the value from the 'Href' column
    url = f"https://www.thegioididong.com{href_value}"
    print(url)

    # Send GET request to the page
    response = requests.get(url, headers=headers)

    # Parse the page content
    soup = BeautifulSoup(response.content, 'lxml')

    # Extract required data
    gia_hien_tai = soup.find(class_="box-price-present")
    gia_hien_tai = gia_hien_tai.text.strip() if gia_hien_tai else None
    print(gia_hien_tai)

    gia_goc = soup.find(class_="box-price-old")
    gia_goc = gia_goc.text.strip() if gia_goc else None

    giam_gia = soup.find(class_="box-price-percent")
    giam_gia = giam_gia.text.strip() if giam_gia else None

    info = {"Khoảng giá": price_range, "Hãng":phone_name, "Tiêu đề":title, "Giá bán": gia_hien_tai,"Giá gốc":gia_goc,"Mức giảm giá":giam_gia}

    # Extract additional parameters
    parameter__list = soup.find('ul', class_='parameter__list')
    if parameter__list:
        li_tags = parameter__list.find_all("li")
        for li in li_tags:
            cau_hinh_name = li.find("p", class_="lileft").get_text(strip=True) if li.find("p", class_="lileft") else None
            cau_hinh_value = li.find("div", class_="liright").get_text(strip=True) if li.find("div", class_="liright") else None

            info[cau_hinh_name] = cau_hinh_value

    data.append(info)

    print("----")


# Convert the data to a DataFrame
scraped_df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_file = 'product_detail_output.xlsx'
scraped_df.to_excel(output_file, index=False)

print(f"Data has been updated and saved to {output_file}")
