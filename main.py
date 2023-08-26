# Importing necessary libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests
import openpyxl

# Sending a GET request to a URL
response = requests.get("https://www.rogerebert.com/reviews")
contents = response.text

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(contents, 'html.parser')

# Extracting movie information
movies = soup.find_all(name="div", class_="review-stack--info")
page_source = 'https://www.rogerebert.com'
movies_name = []
movies_link = []
author_name = []
rate = []

# Looping through the movies to extract data
for movie in movies:
    # Extracting movie names
    movies_name.append(((movie.find(name="h5", class_="review-stack--title").getText()).lstrip('\n')).rstrip('\n'))
    
for movie in movies:
    # Extracting author names
    author_name.append((((movie.find(name="h6", class_="review-stack--byline")).getText()).lstrip('\n')).rstrip('\n'))

for movie in movies:
    # Extracting ratings
    rate.append(len(movie.find_all(name="i", class_="icon-star-full")))

for movie in movies:
    # Extracting movie links
    movies_link.append(page_source + ((movie.find(name="a")).get("href")))

# Creating a dictionary to store movie data
movies_data = {
    "name": movies_name,
    "author": author_name,
    "rate/5": rate,
    "review link": movies_link
}

# Creating a Pandas DataFrame from the collected data
data_set = pd.DataFrame(movies_data)

# Printing the DataFrame
print(data_set)

# Note: Some lines related to CSV and Excel export are commented out.
# Uncomment them if you want to export the data to CSV or Excel.
# data_set.to_csv("movie_data_set.csv", sep=',', index=False, encoding='utf-8')
# read_file = pd.read_csv('movie_data_set.csv')
# read_file.to_excel('dataset.xlsx', index=None, header=True)
