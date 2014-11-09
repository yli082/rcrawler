RCRAWLER
==========

Author & Contributor List
----------
Alexander Ortiz

Program Overview
----------
RCrawler is a basic web crawler written in Python. The project began as a
fun way for me to strength my Python programming skills, as well as SQL.

User's Guide
----------
To run RCrawler run the ```main.py``` file found in ```./src```. 
As the current verison stands, you will be asked to input a query. RCrawler will then crawl the predetermined
amount of pages, starting at the predetermined seed page. Once the crawling is complete a list of all links
associated with the query will be output. In addition to this output a databse that contains all of the word and
link assocations will be created.

Bus/Limitations
----------
* Can not enter custom seed page.
* Can not enter custom of pages to crawl.
* Can not opt out of creating a database.
