import webbrowser
import re
import requests

url=str(input("Enter youtube url :"))

def extract_video_id(url):
    # The regular expression pattern to extract the video ID
    pattern = r"(?<=v=)[\w-]+|(?<=be/)[\w-]+"
    
    # Use regex to find the video ID in the URL
    match = re.search(pattern, url)
    
    if match:
        return match.group()
    else:
        return None
    
video_id = extract_video_id(url)
print(video_id) 

url="https://img.youtube.com/vi/"+str(video_id)+"/maxresdefault.jpg"
print(url)


def open_link_in_browser(link_url):
    webbrowser.open(link_url)

# Example usage
link_url = str(url)
open_link_in_browser(link_url)