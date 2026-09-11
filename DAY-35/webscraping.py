# ============================================================
# WEB SCRAPING PROGRAM
# Extract Product Name, Price and Image URL
# Save the data into a CSV file
# ============================================================

# Step 1: Import Required Libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
from google.colab import files


# Step 2: Define the URL
URL = "https://timely-sunshine-e821b3.netlify.app/"


# Step 3: Load the Web Page
page = requests.get(URL)


# Step 4: Check the Status Code
print("Status Code:", page.status_code)


# Step 5: Parse the HTML Content
htmlCode = page.text
soup = BeautifulSoup(htmlCode, "html.parser")


# Step 6: Test - Extract First Product Name
content = soup.find("div", class_="name")

if content:
    print("First Product Name:", content.text.strip())


# Step 7: Find All Product Items
items = soup.find_all("div", class_="a")

print("Number of Products:", len(items))


# Step 8: Create Empty Lists
names = []
prices = []
images = []


# Step 9: Extract Product Details
for item in items:

    # Extract Product Name
    name_tag = item.find("div", class_="name")
    name = name_tag.text.strip() if name_tag else None

    # Extract Price
    price_tag = item.find("div", class_="price")
    price = price_tag.text.strip() if price_tag else None

    # Extract Image URL
    image_div = item.find("div", class_="image")
    image_tag = image_div.find("img") if image_div else None

    image_src = image_tag.get("src") if image_tag else None

    # Add data to lists
    names.append(name)
    prices.append(price)
    images.append(image_src)


# Step 10: Create a Pandas DataFrame
df = pd.DataFrame({
    "Product_Name": names,
    "MRP": prices,
    "Image_SRC": images
})


# Step 11: Display the Scraped Data
print("\nScraped Data:")
print(df)


# Step 12: Save Data into CSV File
csv_filename = "productdetails.csv"

df.to_csv(csv_filename, index=False)

print("\nCSV file saved as:", csv_filename)


# Step 13: Download CSV File
files.download(csv_filename)