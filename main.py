import requests
from bs4 import BeautifulSoup


def scrape_hotels(location, budget):
    url = "https://www.example.com/hotels/{location}"  # Methnata actual website eke link eka danna one
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        hotels = soup.find_all('div', class_='hotel')  # Ayya We need Adjust this selector according to the HTML structure

        for hotel in hotels[:5]:
            name = hotel.find('h2').text.strip()
            price = hotel.find('span', class_='price').text.strip()
            if int(price.replace('$', '')) <= budget:
                print(f"Hotel: {name}, Price: {price}")
    else:
        print("Failed to fetch data from the website.")


def main():
    location = input("Enter the location: ")
    budget = int(input("Enter your budget: $"))

    scrape_hotels(location, budget)


if __name__ == "__main__":
    main()
