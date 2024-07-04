import requests

#function to get youTube search query
def get_all_youtube_videos(api_key, query, max_results=50):
    search_url = "https://www.googleapis.com/youtube/v3/search"
    videos = []
    next_page_token = None

    while True:
        params = {
            'part': 'snippet',
            'q': query,
            'type': 'video',
            'maxResults': max_results,
            'key': api_key,
            'pageToken': next_page_token
        }
        
        response = requests.get(search_url, params=params)
        if response.status_code == 200:
            result = response.json()
            videos.extend(result.get('items', []))
            next_page_token = result.get('nextPageToken')
            if not next_page_token:
                break
        else:
            print("Failed to fetch data from YouTube API")
            break
    
    return videos

api_key = 'AIzaSyBLwEA35tXQQmx2tXiaEMCUcXh-7atylTU' #API Key
query = 'Bose QuietComfort Ultra' #keywords
max_results = 50  # Maximum results per request

all_videos = get_all_youtube_videos(api_key, query, max_results)

# Displaying video titles and IDs
for video in all_videos:
    title = video['snippet']['title']
    video_id = video['id']['videoId']
    print(f"Title: {title}, Video ID: {video_id}")