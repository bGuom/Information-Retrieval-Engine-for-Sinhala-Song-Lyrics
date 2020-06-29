from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json
import queryGenerator as qG


es = Elasticsearch(HOST="http://localhost",PORT=9200)




def createIndex(index):
    return es.indices.create(index=index,ignore=400)

def deleteIndex(index):
    return es.indices.delete(index=index)


def read_corpus():
    with open('Sinhala_Unicode_Song_Lyrics_Corpus.json','r') as f:
        data = json.loads(f.read())
        return data

def genLyricData(dataArray,indexName):
    for lyricData in dataArray:

        lyric_id = lyricData.get("lyric_id",None)
        title = lyricData.get("title",None)
        title_sinhala = lyricData.get("title_sinhala",None)
        title_english = lyricData.get("title_english",None)
        artist = lyricData.get("artist",None)
        music = lyricData.get("music",None)
        melody = lyricData.get("melody",None)
        lyrics_author = lyricData.get("lyrics_author",None)
        image_url = lyricData.get("image_url",None)
        video_url = lyricData.get("video_url",None)
        youtube_video_id = lyricData.get("youtube_video_id",None)
        lyrics = lyricData.get("lyrics",None)


        yield {
            "_index": indexName,
            "_id":lyric_id,
            "_source": {
                "title_sinhala": title_sinhala,
                "title_english": title_english,
                "artist": artist,
                "music": music,
                "melody": melody,
                "lyrics_author": lyrics_author, 
                "youtube_video_id": youtube_video_id,
                "lyrics": lyrics
            },
        }


def init(indexName):
    if(es.indices.exists(index=indexName)==False):
        createIndex(indexName)
    helpers.bulk(es,genLyricData(read_corpus(),indexName))
    

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
    

def search(search_query):
    
    artist_keywors = ['Artist','Singer','artist','singer','ගායකයා','ගයනවා','ගායනා','ගැයු','ගයන']
    music_keywors = ['Music','Composer','music','composer','සංගීතය','සංගීත','තාලය']
    melody_keywords = ['Melody','melody','තනු නිර්මාණය','තනු','තනුව']
    lyrics_author_keywords = ['lyrics by','ගත්කරු','රචකයා','ලියන්නා','ලියන','රචිත','ලියපු','ලියව්‌ව','රචනා','ගී පද','ගේය පද']
    
    boost = {
        "title_sinhala":1,
        "title_english":1,
        "artist":1,
        "music":1,
        "melody":1,
        "lyrics_author":1,
        "youtube_video_id":1,
        "lyrics":1
        }

    if(isEnglish(search_query)):
        boost["title_english"] += 1
        if("youtube" in search_query.lower()):
            boost["youtube_video_id"] += 2
    else:
        boost["title_sinhala"] += 1
        boost["artist"] += 1
        boost["music"] += 1
        boost["melody"] += 1
        boost["lyrics_author"] += 1
        boost["lyrics"] += 1

        for key in artist_keywors:
            if(key in search_query):
                boost["artist"] += 1

        for key in music_keywors:
            if(key in search_query):
                boost["music"] += 1

        for key in melody_keywords:
            if(key in search_query):
                boost["melody"] += 1

        for key in lyrics_author_keywords:
            if(key in search_query):
                boost["lyrics_author"] += 1

        if(len(search_query.split())>5):
            boost["lyrics"] += 5

              
    field1 ="title_sinhala^{}".format(boost["title_sinhala"])
    field2 ="title_english^{}".format(boost["title_english"])
    field3 ="artist^{}".format(boost["artist"])
    field4 ="music^{}".format(boost["music"])
    field5 ="melody^{}".format(boost["melody"])
    field6 ="lyrics_author^{}".format(boost["lyrics_author"])
    field7 ="youtube_video_id^{}".format(boost["youtube_video_id"])
    field8 ="lyrics^{}".format(boost["lyrics"])

        
    boostedFields = [field1,field2,field3,field4,field5,field6,field7,field8,"title","image_url","youtube_video_id"]

    print("==================================================================================")    
    print (boost)
    print("==================================================================================") 
    res = es.search(index="song_lyrics_index",body=qG.getMultiMatchAgg(search_query,boostedFields))
    return res


    

def pySearch(query):
    res = search(query)
    for hit in res['hits']['hits']:
            print("Song Title : ")
            print(hit.get("_source").get("title_sinhala"))
            print(hit.get("_source").get("title_english"))
            print("Song Artist : ")
            print(hit.get("_source").get("artist"))
            print("Song Music Producer : ")
            print(hit.get("_source").get("music"))
            print("Song Melody : ")
            print(hit.get("_source").get("melody"))
            print("Song Lyrics Authour : ")
            print(hit.get("_source").get("lyrics_author"))
            #print("Song Image URL : ")
            #print(hit.get("_source").get("image_url"))
            #print("Song Youtube Video URL : ")
            #print(hit.get("_source").get("video_url"))
            print("Song Youtube Video ID : ")
            print(hit.get("_source").get("youtube_video_id"))
            print("Song Lyrics : ")
            print((hit.get("_source").get("lyrics")))

            print("===================================================================================\n\n")

#deleteIndex("song_lyrics_index")
init("song_lyrics_index")
#pySearch("Athma Liyanage")
#pySearch("පලංචියේ ලී ඉරුවේ")
#pySearch("Palanchiye lee iruwe")
#pySearch("දිවි කතරට ගංගාවයි මට හමුවූ ගංගා")
#pySearch("ganga")
#pySearch("ජය")
#pySearch("Artist song melody ජය ")
#pySearch("ගායකයා සංගීතය ජය ")
#pySearch("youtube d0CB3nSDHtg")


