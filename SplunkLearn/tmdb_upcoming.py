import requests as req
import json

def tmdb_api_call(requestURL, parameters):
    response = req.get(url=requestURL,params=parameters)
    if response.status_code != 200:
        print(response.json())
        exit()
    data = response.json()
    return json.dumps(data)

def get_upcoming_movies_by_page(api_key, page_number=1):
    requestURL = "https://api.themoviedb.org/3/movie/upcoming"
    parameters = {"api_key" : api_key, "page" : page_number }
    return tmdb_api_call(requestURL,parameters)

def main():
    api_key = "5bcacd05adb3b8df24f75c9b19c204bd"
    upcoming_movie_list = get_upcoming_movies_by_page(api_key,1)
    data = json.loads(upcoming_movie_list)
    # print is streaming to splunk 
    print(json.dumps(data["results"]))

if __name__ == "__main__":
    main()