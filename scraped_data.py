# import requests library and beautifulsoup
import random
import requests
from bs4 import BeautifulSoup

# desired website
url = 'https://cooking.nytimes.com/search'

def scrape(url):
    result = requests.get(url)
    content = result.text
    soup = BeautifulSoup(content, 'html.parser')
    return soup

# scrape each recipe link from website
def recipe_links():
    random_num = random.randint(2, 25)
    return [
        link for page in range(random_num, random_num+3)
        for link in set(
            'https://cooking.nytimes.com' + link['href']
            for link in scrape(url + f"?page={page}").find_all('a', href=True)
            if '/recipes/' in link['href']
        )
    ]

# scrape together each recipe title from website
def recipe_titles():

    return [
        ' '.join([title.text for title in scrape(link).find_all('h1', class_='pantry--title-display')])
        for link in recipe_links()
    ]

# scrape the recipe ingredients from website
def recipe_ingredients():
    
    return [
        [ingredient.text for ingredient in scrape(link).find_all('li', class_='pantry--ui ingredient_ingredient__rfjvs')]
        for link in recipe_links()
    ]

# scrape the recipe times from website
def recipe_times():

    return [
        ' '.join([time.text for time in scrape(link).find('dt', string='Total Time').find_next_sibling('dd')])
        for link in recipe_links()
    ]

# aggregate each recipe title, time to cook, and ingredients into a dictionary
def aggregation():

    aggregation = [{"Title" : title,
        "Time to Cook" : time, 
        "Ingredients" : ingredient,
        "URL": link,}

        for title, time, ingredient, link in zip(recipe_titles(), recipe_times(), recipe_ingredients(), recipe_links())]
    
    return aggregation
