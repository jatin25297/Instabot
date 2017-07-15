import requests

def check_comment(input):
    BASE_URL = "http://apis.paralleldots.com/"
    API_KEY = 'cHoGVxbSSxuEZMWPyWnYpUVfbrXbmUWbyTVNKIly2Vo'
    #input = raw_input("Enter the sentence:")
    url = BASE_URL + "sentiment?sentence1=" + input + "&apikey=" + API_KEY
    responce = requests.get(url).json()
    if responce["sentiment"] >=0.3:
        print "P:"+input
        return False
    else:
        print "N:" + input
        return True
    #print responce
#check_comment()
