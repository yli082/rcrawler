import webcrawler

def main():

    while True:
        ###various seed pages
	#SEED_PAGE = 'http://www.reddit.com'
	#SEED_PAGE = 'http://www.dmoz.org'
	#SEED_PAGE = "http://www.cnn.com/"
	#SEED_PAGE = 'http://www.google.com/asdfsf'
	SEED_PAGE ="http://www.about.com/"
	
	#max number of pages allowed to crawl
	MAX_PAGES = 5000
		
	#user's query
	user_input = raw_input("Enter query: ")
	    
	#if input is not the ext command continue
	if user_input != ".exit":	
            #calls the webcrawler.query function on the users input with the given seed page and max amount of
	    #pages allowed to be crawled
	    #webcrawler.query function returns a list of of URLs associated with the users queried term
	    index = webcrawler.query(user_input, MAX_PAGES, SEED_PAGE)
			
	    #prints the query results
	    print index
            #else terminate the program 
        else:
	    return

if __name__ == "__main__":
    main()
