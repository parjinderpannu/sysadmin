import sys,os
import requests as req
import json

def tmdb_api_call(requestURL, parameters):
    response = req.get(url=requestURL,params=parameters)
    if response.status_code != 200:
        print('status:', response.status_code, 'Headers: ', response.headers, 'Error Response: ',response.json())
        exit()
    data = response.json()
    return json.dumps(data)

def get_upcoming_movies_by_page(api_key, page_number=1):
    requestURL = "https://api.themoviedb.org/3/movie/upcoming"
    parameters = {"api_key" : api_key, "page" : page_number }
    return tmdb_api_call(requestURL,parameters)

def checkpoint(checkpoint_file,movie_id):
    with open(checkpoint_file,'r') as file:
        id_list = file.read().splitlines()
        return (movie_id in id_list)

def write_to_checkpoint_file(checkpoint_file,movie_id):
    with open(checkpoint_file,'a') as file:
        file.writelines(movie_id + "\n")


def stream_to_splunk(checkpoint_file,data):
    for dt in data:
        if checkpoint(checkpoint_file,str(dt["id"])):
            continue
        else:
            write_to_checkpoint_file(checkpoint_file,str(dt["id"]))
            print(json.dumps(dt))

def main():
    api_key = "5bcacd05adb3b8df24f75c9b19c204bd"
    checkpoint_file = os.path.join(os.environ["SPLUNK_HOME"],'etc','apps','tmdb','bin','checkpoint','checkpoint.txt')
    # checkpoint_file = os.path.join('/Users','ppannu','code','personal','sysadmin','SplunkLearn','checkpoint','checkpoint.txt')
    upcoming_movie_list = get_upcoming_movies_by_page(api_key,1)
    data = json.loads(upcoming_movie_list)
    # print is streaming to splunk 
    # print(json.dumps(data["results"]))
    stream_to_splunk(checkpoint_file,data["results"])

if __name__ == "__main__":
    main()