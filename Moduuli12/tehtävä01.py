import requests

def fetch_random_joke(category):
    response = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}')
    data = response.json()
    print(data['value'])

fetch_random_joke('science')
