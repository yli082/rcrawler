import db_interface
import page_interface
import webcrawler

#crawls over my butt designated amount of pages beginning at the specified seed page
def run_crawler(SEED_PAGE, MAX_PAGES):
	
    #sets the current page URL to be that of the seed page
    page_url = SEED_PAGE
    #page_interface.open_link then opens the page and stores its
    #contents in the page variable
    page = page_interface.open_link(page_url)

    #initializes the crawled count, links, and index variables
    count = 0
    links = []
    index = {}
	
    #while the crawled pages count does not equal the max amount of
    #pages allowed to be crawled continue
    while count != MAX_PAGES:
		
	#passes the links variable into page_interface.get_all_links to add all of the links
	#on the current URL's page that are not already in the links variable
        page_interface.get_all_links(page_url, page, links)
		
	#passes the index variable into page_interface.add_to_index to update the dictionary
	#with the words found on the current page(key) and by adding the current URL 
	#to the list of all other URLs associated with that word(value)
        page_interface.add_to_index(page_url, page, index)
		
	#if there are no more pages to crawl return the index
        if len(links) <= 0:
            return index
		
	#set page_url to be the first URL contained in the links variable
        page_url = links[0]
	#then remove that URL from the list of URls to be crawled
        links.pop(0)
		
	#page_interface.open_link then opens the page and stores its
	#contents in the page variable
        page = page_interface.open_link(page_url)
		
	#while the page is returning a HTTP code that signals
	#that a connection could not be made, try the next available URL
	#in the list of URLs to be crawled
        while page == "404":
            page_url = links[0]
            links.pop(0)
            page = page_interface.open_link(page_url)
		
	#increase the count of pages crawled
        count += 1
        #print count
    #updates the database with the data retrieved from crawling     
    db_interface.update_db(index)

    #returns the index 
    return index

#handles the user's queries
def query(KEY, MAX_PAGES, SEED_PAGE):
    #splits the user's query by its spaces
    words = KEY.split(' ')
	
    #if the query is empty return
    if not words:
        return
		
    #initializes the lists used to create the query
    query_unrefined = []
    query_refined = []
	
    #runs the web crawler 
    index = webcrawler.run_crawler(SEED_PAGE, MAX_PAGES)
	
    #for each word in the user's query
    #append the list of URLs associated with the word to the unrefined results
    for w in words:
        query_unrefined.append(index[w])
		
    #if there are no results return
    if len(query_unrefined) == 0:
        return
    #if there is only one set of results return that set
    elif len(query_unrefined) == 1:
        return query_unrefined
    #if there are multiple sets of results continue
    elif len(query_unrefined) > 1:
		
	#sets the main comparison list to be the first set of results in the list
        main_list = query_unrefined[0]
	#then removes that set from the list of sets of results
        query_unrefined.pop(0)
		
	#for each result in the main_list variable
        for i in main_list:
	    #for each other result set in the list of result sets
            for j in query_unrefined:
		#if the current result is in the set add it to the refined results
                if i in j:
                    query_refined.append(i)
    #return the refined results
    return query_refined

#okay to compare all the result sets to the first result set because if the result pertains to all words
#in the query it would show up in each respective result set, other wise the results may only be relevant
#to parts of the query or provide unrelated results 
#e.g. "The big gold fish" would return results related to "the fish", "the big", "big gold", etc.
#instead of "The big gold fish"
