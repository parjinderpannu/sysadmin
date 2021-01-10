import requests as req
import json

def tmdb_api_call(requestURL, parameters):
    response = req.get(url=requestURL,params=parameters)
    if response.status_code != 200:
        print(response.json())
        exit()
    data = response.json()
    return json.dump(data)

def main():
    pass

if __name__ == "__main__":
    main()