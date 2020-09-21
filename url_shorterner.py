#Importing the relavant libraries
import contextlib
from urllib.parse import urlencode
from urllib.request import urlopen
import argparse

def make_tiny(url):
    #Takes in a url to be shorterned and returns the shorterned url
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
    
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')

def main():
    #Makine the url shortener run on command line and prints out thr shortened url

    #Creating the CLI parser
    parser = argparse.ArgumentParser(description="Make tinyurls")

    #Adding the arguments for the parser
    parser.add_argument('Weblink', type = str, nargs='*', help="Website to make tiny")
    
    #Parse args for the parser
    args = parser.parse_args()

    #Making the tinyurls from the arguments parsed
    for url in vars(args)['Weblink']:
        print(make_tiny(url))


if __name__ == '__main__':
	main()