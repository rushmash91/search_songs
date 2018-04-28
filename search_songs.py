import requests
from auth import auth


def main():
    song = input('Track to Search : ')
    key = auth()
    url_m = 'http://ws.audioscrobbler.com/2.0/?method=track.search&track=' + song + '&api_key=' + key + '&format=json'

    res = requests.get(url_m)

    res_json = res.json()

    total = res_json['results']['opensearch:totalResults']

    print(f"Total Number of Tracks Found : {total}")

    results = res_json['results']['trackmatches']['track']

    for i in range(len(results)):
        name = results[i]["name"]
        artist = results[i]["artist"]
        url = results[i]["url"]
        listeners = results[i]["listeners"]
        print(f'{i+1} : {name}\n')
        print(f'     By {artist}\n')
        print(f'     {url} \n')
        print(f'     {listeners} \n\n\n')


if __name__ == "__main__":
    main()
