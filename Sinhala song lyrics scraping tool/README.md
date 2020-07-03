
# Sinhala-Song-Lyrics-Scraping-Tool

## Description
This python script is written using Beautiful soup libarary. This script can scrape https://geepadura.blogspot.com blog site and retrieve Sinhala song lyrics data along with 11 other meta fields. Scraped song details are saved in a csv file each row containing details of a singele song.

## Attributes

Each row contains following fields related to the song. Missing values will be a empty string.

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


## Usage


Use ```getSongData(arg1,arg2,arg3)``` method to scrape the website.

This method requires three arguments

1. arg1 - Destination file name 
2. arg2 - Starting year for scraping
3. arg3- Finishing year for scraping

Example
```getSongData('Sinhala_Unicode_Song_Lyrics_Corpus.csv',2020,2009)```
