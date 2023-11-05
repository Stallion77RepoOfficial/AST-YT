from apiclient.discovery import build
from isodate import parse_duration
import datetime

api_key = ""  # YouTube API'N
youtube = build('youtube', 'v3', developerKey=api_key)

start_date_input = input("Başlangıç tarihi girin (YYYY-MM-DD): ")
end_date_input = input("Bitiş tarihi girin (YYYY-MM-DD): ")

start_date = datetime.datetime.strptime(start_date_input, "%Y-%m-%d").isoformat() + "Z"
end_date = datetime.datetime.strptime(end_date_input, "%Y-%m-%d").isoformat() + "Z"

keywords = input("Anahtar kelimeleri virgülle ayırarak girin: ").split(',')

max_results = int(input("Kaç adet video gösterilsin?: "))
max_duration = int(input("Maksimum video uzunluğu (dakika): ")) * 60
min_views = int(input("Minimum izlenme sayısı: "))

age_restricted = input("Sadece yaş kısıtlamalı videoları göster (E/H): ")
if age_restricted.lower() == 'e':
    age_restricted = True
else:
    age_restricted = False

video_found = False

for keyword in keywords:
    request = youtube.search().list(
        part="snippet",
        maxResults=max_results,
        q=keyword,
        type="video",
        publishedAfter=start_date,
        publishedBefore=end_date,
        videoEmbeddable="true",
        videoSyndicated="true"
    )
    response = request.execute()
    for item in response['items']:
        video_id = item['id']['videoId']
        video_request = youtube.videos().list(
            part="contentDetails,statistics",
            id=video_id
        )
        video_response = video_request.execute()
        content_rating = video_response['items'][0]['contentDetails'].get('contentRating',{})
        duration = parse_duration(video_response['items'][0]['contentDetails']['duration']).total_seconds()
        views = int(video_response['items'][0]['statistics']['viewCount'])
        if 'ytRating' in content_rating and content_rating['ytRating'] == 'ytAgeRestricted' and duration <= max_duration and views >= min_views:
            if age_restricted:
                print('https://www.youtube.com/watch?v=' + video_id)
                video_found = True
        elif not age_restricted and ('ytRating' not in content_rating or content_rating['ytRating'] != 'ytAgeRestricted') and duration <= max_duration and views >= min_views:
            print('https://www.youtube.com/watch?v=' + video_id)
            video_found = True

if not video_found:
    print("Video bulunamadı.")