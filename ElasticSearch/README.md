# ElasticSearch 
Search engine for a Sinhala songs lyrics

## Description
This folder contains the elastic search implementaion for the Sinhala song lyrics search engines. This is implented as a python script where it can be extended to Django or Flask app to create REST API for enabling the use of this search engine with a frontend application

## Setting Up
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
### Text classification
Identify keywords in the search query and return most appropriate search results using boosting techniques. 

* Search for artist using keywords :
```ජෝතිපාල  ගායකයා``` OR ```ජෝතිපාල  ගැයු ගීත ```
* Search for music composer using keywords :
```සංගීතය ක්ලැරන්ස් විජේවර්ධන``` 
* Search for melody composer using keywords :
```ප්‍රියා සූරියසේන තනු නිර්මාණය කල ගීත``` 
* Search for music composer using keywords :
```මහගම සේකර රචිත ගීත``` 

### Boosting

  Boosting is used to refine the search results by analysing the search query and bossting fields related to the search query.
  
  For example :
  
  * Search for song in Sinhala unicode query boost Sinhala text fields
  * Search for song in English query boost English text fields
  * Sraching for youtube video id with youtube keyword boost videoId field
  
 ### Faceted Search
 
 Facted search also known as aggregated search results are implemented using ElasticSeach aggregated queries. In queryGenerator.py file
 
 ```
 query = {
		"size": 10,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": operator,
				"type": "best_fields"
			}
		},
		"aggs": {
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
                        "Music Filter": {
				"terms": {
					"field": "music.keyword",
					"size": 10
				}
			},
                        "Melody Filter": {
				"terms": {
					"field": "melody.keyword",
					"size": 10
				}
			},
                        "Lyrics Author Filter": {
				"terms": {
					"field": "lyrics_author.keyword",
					"size": 10
				}
			}
		}
 ```
 



## Attributes of the results

Search result will returns a list of song details related to the search query along with facted search results. Each song detail will provide following fields.

1. ```lyric_id``` - unique lyric identifier (integer)
2. ```title``` - song title containg both Enlish and Sinhala 
3. ```title_sinhala``` - song title in Sinhala (Unicode) 
4. ```title_english``` - song title in English
5. ```artist``` - song artist name
6. ```music``` - music composer's name
7. ```melody``` - author's name of the melody
8. ```lyrics_author``` - authour's name of the lyrics
9. ```image_url``` - url for song cover image
10. ```video_url``` - Youtube video url
11. ```youtube_video_id``` - Youtube video id
12. ```lyrics``` - song lyrics in Sinhala Unicode


## Version
- Version : 1.0
- Last Scraped : 24/June/2020
