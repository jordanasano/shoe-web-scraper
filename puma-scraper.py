from bs4 import BeautifulSoup
import requests

def scrape_puma(num_shoes):
    count = 0

    html_text = requests.get(f'https://us.puma.com/us/en/women/shoes/lifestyle?offset={num_shoes}').text
    soup = BeautifulSoup(html_text, 'lxml')

    shoes = soup.find_all('li', class_="relative flex flex-col w-full group")

    for shoe in shoes:
        count += 1

        price = None

        if shoe.find('h3', class_="font-bold text-puma-red whitespace-nowrap"):
            price = shoe.find('h3', class_="font-bold text-puma-red whitespace-nowrap").text
        else: 
            price = shoe.find('p', class_="whitespace-nowrap font-bold").text

        name = shoe.find(
            'h3', 
            class_="w-full mobile:text-sm mobile:pr-0 font-bold text-base pr-5"+
            " !leading-snug line-clamp-2 md:line-clamp-none").text.strip()
        
        print(f'{count}: {name} costs {price}!\n')

        if count == num_shoes:
            return

    print('All out of shoes!')

scrape_puma(2000)