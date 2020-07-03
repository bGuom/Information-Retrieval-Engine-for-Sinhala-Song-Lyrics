# Information-Retrieval-Engine-for-Sinhala-Song-Lyrics
Search engine for a Sinhala songs lyrics

## Description
This Repo contain the project source code files of the 
* Sinhala song lyric Search engine built using [ElasticSearch](https://www.elastic.co/elasticsearch/) 
* Web Scraping script built using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Get Started
* Building the Lyrics Corpus  
  Use the scrapingTool.py located in Sinhala song lyrics scraping tool/ to scrape the website which includes the Sinhala Lyrics
* Convert scraped CSV data file to json using any online tool
* Download [ElasticSearch](https://www.elastic.co/downloads/elasticsearch)
* Extract the zip file, open the bin folder and run ElasticSearch
* Verify whether the ElasticSearch is running by visiting http://localhost:9200/ 
* Use SearchTool.py in ElasticSearch folder to test your queries

## Supported Featues
* Search by song title, artist name, music composer, melody and lyrics author.
* Search by song content
* Support both English and Sinhala search queries
* Faceted search for filtering artist,music,melody and lyrics author
* Search for lyrics using Youtube video id

## Indexing and Quering
* Text classification
* Boosting

## Attributes of the results

For detaied descriptions, Please refer the `README.md` file in project folders
* --Sinhala song lyrics scraping tool
* --ElasticSearch


## Version
- Version : 1.0
- Last Scraped : 24/June/2020
