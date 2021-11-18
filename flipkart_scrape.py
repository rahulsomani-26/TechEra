import requests,urllib
import bs4,csv


def get_url(url):
	response = requests.get(url)
	if not response.ok:
		print(" Server responded with ",response.status_code)

	else:
		return(response)

def main():

	source = get_url('https://www.ebay.com/itm/Levis-Mens-501-Original-Fit-Jeans-Straight-Leg-Button-Fly-100-Cotton/132485134303?epid=1100864433&_trkparms=ispr%3D1&hash=item1ed8bab7df:m:m2BdF78tKXSbcodEmR_TT4g&enc=AQADAAAB0KX%2FKt4E1xf3SDqEdBclaYYtvjDwpbA9cdDgo3RTZkPCM5H5WbnmbdO3jBCGv%2FbPrzyyjW8uIubqr68uwW3le1u3XGQ3fsLO7oFNVONXZq1MyziSegpmNFceJJVoowg7Q60e7MqPMIeSflbO6J4S3zZK%2B4ejwEKkhMU70T9Twklqe%2Btlbxk1fJXB%2BZkAzznrap3y%2FeIslcgkobOuYGsyMCN0e9E9ZUx7HnILai5PhQNibzpCCJCW8IzAz69VWXlH7f%2BDbmnF1j6LfllYzGffGGAeXebfnrYMkq5GTnl6F4bze4JOpgIR13Je4%2Bv8O6YLC3WhPVRczHFPBmJz2fhBc75MoeDmAqGzOJ%2F9HDKvac%2BNgcSLlkgrGeMd9Bb6Zcppr4zV%2FMARzAQsTssjEHJmHG8j1DzRaSW9jjUvlreFapRvW%2FTwl6ivx9WUO%2BN5MAlH7RNqIeL2VIC%2BtVS7b8qkhtO%2Bl%2BVqaOC8xJWHQF5pFiJYtmp6XHOHWcQ%2FNk4eBPK74XOYP4GeDrmspj81t%2BxG70vI2PdG%2BSIvmyo%2BrYdJ2UoTplvGpapjmVaxK%2BDwxgwp0RrZ%2F3klGYMCwWbBudFclZ82BsiVQpojx4CKYRkdcSHZ&checksum=132485134303ef1bc7fcb136470a9e7f5bfc9419ae93').text
	#print(source)
	soup = bs4.BeautifulSoup(source,'lxml')
	#print(soup.prettify())
	get_detail_data(soup)

def get_detail_data(soup):
	title = soup.find('h1',id='itemTitle')
	print(len(title))
	print(title.text)
	subTitle = soup.find('h2',id='subTitle')
	print(subTitle.text)
	price = soup.find('span',id='mm-saleDscPrc')
	print(price.text)
	indianPrice = soup.find('span',id='convbidPrice')
	print(indianPrice.text)

	
	ima = soup.find_all('img',id='icImg') 
	ima = ima[1]['src']
				
	imgFile = open('temp.jpeg','wb')
	imgFile.write(urllib.request.urlopen(ima).read())
	imgFile.close()
					#mage = ima[1].img['src']
					#print(image)
				
				
			

if __name__ == '__main__':
	main()