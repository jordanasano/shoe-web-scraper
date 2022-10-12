from bs4 import BeautifulSoup
import requests

def scrape_auto_shops(num_shops):
    count = 0

    while count < num_shops:
        html_text = requests.get(f"https://sacramento.craigslist.org/search/aos?s={count}").text
        soup = BeautifulSoup(html_text, 'lxml')

        shops = soup.find_all('li', class_="result-row")

        if len(shops) == 0:
            print("All out of shops!")
            return

        for shop in shops:
            count += 1
            title = shop.find('a', class_="result-title hdrlnk").text

            if shop.find('span', class_="result-hood"):
                area = shop.find('span', class_="result-hood").text
                print(f'{count}: {title}\n{area}\n\n')
            else: 
                print(f'{count}: {title}\n\n')

            if count == num_shops:
                return


scrape_auto_shops(1000)
