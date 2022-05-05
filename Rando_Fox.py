import requests

# Queries API
response = requests.get("https://randomfox.ca/floof")
# Establish dictionary
fox = response.json()
# Print string for dictionary
print(fox)
# Print string for image
print(fox['image'])
# Print string for link
print(fox['link'])