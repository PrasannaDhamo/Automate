import requests
import json

#api_key = input("Enter yout API_Token : ")
api_key = 'k_T9X2nfj1'
id_url = 'https://imdb-api.com/en/API/SearchMovie/'
movie_url = 'https://imdb-api.com/en/API/Title/'
title = input("Enter Movie title : " )

url = id_url + api_key + '/' + title

def movie_details():
    title_response = requests.get(url)
    title_jsonResponse = title_response.json()
    id_no = (title_jsonResponse['results'][0]['id'])
    
    details_url = movie_url + api_key + '/' + id_no
    
    movie_response = requests.get(details_url)
    movie_jsonResponse = movie_response.json()
    details = json.dumps(movie_jsonResponse, indent=4)
    return details

print(movie_details())
print("Json response of " + title +" movie details is saved in the current folder as text document")

save = open(title+'.txt', "w")
save.write(movie_details())
save.close()
