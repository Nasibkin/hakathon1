from bs4 import BeautifulSoup
import requests
import csv
import re


URL = 'https://www.mashina.kg/search/all/'

def write_to_csv(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['price_dollar'], data['image'], data['description']])
    

def get_html(url):
    response = requests.get(url)
    return response.text
print(get_html(URL))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # return soup
    list_car = soup.find_all('div', class_ = 'list-item list-label') #.find_all('div', class_ = 'list-item list-label')
    # return list_comp
    for car in list_car:
        title = car.find('h2', class_ = 'name').text.replace(',', '').replace('\n', '').replace(' ', '')
        price_dollar = car.find('strong').text.replace(',', '').replace('\n', '').replace(' ', '')
        description = re.sub(r'\s+', ' ', car.find('div', class_="block info-wrapper item-info-wrapper").text).strip()
        image = car.find('img', class_='lazy-image').get('data-src') if car.find('img', class_='lazy-image') != None else 'None'
        dict_ = {'title':title, 'price_dollar':price_dollar, 'image':image, 'description':description}
        write_to_csv(dict_)


def main():
    count = 1
    for i in range(10):
        news_url = f'https://www.mashina.kg/search/all/?page={str(count)}'
        get_data(get_html(news_url))
        count+=1
print(get_data(get_html(URL))) 
main()       


