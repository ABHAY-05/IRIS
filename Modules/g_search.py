import requests
import bs4

def google_search(search, speak):
	url = "https://google.com/search?q=" + search
	page = requests.get( url )
	soup = bs4.BeautifulSoup( page.text , "html.parser" )
	result = soup.find( "div" , class_='BNeawe' ).text
	print(f'Iris: {result}\n')
	speak( result )