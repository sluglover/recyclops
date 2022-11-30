#!/usr/bin/env python3
import requests
import csv
import json


"""
call apple maps api to perform geocoding 
"""
def main():
    """
    hijacked api key found at https://gps-coordinates.org/coordinate-converter.php
    No encryption in headers and written in PHP, must be losers ...
    """
    stolenKey = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9" \
                ".eyJpc3MiOiJtYXBzYXBpIiwidGlkIjoiMk01MzgyRkRKTiIsImFwcGlkIjoiMk01MzgyRkRKTi5tYXBzLm9yZy5ncHMtY29vcmRpbmF0ZXMiLCJpdGkiOmZhbHNlLCJpcnQiOmZhbHNlLCJpYXQiOjE2Njk3NTIzNzksImV4cCI6MTY2OTc1NDE3OSwib3JpZ2luIjoiaHR0cHM6Ly9ncHMtY29vcmRpbmF0ZXMub3JnIn0.nn8ilcyyvB1FecQVFkx62IxbLCyIIjFBzR4V5Mgw0CH72Nt_HBQyOn3FGr02PIBNIceSH5pysAPU3qJu59KU7Q "

    with open("db.csv", "r") as f:
        reader = csv.reader(f)

        for i, line in enumerate(reader):
            address = line[2].splitlines()

            if len(address) < 0 or ("Various" or "Multiple " in address[0]):
                print(f"{i}, N/A")
                continue

            # - construct the request URL and encode
            url = f"https://api.apple-mapkit.com/v1/geocode?q={address}&lang=en-GB".replace(" ", "%20").replace(",", "%2C")
            # - make request
            res = requests.get(url, headers={"Authorization": stolenKey})

            if res.status_code != 200:
                raise Exception(f"Status: {res.status_code} returned")

            parsed = json.loads(res.text)

            if len(parsed["results"]) > 0:
                lat = parsed["results"][0]["center"]["lat"]
                lng = parsed["results"][0]["center"]["lng"]
                print(f"{i}, {lat} {lng}")
            else:
                print(f"{i}, N/A")


if __name__ == "__main__":
    main()
