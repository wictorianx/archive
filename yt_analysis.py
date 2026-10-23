import pandas as pd
import matplotlib.pyplot as plt
from googleapiclient.discovery import build
import isodate

API_KEY = '' # Paste your key here
PLAYLIST_ID = 'PLLLJo1sUuUjvuYyhdo_07nO10ScMgei4G'

def get_full_playlist(api_key, playlist_id):
    print("Connecting to YouTube API...")
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    video_data = []
    next_page_token = None
    
    while True:
        # 1. Get a page of 50 videos from the playlist
        pl_request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        pl_response = pl_request.execute()
        
        # Extract the video IDs
        video_ids = [item['contentDetails']['videoId'] for item in pl_response['items']]
        
        if not video_ids:
            break
            
        # 2. Ask the API for the exact lengths of those 50 videos
        vid_request = youtube.videos().list(
            part='contentDetails,snippet',
            id=','.join(video_ids)
        )
        vid_response = vid_request.execute()
        
        # 3. Store the data
        for item in vid_response['items']:
            duration_iso = item['contentDetails']['duration']
            duration_sec = isodate.parse_duration(duration_iso).total_seconds()
            title = item['snippet']['title']
            
            video_data.append({
                'title': title, 
                'duration_min': duration_sec / 60
            })
            
        print(f"Fetched {len(video_data)} videos so far...")
            
        # Check if there is another page of results
        next_page_token = pl_response.get('nextPageToken')
        if not next_page_token:
            break
            
    return pd.DataFrame(video_data)

# --- Execution ---
try:
    df = get_full_playlist(API_KEY, PLAYLIST_ID)
    print(f"\nSuccess! Total videos retrieved: {len(df)}")
    
    plt.figure(figsize=(15, 6))
    plt.bar(range(len(df)), df['duration_min'], color='darkred')
    plt.xlabel('Video Index (Order in Playlist)')
    plt.ylabel('Duration (Minutes)')
    plt.title(f'Seksenler Playlist Video Lengths ({len(df)} Episodes)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"API Error: {e}")
