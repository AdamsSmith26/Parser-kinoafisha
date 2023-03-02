import requests
from bs4 import BeautifulSoup


url = 'https://www.kinoafisha.info/online/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

def get_name():
    names = []
    films_name = soup.find_all('a', class_= 'movieItem_title')
    for film_name in films_name:
        names.append(film_name.text)
    return names


def get_genre():
    genres = []
    genres_name = soup.find_all('span', class_= 'movieItem_genres')
    for genre_name in genres_name:
        genres.append(genre_name.text)
    return genres
    
def get_year():
    years = []
    year_values = soup.find_all('span', class_= 'movieItem_year')
    for year in year_values:
        years.append(year.text)
    return years

def get_result(names, genres, years):
    results = []
    for i in range(len(names)):
        result = f'{names[i]} - {genres[i]}, {years[i]}'
        results.append(result)
    return results

results = get_result(get_name(), get_genre(), get_year())
files = open('films.txt', 'w', encoding='utf-8')

def add_result_file(files):
    for result in results:
        files.write(result + '\n')
    files.close()

add_result_file(files)