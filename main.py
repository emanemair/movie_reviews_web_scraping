from bs4 import BeautifulSoup
import pandas as pd
import requests

import  openpyxl


response =requests.get("https://www.rogerebert.com/reviews")
contents = response.text
soup = BeautifulSoup(contents, 'html.parser')

movies = soup.find_all(name="div" , class_="review-stack--info")
page_source='https://www.rogerebert.com'
movies_name=[]
movies_link=[]
author_name=[]
rate=[]
# print(movies)
for movie in movies:
    movies_name.append(((movie.find(name="h5", class_="review-stack--title").getText()).lstrip('\n')).rstrip('\n'))
for movie in movies:
    author_name.append((((movie.find(name="h6" , class_="review-stack--byline")).getText()).lstrip('\n')).rstrip('\n'))
for movie in movies:
    rate.append(len(movie.find_all(name="i" , class_="icon-star-full")))
for movie in movies :
    movies_link.append(page_source +((movie.find(name="a")).get("href")) )

# print(movies_name)
# print(movies_link)
# print(author_name)
# print(rate)

# max = 0
# max_index=0
# for r in  range(0,len(rate)):
#     if (rate[r] > max):
#         max=rate[r]
#         max_index=r
#
# print(max , max_index)
# print(movies_name[max_index])
# print(author_name[max_index])


movies_data={
 "name" : movies_name ,
 "author" : author_name ,
"rate/5" : rate,
"review link ": movies_link

}
data_set= pd.DataFrame(movies_data)
# data_set.to_csv("movie_data_set", sep=',', index=False, encoding='utf-8')
# read_file = pd.read_csv (r'C:\Users\User\Desktop\beauitfulSoup\movie_data_set')
# read_file.to_excel (r'C:\Users\User\Desktop\beauitfulSoup\dataset.xlsx', index = None, header=True)
print(data_set)