#! /usr/bin/python3
import requests, bs4, sys, urllib.parse, argparse

# Setting up Argparser for commandline arguments
parser = argparse.ArgumentParser(description='Downloads text data from a subreddit of your choice')
parser.add_argument("-n", "--number", help="Number of results to return (Max 25)", action="store")
parser.add_argument("-s", "--search", help="String to search", action="store")
args = parser.parse_args()
num = args.number

if args.search is None:
	print("You have to provide a search term")
	sys.exit()

search = urllib.parse.quote(''.join(args.search)).replace('%20','+')
res = requests.get('https://duckduckgo.com/html?q='+search, {'User-Agent': 'DuckDuckGogler'})
soup = bs4.BeautifulSoup(res.text, 'html.parser')
if "If this error persists, please let us know: ops@duckduckgo.com" in soup:
	print("Sorry, sometimes duckduckgo doesn't want to work properly. Try running the script again.")
	sys.exit()
print(num)
results = soup.select('.web-result')
rnum = 0

if num is not None:
	for i in results:
		rnum += 1
		info = []
		for item in i.text.splitlines():
			if item.startswith("                  "):
				item = item.replace("                  ","")
			if not item == '' and not item == ' ':
				info.append(item)
		link = i.a['href'].replace("/l/?kh=-1&uddg=","")
		if rnum <= int(num):
			print('\n\033[96m'+str(rnum)+': \033[92m'+info[0]+'\033[0m')
			print('\033[93m'+urllib.parse.unquote(link)+'\033[0m')
			print(info[1]+'\n')

else:
	for i in results:
		rnum += 1
		info = []
		for item in i.text.splitlines():
			if item.startswith("                  "):
				item = item.replace("                  ","")
			if not item == '' and not item == ' ':
				info.append(item)
		link = i.a['href'].replace("/l/?kh=-1&uddg=","")
		print('\n\033[96m'+str(rnum)+': \033[92m'+info[0]+'\033[0m')
		print('\033[93m'+urllib.parse.unquote(link)+'\033[0m')
		print(info[1]+'\n')