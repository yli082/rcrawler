import urllib2
import re
from bs4 import BeautifulSoup

#opens and reads the page associated with the passed in URL
def open_link(url):
    try:
        #print "Opening page - " + url
		
	#returns the contents of the page
        return urllib2.urlopen(url).read()
    except urllib2.HTTPError, error:
        #print "unable to open " + url
		
	#prints the HTTPError code
	#print error.read()
	print "Error: "	+ url
	#if unable to open or connect return the string "404" signifying that
	#the HTTP response code was indicative of an error causing an exception
        return "404"

#adds all of the words found on the page to the index with their update associated values
def add_to_index(page_url, page, index):
    #print "adding to index"
	
    #strips the entirety of the page into alphanumeric characters only, and 
    #replaces any non alphanumeric character with a ' '
    words_on_page = re.sub(r'\W+', ' ', page).split()
	
    #for each word found on the page
    for words in words_on_page:
	
	#sets in_in to be the bool of the word already being in the index
        in_it = words in index
		
	#if it is already in the index
        if in_it:
	    #if the page's URL is no already part of the value
            if page_url not in index[words]:
		#add the page's URL to the value, which is a list of associated URLs
                index[words].append(page_url)
        else:
	    #else create a new key:value pair with the word and page URL
            index[words] = [page_url]
			
#retrieves and returns all of the links on the passed in page
def get_all_links(page_url, page, links):
    #print "getting all links"
	
    #initialize the page as a BeautifulSoup object
    soup = BeautifulSoup(page)
	
    #for every element in the BeautifulSoup object which has an 'a' tag and an 'href' value
    for l in soup.find_all('a', href=True):
		
	#url is equal to the 'href' value 
        url = l['href']
	#the URL is set to all lower case
        url = url.lower()
		
	#if the URL is not a link to an image and it is not '/'
        if url != "/" and not(url.endswith(".jpg") or url.endswith(".png")):
	    #if the URL starts with '/' prefix the missing part of the URL
            if url.startswith('/'):
		      url = page_url + url
	    #if the URL does not start with 'http' prefix 'http/'
            elif not url.startswith('http'):
		      url = page_url + '/' + url
	    #if the URL is not already in the list of links to crawl add it
            if url not in links:
	           links.append(url)
    #return the new list of links to crawl
    return links
