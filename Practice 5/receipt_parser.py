import re  # Library for regular expression operations (searching text patterns)
import json # Library for converting data into JSON format

# Open the file "raw.txt" in read mode with UTF-8 encoding
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read() # Read the entire content of the file into the 'text' variable

# Find all prices: searches for the "0,00" format occurring before the word "Стоимость"
prices = re.findall(r"(\d+ ?\d*,\d{2})\s*Стоимость", text)

# Find product names: searches for text appearing on a new line after a number and a dot (e.g., "1.\nName")
product_names = re.findall(r"\d+\.\n(.+)", text)

# Search for the total amount: looks for the value following the word "ИТОГО:"
total = re.search(r'ИТОГО:\s*\n?([\d\s]+,\d{2})', text)
# If a total is found, extract the first captured group; otherwise, set to None
last_total = total.group(1) if total else None

# Search for date and time in the format DD.MM.YYYY HH:MM:SS
date = re.search(r'\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}', text)
datetime = date.group(0) if date else None

# Determine the payment method based on keywords found in the text
if "Банковская карта" in text:
    payment_method = "Банковская карта" # Set to Bank Card if found
elif "Наличные" in text:
    payment_method = "Наличные"         # Set to Cash if found
else:
    payment_method = "Не найдено"       # Set to Not Found if neither is present

# Combine all extracted data into a single dictionary object
result = {
    "products": product_names,      # List of product names
    "prices": prices,               # List of extracted prices
    "reported_total": last_total,   # Final total amount
    "datetime": datetime,           # Date and time string
    "payment_method": payment_method # Payment type
}

# Print the result as a formatted JSON string (ensure_ascii=False handles Cyrillic correctly)
print(json.dumps(result, ensure_ascii=False, indent=4))