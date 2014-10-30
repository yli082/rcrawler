RCRAWLER
==========

Licensing information: See LICENSE
---
Source can de downloaded from https://github.com/aorti017/rcrawler.git
---

Author & Contributor List
----------
Alexander Ortiz

Program Overview
----------
RCrawler is a basic web crawler written in Python. The project began as a
fun way for me to strength my Python programming skills, but I have decided to open
it up to the open source community.

File List
----------
```
.:

src

LICENSE

README.md
```
```
./src:

db_interface.py

main.py

page_interface.py

webcrawler.py
```

User's Guide
----------
To run RCrawler simply run the ```main.py``` file found in ```./src```. As the current
verison stands, you will be asked to input a query. RCrawler will then crawl the predetermined
amount of pages, starting at the predetermined seed page. Once the crawling is complete a list of all links
associated with the query will be output. In addition to this output a databse that contains all of the word and
link assocations will be created.

Bus/Limitations
----------
* Can not enter custom seed page.
* Can not enter custom of pages to crawl.
* Can not opt out of creating a database.
