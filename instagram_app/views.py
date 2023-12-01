from django.shortcuts import render
from datetime import datetime
import requests

def get_media(request):
    token = 'IGQWRPX3UzLXdrTTVOaVdJZAFp0aHI5ZAzBYT242M25FUHlFTmpPSmhzMUVFN09MN0F0eE0yTm1ReXRtYjZAhT1VMR3Y0YTMzU0pFaG5EVnczeGJmLVZAteGFIRWZAzTU9idmxuUDduN2c2M3pLLUFwTURaWmtvTGVNNmcZD'
    url = 'https://graph.instagram.com/me/media?fields=id,username,caption,timestamp&access_token='+token
    
    response = requests.get(url,)
    data = response.json()
    all_media = data['data']
    print(all_media)
    output = []
    for media in all_media:
        media_id = media["id"]
        media_uri = 'https://graph.instagram.com/'+media_id+'?fields=id,media_type,media_url,username,timestamp&access_token='+token
        response = requests.get(media_uri,)
        media_data = response.json()
        media["url"] = media_data["media_url"]
        media["type"] = media_data["media_type"]
        media["username"] = media_data["username"]
        timestamp_data = media_data["timestamp"]
        timestamp_datetime = datetime.strptime(timestamp_data, '%Y-%m-%dT%H:%M:%S%z')
        media["date"] = timestamp_datetime.strftime('%B %d, %Y')
        media["time"] = timestamp_datetime.strftime('%H:%M')

    
    return render (request, 'instagram.html', { "all_media": all_media} )


