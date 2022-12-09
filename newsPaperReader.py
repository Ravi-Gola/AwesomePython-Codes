import requests
from win32com.client import Dispatch

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


def technology_news():
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=318229509c7b45cdbeaafe8d6d405185')
    r = response.json()
    articles = r['articles']
    count = 1
    speak("Todays technology news are")
    for item in articles:
        newsTitle = item['title']
        speak(f"news {count}")
        speak(newsTitle)
        count = count + 1


def business_news():
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=318229509c7b45cdbeaafe8d6d405185')
    r = response.json()
    articles = r['articles']
    count = 1
    speak("Todays  business news are")
    for item in articles:
        newsTitle = item['title']
        speak(f"news {count}")
        speak(newsTitle)
        count = count + 1

def entertainment_news():
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=318229509c7b45cdbeaafe8d6d405185')
    r = response.json()
    articles = r['articles']
    count = 1
    speak("Todays  entertainment news are")
    for item in articles:
        newsTitle = item['title']
        speak(f"news {count}")
        speak(newsTitle)
        count = count + 1

def health_news():
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=318229509c7b45cdbeaafe8d6d405185')
    r = response.json()
    articles = r['articles']
    count = 1
    speak("Todays  health news are")
    for item in articles:
        newsTitle = item['title']
        speak(f"news {count}")
        speak(newsTitle)
        count = count + 1

def  science_news():
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=318229509c7b45cdbeaafe8d6d405185')
    r = response.json()
    articles = r['articles']
    count = 1
    speak("Todays  science news are")
    for item in articles:
        newsTitle = item['title']
        speak(f"news {count}")
        speak(newsTitle)
        count = count + 1

def sports_news():
    response = requests.get('https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=318229509c7b45cdbeaafe8d6d405185')
    r = response.json()
    articles = r['articles']
    count = 1
    speak("Todays  sports news are")
    for item in articles:
        newsTitle = item['title']
        speak(f"news {count}")
        speak(newsTitle)
        count = count + 1

if __name__ == '__main__':
    sports_news()









