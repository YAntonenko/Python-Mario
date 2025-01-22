# 22.01.2025 Yuna Antonenko

import json
import requests

url = 'https://dummyjson.com/products'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for product in data["products"]:
        print(f"{product['id']}.")
        print(f"Product: {product['title']}")
        print(f"Description: {product['description']}")
        print(f"Category: {product['category']}")
        print(f"Weight: {product['weight']}00g")
        print(f"Price: {product['price']}€")
        print("-------------------")


else:
    print("Tekkis viga!", response.status_code)


















