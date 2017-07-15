import requests, urllib
from my_token import ACCESS_TOKEN
BASE_URL = "https://api.instagram.com/v1/"

def get_self_post():
    url = BASE_URL + "users/self/media/recent/?access_token="+ ACCESS_TOKEN
    self_media = requests.get(url).json()
    if self_media["meta"]["code"] == 200:
        if len(self_media["data"]):
            image_id = self_media["data"][0]["id"]
            image_url = self_media["data"][0]["images"]["standard_resolution"]["url"]
            urllib.urlretrieve(image_url, image_id + ".jpeg")
            return image_id
        else:
            print "No Recent Post exist"
            return -1
    else:
        print "Error" + self_media["meta"]["code"]
        return -1

def get_post_liked():
    url = BASE_URL + "users/self/media/liked/?access_token=" + ACCESS_TOKEN
    self_media = requests.get(url).json()
    if self_media["meta"]["code"] == 200:
        if len(self_media["data"]):
            image_id = self_media["data"][0]["id"]
            image_url = self_media["data"][0]["images"]["standard_resolution"]["url"]
            urllib.urlretrieve(image_url, image_id + ".jpeg")
            return image_id
        else:
            print "No Recent liked Media found"
            return -1
    else:
        print "Error" + self_media["meta"]["code"]
        return -1

def get_user_post(user_id):
    url = BASE_URL + "users/" + user_id + "/media/recent/?access_token=" + ACCESS_TOKEN
    self_media = requests.get(url).json()
    if self_media["meta"]["code"] == 200:
        if len(self_media["data"]):
            image_id = self_media["data"][0]["id"]
            image_url = self_media["data"][0]["images"]["standard_resolution"]["url"]
            urllib.urlretrieve(image_url, image_id + ".jpeg")
            return image_id
        else:
            print "No Recent Post exist"
            return -1
    else:
        print "Error" + self_media["meta"]["code"]
        return -1


