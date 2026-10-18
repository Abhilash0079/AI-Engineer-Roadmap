products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Phone", "category": "Electronics"},
    {"name": "Shirt", "category": "Clothing"},
    {"name": "Jeans", "category": "Clothing"},
    {"name": "Book", "category": "Education"}
]

'''
Output:
{
    "Electronics": ["Laptop", "Phone"],
    "Clothing": ["Shirt", "Jeans"],
    "Education": ["Book"]
}
'''

grouped_products = {}

for product in products:
    category = product["category"]
    if category in grouped_products:
        grouped_products[category].append(product['name'])
    else:
        grouped_products[category] = [product['name']]

print(grouped_products)