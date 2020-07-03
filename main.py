import os
import sys
import time
import speech_recognition as sr
import webbrowser
from googleapiclient.discovery import build
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

# Google API and speech recognition initialization
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
youtube = build('youtube', 'v3', developerKey=GOOGLE_API_KEY)
r = sr.Recognizer()
mic = sr.Microphone()


def get_audio():
    with mic as source:
        # Tweaking sound recognition to filter out background noise
        r.dynamic_energy_threshold = False
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 1200
        print('Puhu....')
        audio = r.listen(source)
        print(audio)
        voice_data = ' '
        try:
            voice_data = r.recognize_google(audio, language='fi-FI')
            print(voice_data)
        except sr.UnknownValueError:
            print('I did not get that.')
        except sr.RequestError:
            print('Sorry, we have some techinal difficulties.')
        return voice_data


def send_response(vd):
    if vd.startswith('video '):
        query = vd.split(' ', 1)
        query_response = get_video(query[1])
        if query_response['items']:  # User's query finds videos
            video_id = query_response['items'][0]['id']['videoId']
        else:
            return print('We found no videos with your request. :-/')
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        webbrowser.get().open(video_url)
    # Ends the program
    if vd == 'exit':
        sys.exit()


def get_video(query):
    # pylint: disable=maybe-no-member
    req = youtube.search().list(q=query, type='video', maxResults=1, part='snippet')
    res = req.execute()
    return res


while True:
    voice_data = get_audio()
    send_response(voice_data)
