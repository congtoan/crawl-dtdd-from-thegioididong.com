# Crawl Mobile Listings from TheGioiDiDong.com

This repository contains a Python script that crawls mobile phone listings from the website TheGioiDiDong.com. It scrapes the phone names and prices within specific price ranges and exports the details into an Excel file. The extracted information includes the `href` link and `data-name` for each phone listing.

## Features
- Scrapes mobile phone listings for different brands and price ranges.
- Extracts the `href` link and the `data-name` attribute from the page.
- Saves the extracted data into an Excel file for further analysis.
- Easily customizable for other ranges or brands.

## Price Ranges
The tool crawls phones from the following price ranges:
- **Under 2 million VND** (`duoi-2-trieu`)
- **2-4 million VND** (`tu-2-4-trieu`)
- **4-7 million VND** (`tu-4-7-trieu`)
- **7-13 million VND** (`tu-7-13-trieu`)
- **13-20 million VND** (`tu-13-20-trieu`)
- **Above 20 million VND** (`tren-20-trieu`)

## Brands Crawled
The tool is currently set up to crawl the following mobile phone brands:
- Samsung
- Apple (iPhone)
- OPPO
- Xiaomi
- Vivo
- Realme
- Honor
- TCL
- Tecno
- Nokia
- Masstel
- Mobell
- Itel

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/congtoan/crawl-dtdd-from-thegioididong.com.git
   cd crawl-dtdd-from-thegioididong.com
