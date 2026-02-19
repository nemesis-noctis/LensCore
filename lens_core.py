import random

import requests
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import (
    ComputerVisionErrorResponseException,
)
from msrest.authentication import CognitiveServicesCredentials

AZURE_VISION_ENDPOINT="https://lenscore.cognitiveservices.azure.com/"

class Song:
    def __init__(self, id, name, artist, song_url, album_cover_url, rank):
        self.id = id
        self.name = name
        self.artist = artist
        self.song_url = song_url
        self.album_cover_url = album_cover_url
        self.rank = rank
        

class LensCore:
    def __init__(self, api_key):
        self.computervision_client = ComputerVisionClient(AZURE_VISION_ENDPOINT, CognitiveServicesCredentials(api_key))
        
        
    def get_tags_from_img(self, img_file_path, lang):
        '''
        Returns a list of tags from the Azure Vision API based on an image in the selected language. If the file is invalid or
        no tags are found, it returns None.
        
        :param img_file_path: An image in a valid format.
        
        :param lang: Language for searching tags.
        '''
        local_image = open(img_file_path, "rb")
        try:
            image_tags_response = self.computervision_client.tag_image_in_stream(local_image, language=lang)
        
        except ComputerVisionErrorResponseException:
            print("Invalid File, returned None.")
            return None
        
        else:
            if len(image_tags_response.tags) == 0:
                print("No tag found, returned None")
                return None
            
            image_tags_list = [tag.name for tag in image_tags_response.tags]
            return image_tags_list
            
            
    def select_tags_to_search(self, tags:list):
        '''
        Returns a list of up to 5 tags from the tags received, with the first being the one with the highest confidence and the others being random.
        If an invalid value is received for tags, returns None.
        
        :param tags: list of tags to be selected.
        :type tags: list
        '''
        if tags is None or tags == []:
            print("No tags provided, returned None.")
            return None
        
        max_tags_number = min(len(tags), 5)
        tags_number = random.randint(1, max_tags_number)
        
        tags_to_search = []
        tags_to_search.append(tags[0])
        
        if tags_number > 1:
            others = random.sample(tags, tags_number - 1)
            tags_to_search.extend(others)
        
        return tags_to_search
        
    
    def search_songs(self, tags:list):
        '''
        Searches for songs based on tags using the Deezer API and returns Song objects for each song with its data. 
        If no song is found or an invalid value is received for tags, returns None.
        
        :param tags: List of tags to search for.
        :type tags: list
        '''
        if tags is None or tags == []:
            print("No valid tags received, returned None")
            return None
        
        tags_formated = " ".join(tags)
        
        headers={"User-Agent": "LensCore/1.0 (https://github.com/nemesis-noctis)" }
        params={"q": tags_formated}
        
        deezer_endpoint = "https://api.deezer.com/search/track"
        response = requests.get(url=deezer_endpoint, params=params, headers=headers)
        response.raise_for_status()
        
        songs_search_result = response.json()["data"]
        
        if songs_search_result == []:
            print("No Music found, returned None")
            return None
            
        songs_searched = [Song(id=song["id"],
                            name=song["title_short"], 
                            artist=song["artist"]["name"], 
                            song_url=song["link"], 
                            album_cover_url=song["album"]["cover_big"], 
                            rank=song["rank"],) for song in songs_search_result]
        
        return songs_searched    
            