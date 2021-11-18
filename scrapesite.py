import requests
import bs4 
res = requests.get('https://www.flipkart.com/search?q=jeans')
soup = bs4.BeautifulSoup(res.text,'html.parser')
containers = soup.find('div',{'class':'IIdQZO _1R0K0g _1SSAGr'})
print(' Total Number of Products found' ,len(containers))
for container in containers:
	brand = container.findAll('div',{'class':'_2B_pmu'})
	description = container.find_all('div',{'class':'_2mylT6'})
	myLinks = container.find_all('a')
	print(myLinks[0].attrs['href'])

