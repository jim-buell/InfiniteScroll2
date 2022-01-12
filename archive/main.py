#main.py

from newsapi import NewsApiClient

def getNewHeadlines():
	# Init
	newsapi = NewsApiClient(api_key='2a547104c0d14649850d41b220871320')

	# /v2/top-headlines
	top_headlines = newsapi.get_top_headlines(country='us')
	#										  pageSize=20)
	return top_headlines

def formatHeadlines():
	top_headlines = getNewHeadlines()
	Headlines = top_headlines['articles']
	headlineList = []
	if Headlines:
			for articles in Headlines:
				b = articles['title'][::-1].index("-")
				if "news" in (articles['title'][-b+1:]).lower():
					headlineList.append(f"{articles['title'][:-b-2]}.")
				else:
					headlineList.append(f"{articles['title'][:-b-2]}.")
			for item in headlineList:
				print(item) 
	else:
		exit()
		
def writeFile():
	headlineList = formatHeadlines()
	f = open("/Users/jbuell/Dropbox (IDEO)/00 Jim's Dropbox/Python/Infinite Scroll 2/masterHeadlines.txt", "a")
	for element in headlineList:
		f.write(element + "\n")
	else:
		f.close()
		
		
def mainPrompt():
	getNew = input("Do you want to get new headline results? y or n? ")
	if getNew == "y":
		getNewHeadlines()
		print("It was yes.")
	formatHeadlines(),
	writeFile()
	

#mainPrompt()
writeFile()