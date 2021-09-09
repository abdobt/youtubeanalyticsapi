from googleapiclient.discovery import build
import pandas as pd
from googleapiclient import discovery
youtubeapikey=""
youtube=build('youtube','v3',developerKey=youtubeapikey)
#stats=youtube.channels().list(part='statistics',id='').execute()
#stats=youtube.search().list(part='snippet',channelId=').execute()
#stats2=youtube.videos().list(part='statistics',id=stats["items"][1]["id"]["videoId"]).execute()
#print(stats2)
import google_auth_oauthlib.flow
import os
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

scopes = ['https://www.googleapis.com/auth/yt-analytics.readonly',
          'https://www.googleapis.com/auth/yt-analytics-monetary.readonly',
          'https://www.googleapis.com/auth/youtube.readonly']

api_service_name = "youtubeAnalytics"
api_version = "v2"
client_secrets_file = "client_secret_desktop.json"
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_console()
youtube_analytics = discovery.build(
    api_service_name, api_version, credentials=credentials)

request = youtube_analytics.reports().query(
    dimensions="deviceType",
    endDate="2021-06-30",
    ids="channel==MINE",
    maxResults=8,
    metrics="views",
    startDate="2014-05-01"
)

res = request.execute()
print(res)
from IPython.display import JSON

JSON(res, expanded=True)
request = youtube_analytics.reports().query(
    dimensions="day",
    endDate="2021-06-01",
    ids="channel==MINE",
    maxResults=8,
    metrics="views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost,shares,comments",
    startDate="2021-05-01"
)

res = request.execute()
print(res)
request = youtube_analytics.reports().query(
    dimensions="video",
    endDate="2021-06-30",
    ids="channel==MINE",
    maxResults=10,
    metrics="views,comments,likes,shares,dislikes,estimatedMinutesWatched,averageViewPercentage,subscribersGained,subscribersLost",
    sort="-views",
    startDate="2014-05-01"
)

res = request.execute()
print(res)
rows=res["rows"]
df = pd.DataFrame(rows)
df.columns =['video','views','comments','likes','shares','dislikes','estimatedMinutesWatched','averageViewPercentage','subscribersGained','subscribersLost']
print(df)
