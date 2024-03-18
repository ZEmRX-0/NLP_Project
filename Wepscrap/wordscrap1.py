import requests
from bs4 import BeautifulSoup

base_url = 'https://relatedwords.io'

variable = input("Enter the word: ")


url = f'{base_url}/{variable}'

response = requests.get(url)

if response.status_code == 200:
   
    soup = BeautifulSoup(response.text, 'html.parser')

    
    elements = soup.find_all(attrs={"data-term": True})

   
    words = {element['data-term'].strip('"') for element in elements}


    sorted_unique_words = sorted(words)


    with open('extractedwords.txt', 'w',encoding='utf-8') as file:
        for word in sorted_unique_words:
            file.write(word + '\n')

    print("Sorted unique words after data-term= extracted and written to 'extractedwords.txt' file.")
else:
    print(f"Error: {response.status_code}")
