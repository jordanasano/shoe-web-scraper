from bs4 import BeautifulSoup
import requests

def scrape_shoe_data(num_shoes):
    count = 0
    while count < num_shoes:
        html_text = requests.get(f'https://www.kohls.com/catalog/mens-shoes.jsp?CN=Gender:Mens+Department:Shoes&cc=mens-TN2.0-S-shoes&kls_sbp=56751120711696885714221506018546775523&PPP=48&WS={count}&S=1&sks=true').text
        soup = BeautifulSoup(html_text, 'lxml')

        shoes = soup.find_all('li', class_='products_grid')

        for shoe in shoes:
            if count == num_shoes:
                return

            titles = shoe.find_all('p')

            for title in titles:
                if title.text.strip() != 'For Price, Add to Cart':
                    title = title.text.strip()

            price = None

            if shoe.find('span', class_="prod_price_amount red_color"):
                price = shoe.find('span', class_="prod_price_amount red_color").text.strip()
            else: 
                price = shoe.find('span', class_="prod_price_amount").text.strip()

            if price == '':
                price = shoe.find('div', class_="prod_price_original").text.strip()
                price += ', but add to cart to see reduced price'
            count += 1
            print(f"{count}: The {title} costs {price}.\n")
